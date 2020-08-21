# Sprint Planning

The purpose of sprint planning is to make sure that the team has accepted the correct items to work on, that those items are well-defined and small in scope, and that all tasks are expected to be completed before the sprint ends.

Based on the requirements for proper [estimation](./estimation.md), the sprint planning meeting should consist of the following steps:

1. Bring the project board up-to-date by moving any completed tasks and features to the "Done" column, if they are not already moved.  If any outstanding tasks or features are to be changed or killed, this should be discussed and decided as a team.

2. Prioritize the top 10 outstanding features in your backlog.  If you have more than 10 features, the remaining can be unprioritized.  This priority should be motivated by client expectations.

3. Define the [acceptance criteria](https://www.softwaretestinghelp.com/user-story-acceptance-criteria/) for each of these 10 features.  This should be motivated by client expectations.  If it is unclear what the acceptance criteria is, log an *exploration* issue to clarify and assign it to a team member.

4. Assign one feature to each team member, with top priority features being assigned first.  Do not assign a feature if its acceptance criteria is incomplete.  Move these assigned features to the "In Progress" column in the project board.  Each feature should be completed before assigning new features.

5. Identify any questions that need to be answered for each feature assigned.  Questions identified here should be technical, like deciding on what tool to use for implementation or exploring how the system should be architected.  Each of these questions should be logged as a *exploration* in GitHub Issues.

6. Identify any known tasks which are required to complete a feature.  These tasks will be technical, such as implementing code.  For each of these tasks, make sure to define acceptance criteria and validation techniques.  The task should include any required documentation, and meet code standards such as linting and regression testing.  The validation techniques should be specific enough that anyone on the team could execute them; preferably, the validation should be automated to facilitate regression testing in the future.

7. Identify any [chores](./issues.md) which the team should complete.  Since chores provide value for the team instead of the client, they should provide a positive return-on-investment for time spent.  If a chore is expected to save time over the course of the project, it should be worked on first.  If a chore is not expected to save time over the course of the project, it should not be worked on at all and should be closed.

7. Accept tasks into the sprint such that they could reasonably be expected to be completed during the sprint.  Prefer exploration over implementation to reduce risk.  For example, if issues are expected to take 2-4 hours to complete, and a sprint is a week, each member should be assigned 2-3 issues at the end of sprint planning; these should include any outstanding tasks which were not completed in the previous sprint.

At the end of sprint planning you should have:
- assigned exploration issues to clarify acceptance criteria
- a top-10 prioritized backlog of features, including acceptance criteria
- exploration logged as issues to clarify technical implementation
- chores logged as issues which are expected to save time over the course of the project
- tasks logged as issues to perform implementation, with defined acceptace criteria and validation techniques
- 2-3 assigned issues per team member.