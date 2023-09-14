# Git / GitHub Lab

## Objective

Gain practical experience in collaborative software development using Python and Git by forking, cloning, making code contributions, and creating pull requests in a shared repository, while learning essential version control and programming skills.

## Helpful Resources

- [Getting Started with Python](https://www.python.org/about/gettingstarted/)
- [Getting Started with Git](https://docs.github.com/en/get-started/getting-started-with-git)

![image](https://github.com/VedikaSrivastava/CS506-labs-Fall2023/assets/83489280/217b0f8f-1366-4e74-8d8a-f99dcc01e9ec)


### Lab Instructions

Please complete the items below in order.

1. [**Fork the Repository**](https://help.github.com/en/articles/fork-a-repo)
   - Go to the original repository on GitHub: [Data-Science-Fundamentals](https://github.com/gallettilance/Data-Science-Fundamentals)
   - Click on the "Fork" button in the top-right corner of the page.

2. [**Clone Your Fork Locally**](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
   - Open your terminal or command prompt.
   - Clone your forked repository to your local machine using the following command, replacing `<your-username>` with your GitHub username:
     ```shell
     git clone https://github.com/<your-username>/Data-Science-Fundamentals.git
     ```
   - Alternatively - copy the url of your repo (find it under "Code")
     ```shell
     git clone <url of your forked repo>
     ```

3. [**Add a Remote Named 'upstream'**](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories)
   - Change your current working directory to the cloned repository:
     ```shell
     cd Data-Science-Fundamentals\student-notes
     ```
   - Add a remote called 'upstream' that points to your forked repository:
     ```shell
     git remote add upstream <url of repo>
     ```

4. [**Create and Checkout a New Branch**](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches)
   - Create a new branch for your code changes. Replace `<branch-name>` with an appropriate branch name describing the component you are working on:
     ```shell
     git checkout -b <branch-name>
     ```

5. **Make some changes**
   - For this lab edit the `README.md` to include your name
   - Alternatively, if you feel confident, create a `.py` or `.ipynb` file to incorporate any changes.

6. **Add and Commit Your Changes**
   - [Add](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) your changes to the staging area:
     ```shell
     git add .
     ```
   - [Commit](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) your changes with a descriptive message:
     ```shell
     git commit -m "<Add description of changes>"
     ```

7. [**Push Your Changes to Your Fork**](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository)
   - Push the changes to your forked repository on GitHub:
     ```shell
     git push upstream <branch-name>
     ```

8. [**Create a Pull Request**](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
   - Go to your forked repository on GitHub.
   - You should see a banner with a "Compare & pull request" button for the branch you just pushed. Click on it.
   - Provide a descriptive title and any additional information about your changes in the comment box.
   - Click the "Create pull request" button.

Congratulations! You've successfully forked a repository, made code contributions, and created a pull request using Git.
<br><br>
### [Multi Author Commit](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors)
In collaborative software development, it's essential to properly attribute contributions to multiple authors in a commit. Here's how you can add multiple authors to a commit:

1. **Make changes to your file, stage your changes and commit**
   - For this lab edit the `README.md` to include your name and your collaborator's name
   - Alternatively if you feel confident, create or edit your `.py` or `.ipynb` file to incoporate any changes.


2. **Edit the Commit Message**
   - Open the commit message for editing with your preferred text editor:
     ```shell
     git commit --amend
     ```
     This opens the last commit message in your text editor.

3. **Add Co-authors**
   - In the commit message, add co-authors' information in this format:
     ```
     Co-authored-by: Name <email@example.com>
     ```
     Replace `Name` with the co-author's name and `<email@example.com>` with their email address. Add multiple co-authors by including multiple lines.
     - Press `i` to enter edit mode in your text editor

4. **Save and Close the Commit Message**
    - `Esc` + `:q` to quit without saving
    - `Esc` + `:wq!` to save and quit

5. **Push the Changes**


Keep in Mind
- **Merge** combines the changes from one branch into another, preserving the original branch's commit history and creating a new merge commit.
- **Rebase** moves or integrates the changes from one branch onto another, creating a more linear commit history without extra merge commits. It replays the branch's commits on top of the target branch.


**Lab will be considered complete once you have pushed your changes to your local PR and created a pull request with your collaborator**
