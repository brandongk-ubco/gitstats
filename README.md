# gitstats

This repository documents how to use the [GitHub project management](https://github.com/features/project-management) features to support an agile methodology.  It also provides code which uses [PyGithub](https://pygithub.readthedocs.io/en/latest/introduction.html) to query the [API](https://docs.github.com/en/rest) to track project progess and contributions for team members.

For a full list of what's included, see the [Table of Contents](./docs/technical/contents.md)

# Installing and Running gitstats

It is easy to run gitstats through [syzygy](https://ubc.syzygy.ca). You will need to:

1. Create a [personal access token](https://github.com/settings/tokens) in GitHub.  Note that these personal access tokens are applied on the user, not the repository.  If your repository is public, you do not need to provide it any scope; if your repository is private, you need to provide the `repo` scope.

1. Login to [syzygy](https://ubc.syzygy.ca) using your CWL

1. Look at the [example](./docs/examples/gitstats.ipynb) that exists in this repo.  You will need to change the access token variable to the access token you created above, as well as the group name and repository.  The repository is the GitHub path, including user name and repository name.

1. Run the script and observe the results.

It is also possible to run gitstats locally.  You will need to have a Python 3.6+ environment setup, and [anaconda](https://www.anaconda.com/products/individual) is suggested.  Install requirements using `pip install -r requirements.txt` and either run the example notebook through Jupyter or convert it to a simple script.

# Getting Stared

1) Make sure you understand [agile](./docs/technical/agile.md) and read the [manifesto](./docs/technical/agile_manifesto.md).  Also, read and understand the overview of the [software development lifecycle](./docs/technical/lifecycle.md).

1) As a team, understand the [roles](./docs/technical/roles.md) and agree on each member's role for the duration of the project.

1) Complete the [individual git exercise](https://people.ok.ubc.ca/bowenhui/499/gitex_indiv.html) to become familiar with using git for version control.

1) Complete the [team git exercise](https://people.ok.ubc.ca/bowenhui/499/gitex_team.html) to become familiar with using git as a team.

1) Have the DevOps / Technical Lead [setup the github repository](./docs/technical/git_basics.md).  Some features require a pro github account, which can be obtained using [GitHub for Education](https://education.github.com/pack) and your school e-mail address.

1) Have the DevOps / Technical Lead configure the [GitHub issue labels](./docs/technical/issues.md) and milestones needed.

1) Have the client liaison / product owner setup your first client meeting.  When you meet your client for the first time, introduce yourselves as well as your roles in the project. While your objective is to learn who your client is and the project details, you will need to keep in mind that your client is most likely not familiar with how this course works or what is expected of you or of them. Explain to them there is a course schedule and there are intermediate reports that will be created as part of the project that you will go over with them upon completion. Record the minutes of the first client meeting in the repostory.  Record the features requested by the client as user stories using [GitHub issues](./docs/technical/issues.md).

1) Have the project / scrum manager schedule your first sprint planning meeting, where you divide features into tasks and record any [exploration](./docs/technical/issues.md) that needs to be performed before proceeding with coding work.  Each task should be expected to take 2-4 hours, and exploration should be undertaken until this is possible.

# Weekly Expectations

- Have a team meeting where you perform a [retrospective](./docs/technical/retrospective.md) and [sprint planning](./docs/technical/planning.md).
- Accept 2-3 team issues per team member into the sprint, and have those issues completed by the end of the sprint.
- Assess team progress through a projection of feature completion, and identify any delays in milestone delivery early.
- Have a client meeting to prioritize features, identify acceptance criteria, and communicate team progress.

# Progress Evaluation

There will be [weekly progress evaluation](./docs/technical/evaluation.md), calculated both on individual contributions relative to the team and overall team progress.