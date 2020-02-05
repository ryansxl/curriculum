# Developer Relations Workflow with GitHub

## Stage Overview

Stage 1 (Pre-Review): DevRel Stage 1

Stage 2 (Post-Review): Continue Perfecting DevRel Stage 1 + DevRel Stage 2

Stage 3 (Kevin): Kevin conducts final review

Stage 4 (Writers): Writers re-style curriculum for grammar, writing style etc.

Stage 5 (Contentful): Writers copy and paste into Contentful

Additionally, Stages 1-3 are handled and marked within GitLab.

Stage 4 is the GitLab issue that Kevin will raise.

Stage 5 is Contentful.

## Stage Processes

Bullet points indicate steps to be completed, when all the bullet points are done in order, then the corresponding status for that stage should be marked in Airtable.

### Stage 0: Issues and Milestones

- Issues
  - Come up with issues
  - Different Types:
    - Context (explanations of underlying concepts)
    - Content (code and explanations of code)
    - Styling (separating cards into steps, typos, flow, only local images)
    - Visuals (custom visuals)
    - Create (need to create a new card)
    - Ordering (card ordering, moving content from card to card)
  - **Name your issue with this format**: Activity/Lab (task_number) (activity/lab name) (title)
  - Ex. Activity 2.2.1 Bookkeeper Visuals
  - For non-core modules, just include module name 
    - ex. Postman.1 Testing API Endpoints
  - **Assign difficulty label to each issue**
    1. Easy (1)
    2. Medium (2)
    3. Hard (3)
    4. Writing (4)
    5. Visuals (5)
  - **Assign issues to your team members**
    - with due date if necessary
- Milestones
  - To satisfy your quota and/or perk requirements
  - Reviewers will set milestones on GitHub on a weekly basis 
    - Generally speaking, devs will need to resolve issues with a **total weight of 10 per week** individually
      - If your reviewer asks you to do more to meet his or her quota, please do
    - Reviewers are responsible for merging 2 labs / 6 activities a week
    - Team PERK: merging 4 labs / 12 activities a week

### Stage 1: Before 1st Review

- Developers
  - Assigned issues to work in, usually in a specific lab/activity
    - Each activity/lab is in an assigned folder
    - Issue notifications can be found in top right corner
  - Create a branch named firstname_activityorlabname
    - ex. Kevin_AnalyzingTweetsActivity
  - Find issues to work on for your assigned activity/lab
  - Develop curriculum by DevRel Stage 1 Requirements
  - Devs upload folder of .md files to the folder assigned
  - Start **pull request** and assign to reviewer
  - **Reference the Issue you are working on in your MERGE REQUEST!**
    - Use "Closes #xx" with xx as your issue number in your merge request message
      - Ex. "Closes #10
  - Mark "Pre-Review" stage in GitLab "label"

> Note that Stages 2-4 are completed **in the same merge request!**

### Aside on Comments (Stages 2-4)

- Developers: For every single commit to a merge request, please put "/spend xx hours".
  - We would like to get a good idea of your work to place you in the right team

### Stage 2: After 1st Review

- Reviewer reviews .md files
  - Leave feedback in terms of **comments** on merge request
    - Check merge request notification in top right corner
    - Go to Merge request
    - Click on Changes tab
  - Reviewer leaves comments in Changes tab
    - Types of issues
      - Context (explanations of underlying concepts)
      - Content (code and explanations of code)
      - Styling (separating cards into steps, typos, flow, only local images)
      - Ordering (ordering of cards, moving parts of card content to another)
      - Visuals (custom visuals)
      - Create (need to create a new card)
    - Resolve all comments into an issue
      - Button in upper right
      - Repeat entire process to make multiple issues when necessary
- Developer responds to comments
  - By going to issue
  - Checking out a pull request's branch https://stackoverflow.com/questions/2236743/git-refusing-to-fetch-into-current-branch/19205680
    - then `git pull` to get latest code and work on comments locally
- Developer + reviewer work together to get all comment threads resolved
- Reviewer changes assignee to Kevin
- Mark "Post-Review" in GitLab "label"

### Stage 3: Final Review

- Kevin conducts one final review, makes comments where necessary
- Kevin works with reviewer and developers to resolve comments
- When all comments resolved, Kevin updates GitLab status to "Final Review", merges the request!

### Stage 4: Technical Writers

- Kevin raises an issue and changes assignee to writer
  - Writer will re-style curriculum
- When finished, writers mark status to "Final Edits"

### Stage 5: Contentful

- Writers copy and paste into Contentful, format accordingly
- Writers finish, publish within Contentful
