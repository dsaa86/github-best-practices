# Understanding Branches

## TL;DR

-   Branches allow us to separate the individual efforts of developers when they are working on different features.

-   Branches keep a track of changes so that we can fall-back to a working version of the code if a new error is introduced accidentally.

## Git from the very beginning

### - Git and Github are _**not**_ the same.

-   Git is a technology. It is the software that actually performs version control and manages all of the functionality that we know and love.

-   Github is a storage service that utilises Git in order to manage the files stored on its servers.

### - Git allows us to version control our software.

-   Version control is the process by which we can record incremental changes to our repos. Remember that a repo does not necessarily have to contain code.

-   Through Git we have a huge amount of control over what changes we record, and how we record these.

-   We are also able to use these change records to roll-back our code to a previous version. This is very useful if we introduce a bug through a change in code.

-   We can interact with Git in different ways

    -   We can use the Command Line Interface to write text-based commands for Git.

    -   We can use a GUI-based programme to visualise and interact with Git through a more typical computer programme. Ultimately this is still issuing CLI commands, it just does it in the background.

## How do we use branches?

### - Isolated development

-   Development of a software solution often takes place in parallel - there are lots of developers working on different features of the same software at the same time.

    -   This would be utter chaos if all of the developers were working on precisely the same files at exactly the same time.

-   One solution would be to just copy all of the files to each developer's computer and then for them to develop their feature with this local copy.

    -   This is exactly what we do when we run `git clone <insert repo name>`

-   Imagine that two developers are working on different features of a system

    -   Developer One is working on the login and authentication feature

    -   Developer Two is working on the stock and inventory feature of the system

    -   These features are seperate enough that they will not cause conflicts with each other when one or other of the developers submits their changes.

-   Developer One completes the requirements list for the login feature, tests the code, and submits for review.

    -   Git tracks all of the changes that Dev One has made to the code, and records this in comparison to the code that was originally cloned.

-   A few days later, Dev Two completes the stock feature and submits the code.

    -   Again, Git tracks all of these changes.

-   There are now effectively three versions of the code

    1. The original code
    2. The code modified by Dev One
    3. The code modified by Dev Two

-   As there are no clashes between Dev One and Dev Two's code, we can merge them all together to come up with a new version of the 'original' or 'master' code.

    -   This new version now reflects the changes made by both Dev One and Dev Two.

### - Version Control

-   A little while later, some changes need to be made to the user interface. This will affect the way that the login screen is displayed and also change the appearance of items of stock.

    -   The changes will NOT affect how the login and stock features work, the earlier code from Dev One and Dev Two won't be altered.

-   Instead of just cloning the code, Dev Three creates a new branch and clones the code in to this branch. This totally isolates the development of the new feature from the master code.

    -   The isolation will still exist even when Dev Three syncs the code to Github.

-   This means that Dev Three can make all the necessary changes; these can be tested, reviewed, tweaked, adapted, and fiddled with.

    -   Other developers can interact with these changes by cloning the new branch. They don't need to touch the 'master' branch in any way whatsoever.

-   When Dev Three is satisfied that the new feature has been implemented properly, the changes made can be merged in to the 'master' branch. The changes go 'live' to any end users of the code, and any future branches will also include this merged feature.

### - Code Resilience

-   A few years later, a dev is tasked with changing the login and authentication process.

-   A new branch is created, and the 'master' branch is cloned in to this.

-   The new dev makes the necessary changes to the codebase and it is merged in to the 'master'

-   After a few weeks, a user encounters an error that has been cause by the changes.

-   Using Git, the error can be fixed like this:

    1. The 'master' branch is rolled back to the last version that worked properly - this is from the last version **before** the new authentication feature was merged in.

        - Because Git tracks all changes, this is as easy as typing a one-line command in the Terminal

        - The 'live' code is now fixed, albeit without the new functionality.

    2. The dev can go back to the branch with the modified code and keep working on it until the error is fixed.

        - The preservation of the branch means that the dev doesn't have to do all of the work again

-   Once the error has been fixed, everything can be re-merged.
