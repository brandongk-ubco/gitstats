# Task Estimation

Accurately estimating the time to complete software is [complex](https://chrismm.com/blog/project-delays-why-software-estimates/) and [inaccurate](http://scribblethink.org/Work/Softestim/softestim.html), with some practitioners going so far as to [reject the practice entirely](https://www.youtube.com/watch?v=QVBlnCTu9Ms).  However, this difficulty does not negate the requirement to deliver usable software on time.

As a general rule, it is better to deliver 80% of features which are 100% functional than to deliver 100% of the features which are 80% functional.  Put another way, delivering lesser amounts of fully working software is preferable to making more, partially working software.  At the outset, it is very hard know how long it will take to make a feature 100% complete.  The main reason for this is unknown complexity.  Software development almost always contains some research element; if it didn't, the desired software would already exist, and it would usually be better just to use it.

<img src="./knowns.png?raw=true" width="400" style="float:right; margin-left:10px;" >

A general explanation for difficulty in estimation can be described as whether or not we know the task needs to be done, and whether or not we know how to do it.  This is usually phrased as [knowns and unknowns](https://medium.com/datadriveninvestor/known-knowns-unknown-knowns-and-unknown-unknowns-b35013fb350d).  The known knowns are easy to estimate, as not only do we know they need to be done, we also know how to do them.  Known unknowns present some risk, but this can be mitigated by starting exploration early to gain better understanding of how the task can be completed.  Unknown knowns present a higher degree of risk, as the task is unidentified; when it is uncovered, some amount of time will need to be spent to complete the task, and the task may be complicated so that it takes a lot of time.  However, the biggest risk are the unknown unknowns, or the things we both don't know need to be done and don't know how to accomplish; such tasks exist in almost every software project, and make a priori accurate estimation virtually impossible.

There are a few strategies which can be used to help better plan a project:

- A priori estimation is almost always wrong, so don't spend large amounts of time trying to do it.
- Embark on exploration tasks early to gain better understanding of what needs to be done or how it should be accomplished.
- Commit to completing only small, well-defined tasks; this limits unplanned time investment.
- Once work has begun, continue on a feature until it is closed, either because it is complete or because enough knowledge has been gained to conclude that the feature is not worth completing.

These strategies come together to create a simple workflow:

- Maintain a prioritized backlog, and work on higher priority features first.
- Work only one a small number of features at a time (preferably one per developer), which encourages completion of outstanding work.
- Before starting to code, break features down into small, well-defined tasks; this will surface any misunderstandings or questions which need to be answered.
- The entire team should particiapte in the feature -> task breakdown, and the entire team should be in agreement that the tasks are well-defined and small.  If one team member disagrees with the others, they either misunderstand the task, so that it needs to be better defined, or they see some complexity in the task that the others have missed.  Either situation should be resolved before proceeding with work.
- Correct any misunderstandings and answer any questions early by embarking on exploration tasks before coding.

If such a process is followed, estimation of each task is unnecessary as the team has agreed that every task is small and similar in size to other tasks.  Moreover, estimating features is avoided; feature completion is simply the completion of underlying tasks.  Finally, a projection of the completion date for a feature can be calculated by looking at the time used to complete previous tasks and the number of tasks outstanding; since every task is of similar size, the projected completion date is of relatively high accuracy.  If, during exploration, it becomes clear that the feature is not worth the investment, the feature can removed from the project.