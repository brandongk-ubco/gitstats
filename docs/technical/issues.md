One of the key components of [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) is high visibility of the work being embarked upon.  This allows the team, management, or client to see quickly and easily the plan and progress.  In this project, we will achieve visibility through [GitHub Issues](https://guides.github.com/features/issues/) and [GitHub Projects](https://github.com/features/project-management).

# Types of Issues

<img src="./labels.gif?raw=true" width="400" style="float:right; margin-left:10px;" >

Delete the default labels and create labels for the following four types of issues.  They will be used to track progress.

## Feature

A feature is a [user story](https://www.productplan.com/glossary/user-story/), and consists of a description of the user(s) ability to complete certain goals using the system.

## Task

A task is a step in the process to completing a feature.  A feature is completed when underlying tasks are completed.  Usually, tasks will include many aspects such as coding, testing, and documentation.  The task should be fully contained, such that all aspects of delivering the task are in a single issue.  In short, you should not have a coding task and a separate documentation task; they should be completed and delivered at the same time.

## Exploration

Exploration is required when breaking a feature into tasks is not possible, either because you are unclear what needs to be done or unclear how it should be accomplished.  These exploration tasks should be embarked upon early to limit risk to the project and/or time invested in features which turn out to be too complex to be worth completing.

## Chore

A [chore](https://scrumdictionary.com/term/chore/) is an item which provides value to the team rather than the client.  Examples include implementing [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration), [linting](https://en.wikipedia.org/wiki/Lint_(software)) the project, or [refactoring a codebase](https://en.wikipedia.org/wiki/Code_refactoring).

Generally, the client doesn't care whether or not a chore is completed.  They can be seen as implementation details from their perspective.  However, chores can create tools which speed up development.  They should be embarked upon in the return-on-investment is high; that is, completion of the chore will save more time than the work it took to implement.

