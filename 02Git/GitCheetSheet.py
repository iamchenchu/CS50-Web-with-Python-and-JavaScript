"""**Most Used Commands**

**Initializing and Cloning Repositories**
git init: Initializes a new Git repository locally.
git clone [url]: Creates a copy of an existing repository from a URL.

**Basic Local Repository Operations**
git status: Shows the status of changes as untracked, modified, or staged.
git add [file/directory]: Adds files or directories to staging.
git commit -m "[commit message]": Commits staged changes with a message.
git diff: Shows file differences not yet staged.
git diff --staged: Shows file differences between staging and the last file version.

**Branching and Merging**
git branch: Lists local branches.
git branch [branch-name]: Creates a new branch.
git checkout [branch-name]: Switches to a different branch.
git merge [branch]: Merges the specified branch into the current branch.
git branch -d [branch-name]: Deletes a branch.

**Stashing and Cleaning**
git stash: Temporarily stores all modified tracked files.
git stash pop: Restores the most recently stashed files.
git clean -n: Shows which files would be removed from working directory.

**Working with Remote Repositories**
git fetch [remote]: Fetches changes from the remote but doesn’t merge them.
git pull [remote]: Fetches changes from the remote and merges them.
git push [remote] [branch]: Pushes local branch commits to the remote repository branch.
git remote -v: Lists all currently configured remote repositories.

**Tagging and Logging**
git tag: Lists tags.
git tag [tag-name]: Creates a new tag.
git log: Displays the commit history.

**Undoing Changes**
git reset [file]: Unstages the file, but preserves its contents.
git reset [commit]: Resets to a particular commit in your history, losing all changes that came after it.
git checkout -- [file]: Discards changes in the working directory.
git revert [commit]: Creates a new commit that undoes all of the changes made in the specified commit.

"""