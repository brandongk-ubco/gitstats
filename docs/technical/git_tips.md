# Git Flow

There is a very common [git flow](https://nvie.com/posts/a-successful-git-branching-model/) and a [good tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) on it.

The basics of gitflow are:
- A develop branch is created from master
- A release branch is created from develop
- Feature branches are created from develop
- When a feature is complete, it is merged into the develop branch
- When the release branch is done, it is merged into develop and master
- If an issue in master is detected, a hotfix branch is created from master
- Once the hotfix is complete, it is merged to both develop and master

# Setup a correct .gitignore.
There's a whole [list](https://github.com/github/gitignore) of them to chose from.  When possible, prefer whitelisting over blacklisting.  That is, setup your .gitignore to:

```
**
!myfile
!mydirectory/
!mmydirectory/otherfile
```

Note that when doing this, you must first disignore any directories, then any files in the directory.  If you don't disignore the directory, the parser won't even enter it to look for files.

# Setup protected branches
[Protected branches](https://help.github.com/en/articles/about-protected-branches) should be used at minimum for [integration branches](./git_basics.md).  This stops amending / force pushing to common code branches and breaking things, or deleting Master (which I've actually seen done once in a production app).

# Merge develop back into feature branches BEFORE merging the feature branch into develop. 

In protected branches, you can enforce that branches are up-to-date before merging. Do NOT use Github's "resolve conflicts" button.  This feature can break things, and even comes with a giant warning: https://help.github.com/en/articles/resolving-a-merge-conflict-on-github 

# Prefer resolving conflicts locally then pushing the resolution to Github.

You can also enforce code reviews before merging PRs with protected branches, which is a good idea. Never use "Squash and Merge", and better yet use the option to disable it entirely.

# Use merge commits exclusively with common branches.

https://github.blog/2016-04-01-squash-your-commits/  You can get bad (really, really bad, where the entire code base is a conflict) merge conflicts if branches share some commits and then one branch squashes on merge to develop.

# (Try to) NEVER force push.

Force pushing is a destructive operation.  The better option is to append commits, undoing whatever the problem is you're trying to fix.  If absolutely necessary, it's better to use force-with-lease: https://blog.developer.atlassian.com/force-with-lease/

# If all else fails and code is lost by some destructive git operation, you can usually get it back with the reflog

The [reflog](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog) is a dangerous tool, and can make things worse if misused.  I've only needed it twice in about 4 years of using Git extensively at work.

# Git matches commits to contributors based on e-mail.

You should [setup git](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) with your correct name and e-mail address to make sure they link up.
