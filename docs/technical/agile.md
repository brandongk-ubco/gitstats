# Agile Software Development

Agile software development is founded on self-organizing, cross-functional teams which rapidly adapt to changing requirements in order to devliver valuable software to the customer quickly and frequently.  The values are principles are defined in the [agile manifesto](./agile_manifesto.md).

There are two common frameworks which are inspired by this manifesto: scrum and kanban.  [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)) employs timeboxed sprints, with the scope of the sprint being agreed to by the team before starting, and the expectation that all work assigned be finished by a pre-determined time (usually after 2 - 4 weeks of work).  [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) mandates high visibility of progress as work is undertaken, and the agreement that tasks will not exceed capacity to maintain a sustainable work environment for all.  Often, Scrum and Kanban are used together, and this is the approach taken in the capstone projects.

Since agile is an iterative framework that encourages rapid changes in requirements, individual tasks are expected to be very small, and the team has a [definition of done](https://www.productplan.com/agile-definition-of-done/) which is expected to be met for all tasks.  In this case, tasks are expected to take 2-4 hours to complete, and the definition of done is as follows:

- The acceptance criteria are met and the validation techniques are satisfied
- Code is peer reviewed
- Code is merged to develop via Pull Request
- develop is merged to master via Pull Request
- Code/feature passes regression testing
- Code/feature passes smoke testing
- Code is documented inline with PyDoc, JSDoc, JavaDoc or similar.
- Technical documentation is updated for system-level decisions / diagrams
