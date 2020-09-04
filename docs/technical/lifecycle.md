<img src="./SDLC.png?raw=true" width="200" style="float:right;margin-left:10px;" >

# Software Development Lifecycle

The [software development lifecycle](https://en.wikipedia.org/wiki/Systems_development_life_cycle) defines a general process for creating software.  It consists of 5 steps: Planning, Analysis, Design, Implementation, and Maintenance.  There are many different implementations of this general lifecycle, but in this project we will adhere to the [agile](./agile_manifesto.md) methodology, where these steps are performed iteratively and repeated often.  This allows for quick adaptation to changing requirements and priorities.  Fast iteration requires small tasks that are [completed](./agile.md) often.

# Planning

## Requirements Gathering

Requirements are gathered from the client and logged as [user stories](https://www.productplan.com/glossary/user-story/) which are called features.  Features are not required to be completable in a single sprint.  These stories are put into the [backlog](https://www.agilealliance.org/glossary/backlog/).  Each story is required to have [acceptance criteria](https://www.productplan.com/glossary/acceptance-criteria/), which are a definition of what the client or team would expect a completed deliverable to accomplish.

## Sprint Planning

During [sprint planning](./planning.md), features in the backlog are refined into deliverable tasks and accepted to be worked upon.  Each task is expected to take 2-4 hours to complete fully.  If it is unclear how to proceed with a feature, or how long a task will take, then [exploration](./issues.md) must be performed; this exploration must be completable in the same timeline as a task, and produce a clear deliverable (e.g. pros-cons list or small prototype) which can be reviewed by the entire team.  Each task / exploration must have a clear outcome defined through acceptance criteria and validation techniques.  Validation techniques define *exactly* how you will guarantee that the acceptance criteria have been met; for code deliverables, for example, passing linter requirements, code review, and the creation of automated tests are common validation techniques.

The outcome of sprint planning is a list of tasks accepted into the sprint.  These tasks are well-defined, work towards the completion of features, and are expected to be completable during the sprint.  For example, if each tasks is 2-4 hours, sprints are one week long, and each member is expected to do 6 - 10 hours of work per week, then each member should be assigned 2-3 tasks at the start of each sprint.

# Design & Implementation

In the agile method, design and implementation are usually done together as much as possible during the completion of [issues](./issues.md).  There are some overarching design decisions that need to be made, such as what programming language to use and the overall system architecture.  These should be completed as exploration issues, with the deliverables checked in to the repository.  For the programming tools, for example, the deliverable could include a description of constraints and pros / cons list.  For the system architecture, your group should produce [Data Flow Diagrams](https://people.ok.ubc.ca/bowenhui/310/8-DFD.pdf) for both Level 1 (showing the interaction with external systems) and Level 2.

# Maintenance

The maintenance stage of the lifecycle is limited in prototype development, as the system is not in widespread use.  However, there is a very common maintenance requirement which your team will engage in: automated regression testing.  Automated regression testing is extremely valuable over the life of a project; without it, the time to execute manual tests goes up as each new feature is added.  Automated testing is much faster, so can be easily done at many more points in the development process (i.e. before merging a PR, after merging a PR, as part of a developer's workflow).

# Analysis

The lifecycle is a circle, showing that the process has no beginning and no end; analysis comes both at the beginning and the end of a feature.  The first thing you must do is analyze what you are attempting to complete, and produce good acceptance criteria and validation techniques to make sure that the software is solving problems the client needs resolved.  Once a feature is deployed, you must also analyze if it has met its goal through client and user feedback, and determine if there is anything that should be changed.
