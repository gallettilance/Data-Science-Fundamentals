import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import tqdm

# Load data
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
full_df = [train_df, test_df]

# Extract titles from names
def extract_title(name):
    return name.split(',')[1].split('.')[0].strip()

# Features
for dataset in tqdm(full_df):
    # Has cabin
    dataset['has_cabin'] = dataset['Cabin'].notna().astype(int)
    
    # Family members
    dataset['family_members'] = dataset['SibSp'] + dataset['Parch'] + 1
    
    # Title
    dataset['Title'] = dataset['Name'].apply(extract_title)
    common_titles = dataset['Title'].value_counts()[dataset['Title'].value_counts() > 10].index
    dataset['title_type'] = dataset['Title'].apply(lambda x: 1 if x in common_titles else 0)
    
    # Fare price
    dataset['Fare'] = dataset['Fare'].fillna(dataset['Fare'].mean())
    dataset['fare_price'] = pd.cut(dataset['Fare'], bins=3, labels=[0, 1, 2])
    
    # Two additional numerical features
    dataset['fare_to_age_ratio'] = dataset['Fare'] / dataset['Age']
    dataset['family_to_age_ratio'] = dataset['family_members'] / dataset['Age']

# Features and target
features = ['Pclass', 'Sex', 'Age', 'Fare', 'family_members', 'has_cabin', 'title_type', 'fare_price', 'fare_to_age_ratio', 'family_to_age_ratio']
target = 'Survived'

# Define preprocessors for numerical and categorical features
numeric_features = ['Age', 'Fare', 'family_members', 'fare_to_age_ratio', 'family_to_age_ratio']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_features = ['Pclass', 'Sex', 'title_type', 'fare_price']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Define model pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('rf', RandomForestClassifier(random_state=42))
])

# Define hyperparameters for grid search
param_grid = {
    'rf__n_estimators': [100, 200, 300],
    'rf__max_depth': [None, 10, 20],
    'rf__min_samples_split': [2, 5, 10],
    'rf__min_samples_leaf': [1, 2, 4]
}

# Grid search with cross-validation
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(train_df[features], train_df[target])

# Best model from grid search
best_model = grid_search.best_estimator_

# Predict on test set
predictions = best_model.predict(test_df[features])

# Save predictions to CSV
submission_df = pd.DataFrame({'PassengerId': test_df['PassengerId'], 'Survived': predictions})
submission_df.to_csv('submission.csv', index=False)