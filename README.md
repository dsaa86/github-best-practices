# Github Best Practices

## TL;DR

There is no tl;dr...make sure that you read the file, please.

## Purpose

As a team of developers, it is crucial that we are able to track the progression of a software solution from conception to delivery. Git as a technology, which is seperate to Github, allows us to perform version control on a repository. Github is merely a service that allows us to move a repository to the Cloud to allow for easier distributed development.

This document will guide you through the processes for best-practice version control of software development for small teams. Please note that there are multiple ways of implementing a version control policy, however, this method is a proven way of enabling small teams to track software versions without adding too much overhead to any individual person.

## Process

Unless otherwise stated, all steps are on your local machine.

### 1. Initialise a local repo

1. Using Terminal / PowerShell, navigate to the directory where your development projects are saved.

2. Create a new folder for your project.

    ```
    mkdir <insert folder name>
    ```

3. `cd` in to the folder and then type `git init`. You should see some output stating that an empty repository has been created.

### 2. Create a remote repo

If the remote repo already exists on Github then skip this step.

Go to Github and create a repository. Leave the default settings as is, but ensure that you select a repo name that clearly articulates the purpose of that repository.

Spend some time considering this name - we will be referring to it for a long time in to the future.

### 3. Clone the repo to your local machine

In Github, ensure that you have opened the repo page. In the 'code' tab of the repo, you should see a green button that says 'code'.

-   [Code button](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/GithubRepoCodeButton.png)

Select the button and ensure that 'HTTPS' is selected, then copy the URL that is displayed in the drop-down option box.

On your local machine, go to Terminal / PowerShell and ensure that you are still in the new Git dir that you just created. Type `git clone <url>`, replacing `<url>` with the URL that you just copied.

Press enter. The repo should be cloned to your local machine.#

If you are asked for authentication tokens, read [this guide]().

Type `ls -l` to view the files that you have just cloned to your system.

### 4. Understanding branches

If you are unsure of what Git allows us to do and what a branch is, then read [this guide]()

### 5. Create a branch for your new feature

When creating **_any_** new feature, no matter how small, you **must** create a new branch and develop on this branch.

We must first make sure that our repo is up-to-date with the `main` branch. To do this type:

```
> git checkout main
> git pull
```

This will ensure that the main branch is selected as the 'current' branch on your local machine, and then pull down any changes that have been made since you last performed a pull.

We then need to create a new branch and switch to this branch.

```
> git checkout -b <new branch name>
```

Make sure that you choose a branch name relating to the feature that you are developing.

### 6. Make regular commits

Every time you make a change to your code, you should commit this change to your repo. I can't stress this enough!

If you are unsure what commits and the structure of a repo looks like, read [this guide]()

You should make a commit when you have implemented a significant function, or when you have completed a specific requirement, or when you have written the tests that test a specific requirement or feature.

Small commits regular and often allow you to roll back any changes that later break the code. One large, infrequent commit can cause problems if you need to refactor a change that has broken the code.

1. Add any new files that you may have created since the last commit.

    ```
    > git add --all
    ```

    or

    ```
    > git add <file name>
    ```

2. Commit all of your changes

    ```
    > git commit -m "<insert commit message>"
    ```

Your commit message should be a short summary of what changes have been made since the last commit.

For best practice on writing commit messages, see [this guide]()

### 7. Pull and merge remote changes

If you have completed developing your feature, or it is the end of the day, or you need help with a specific problem, then it is time to push your local repo up to the remote repo.

Essentially, feel free to push your changes whenever feels right. Remember, if your local machine is damaged beyond repair, then your local repo is also gone for good!

1. It is imperative to ensure that _**any**_ changes made to the `main` branch are synced to your local repo.

    If you skip this step, you are risking a world of pain in merge conflicts. I've learned the hard way - don't skip this step.

    ```
    > git checkout main
    ```

    This will switch the 'working' branch back to `main`

2. Pull any changes from the `main` branch down to your local repo

    ```
    > git pull
    ```

3. Switch back to your development branch

    ```
    > git checkout <name of your branch>
    ```

    Don't miss this step or you'll run in to some weird errors in the next few steps.

4. Merge any changes from the `main` branch in to your feature branch.

    ```
    > git merge main
    ```

### 8. Push all of your changes to the remote

Once you have managed all of the steps above, the push process is actually fairly easy.

```
> git push -u origin <name of your branch>
```

## That's it ... almost ...

OK, so you have created a local repo; cloned a remote repo in to it; created a new branch for your feature; developed your new feature; tested your new feature; and then pushed your new feature up to the remote.

What's next?

We need to integrate your new feature in to the `main` branch.

### 9. Creating a pull request (PR)

On Github, open the repository and then click "Pull Request" in the top menu.

-   [Top menu bar](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/GithubRepoMenuBar.png)

Create a new pull request, ensuring that your new branch is set as the 'source' and the `main` branch is the 'destination', this should be automatically selected.

-   [Create pull request button](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/GithubNewPullRequestButton.png)
-   [Create pull request popup](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/GithubNewPullRequestPopup.png)
-   [Branch selection](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/GithubNewPullRequestBranchSelection.png)

In any normal situation, there should be no need for you to issue a pull request that merges to any branch other than `main`.

Add details to the PR form that will allow the code to be reviewed prior to merging the changes in to `main`. In particular, add in the details of your code reviewer and anybody else who should be aware of this pull request.

-   [Pull Request change form](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/GithubNewPullRequestDialog.png)
-   [Pull request reviewers](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/GithubNewPullRequestAssignees.png)

**_Your code will automatically be tested when the pull request is submitted. If you do not have 100% passing tests, your pull request will be rejected._**

Once your tests are passing, the request will be passed to the reviewer. At this stage there may be some back and forth as you resolve queries and update code to satisfy the code review.

-   [Tests being performed](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/PullRequestPerformingTests.png)
-   [Tests failed](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/PullRequestFailedTests.png)
-   [Test failure report](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/PullRequestFailedTestsDetails.png)
-   [Tests passing](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/PullRequestPassingTests.png)

Once any changes have been made and your code is ready to go, all of your changes will be merged with the `main` branch.

## If you wish to visualise the branches and commits

1. Open the Source Control extension. This should be installed by default.

    - [Source Control extension](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/OpenSourceControl.png)

2. Select the 'Git Graph' button from the top of the extension. In this image, it is the right-most button.

    - [Git Graph Button](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/SelectGitGraph.png)

3. View the git graph. This shows the branch history, user history, and commit history for the entire repo. You can filter this view in numerous ways to fit your needs.
    - [Git Graph](https://github.com/dsaa86/github-best-practices/blob/main/resources/images/GitGraph.png)

## You're done!

That's it. Your feature has been developed and the changes accepted.

Your code is now a part of the main codebase.
