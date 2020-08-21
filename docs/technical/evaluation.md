# Evaluation

The team will receive a mark for their progress, and each individual will have that mark adjusted for their effort relative to their team members.  Three criteria will be used for marking:

- Inidividual contribution relative to the team, measured through:
    - [participation in completed pull requests](./git.md)
    - number of comments on completed pull requests
    - number of commits on completed pull requests
    - number of changes on completed pull requests
- Weekly team progress through the completion of [issues](./issues.md)
- Overall team progress through feature delivery at pre-defined milestones.

# Weekly Score

## Realtive Individual Contribution

Weekly individual contribution will be relative to the team.  The formula for calculating the contribution will be given as:

<img src="https://latex.codecogs.com/png.latex?\Large&space;\text{effort}= 5 * \frac{\sum \hat{p}_i}{\sum p} + 5 * \frac{\sum \hat{c}_i}{\sum c} + 3 * \frac{\sum \hat{h}_i}{\sum h} + 2 * \frac{\sum \hat{o}_i}{\sum o}" style="background:white;padding:10px;"/>

Where:
 - p is the number of completed pull requests
 - c is the number of commits on completed pull requests
 - h is the number of changes (line additions or subtractions) on completed pull requests
 - o is the number of comments on completed pull requests
 - i indicates the amount completed by the individual

If any of the denominators are zero, that component will be ignored.

The total effort is then normalized such that the highest score receives 100%.

## Weekly Team Progress

Team progress will be calculated as a fraction of expected progress.  It will be calculated as:

<img src="https://latex.codecogs.com/png.latex?\Large&space;\text{progress}= min(\frac{\sum \hat{t} + \hat{e} + \hat{c}}{\sum \tilde{t} + \tilde{e} + \tilde{c}}, 1)" style="background:white;padding:10px;"/>

Where
 - t is the number of tasks
 - e is the number of exploration tasks
 - c is the number of chores
 - the numerator is a count of those completed
 - the denominator is the expected number to be completed, given as 2 times the number of team members.

 Note that you will not get a score more than one for completing more than the expected number of tasks.  It is better to work consistently to promote team sustainability.

 ## Final Weekly Score

The final weekly score will be assigned to each individual through a combination of team progress and individual effort.

 <img src="https://latex.codecogs.com/png.latex?\Large&space;\text{score}= \text{progress} * \text{effort}" style="background:white;padding:10px;"/>

 Note that:
  - progress is in [0,1], and is the same for all team members.
  - effort is in [0,1], and is not the same for all team members.

# Milestone Score

A score will be assigned to a team based on the number of features completed at each milestone.  This is a somewhat subjective process... **TODO**?