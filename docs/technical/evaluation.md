# Evaluation

The team will receive a mark for their progress, and each individual will have that mark adjusted for their effort relative to their team members.  Three criteria will be used for marking:

- Inidividual contribution relative to the team, measured through:
    - [participation in completed pull requests](./git.md)
    - number of comments on completed pull requests
    - number of commits on completed pull requests
    - number of changes on completed pull requests
- Weekly team progress through the completion of [issues](./issues.md)
- Overall team progress through feature delivery at pre-defined [milestones](./project_management.md).

# Weekly Score

## Realtive Individual Contribution

Weekly individual contribution will be relative to the team.  The formula for calculating the contribution will be given as:


<img src="./contribution.png?raw=true" style="background:white;padding:10px;"/>

Where:
 - p is the number of completed pull requests contributed to
 - c is the number of commits on completed pull requests
 - h is the number of changes (line additions or subtractions) on completed pull requests
 - o is the number of comments on completed pull requests
 - i indicates the amount completed by the individual

 Each element is calculated as a piecewise linear function of the expected number for a week.  The expected contribution per week is:

- Create 4 commits (merge commits are excluded)
- Generate 200 changed lines of code (excluded merge commits)
- Contribute to 4 pull requests (ideally 2 as a coder and 2 as reviewer)
- Create 4 comments on pull requests.

Linear interpolation with a slope of 1 between 0 and the expected contribution is used for each category; above the expected contribution, the slope is reduced to 0.25; the maximum score for each category is 1.25.

<img src="./non-linear-contributions.png?raw=true" style="background:white;padding:10px;"/>


## Weekly Team Progress

Team progress will be calculated as a fraction of expected progress.  It will be calculated as:

<img src="./progress.png?raw=true" style="background:white;padding:10px;"/>

Where
 - t is the number of tasks
 - e is the number of exploration tasks
 - c is the number of chores
 - the numerator is a count of those completed
 - the denominator is the expected number to be completed, given as 2 times the number of team members.

Note that you will not get a score more than one for completing more than the expected number of tasks.  It is better to work consistently to promote team sustainability.

 ## Final Weekly Score

The final weekly score will be assigned to each individual through a combination of team progress and individual effort.

<img src="./score.png?raw=true" style="background:white;padding:10px;"/>

 Note that:
  - progress is in [0,1], and is the same for all team members.
  - effort is in [0,1], and is not the same for all team members.
