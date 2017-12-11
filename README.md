# Track My Team!

Track My Team: A web app that will track all sports team events. This web app uses Django as the web framework alongside Python and Javascript.

## Week 1

### Requirements

#### Part 0: Tutorials

#### Part 1: Navigation Bar

Create a navigation bar that will appear at the top of every page. This will allow the user to easily access the views.

#### Part 2: Signup and Login

Create signup and login forms on individual pages for users to create an account if they do not have one or to access their account if they do have an account. It is okay if there are duplicate users that create an account.

#### Part 3: User Interface - Captains and Players

Captain
- Create a team profile
    - Create a roster within that team
    - Create a page to view all events (optional)

Player
- View team profile
    - View roster of team
    - Display a page to view all events (optional)

#### Part 4: Interacting with Django Database

Store the signup/login inputs, team profile information, and roster into the database. Retreive information stored in the database to display the team profile and roster for players, those who are not captains of a team.

#### Part 5: Testing

Create a manual test plan for this week. Write a test plan including screenshots and specific steps for a human tester to follow - what a tester should do and what he/she should observe.

### Grading Rubric

| Category | Weight | Scoring | Requirement |
| --- | --- | --- | --- |
| Basic Preparation | 2 | 0-1 | Ready to go at the start of section |
| Cleverness | 2 | 0-2 | The hardest points on the rubric |
| Rubric | 2 | 0-1 | Submitted a grading rubric |
| Code Submission | 4 | 0-2 | Submitted correct content on time and to the correct location in the repository |
| Decomposition | 4 | 0-2 | Project is adequately decomposed to different classes and methods |
| Documentation | 4 | 0-2 | Comments for each class and each function are clear and are following style guides |
| Effort | 2 | 0-2 | Perform considerable amount of work |
| Naming | 2 | 0-2 | Variable names and method names are readable and are following the naming conventions of the language you chose |
| Overall Design | 5 | 0-2.5 | Have nice approaches and structures in overall |
| Participation | 5 | 0-2.5 | Interact with the group 2 times (ask a question, make a comment, help answer a question, etc.) |
| Presentation | 4 | 0-2 | Present the code clearly |
| Requirement - Navigation Bar | 2 | 0-1 | 0 points: No navigation bar; 1 point: Navigation bar |
| Requirement - Signup/Login | 4 | 0-2 | 1 point: Created a signup OR login form; 2 points: Created both signup AND login form |
| Requirement - Captain UI | 5 | 0-2.5 | 2 points: Basic UI for adding team profile and roster; 2.5 points: Basic UI for ALL the views |
| Requirement - Player UI | 5 | 0-2.5 | 2 points: Basic UI for viewing team profile and roster; 2.5 points: Basic UI for ALL the views |
| Requirement - Database | 5 | 0-2 | 2 points: Ability to store inputs in database OR retreive from database; 2.5 points: Ability to store inputs in database AND retreive from database |
| Testing | 4 | 0-2 | 0 points: No test plan; 2 points: Manual test plan |
| Schedule | 2 | 0-1 | Revised final project schedule if necessary |
| **Total** | **63** | | |

## Week 2

### Requirements

#### Part 1: User Interface - Captains

Improve the previous week's user interface. Figure out how to submit the forms and send data to database. Also, allow the team captains to be able to edit the team profile and roster. Create a team profile dashboard that will have access to the team roster and event pages.

#### Part 2: Displaying Event Page

Create a calendar or list view of all events happening in the team. The team captain should be able to add/remove and edit all events. Also, make it possible for events to be recurring. When editting recurring events, make sure it can change for just one event.

#### Part 3: Accessing Event Details

When events are clicked, all the details will display including: time and date, location, and event details. Also, import a map to show the location as well as allow for any attachments or notes to be uploaded with the event. For example, the workout of the week or drills worked on at practice.

#### Part 4: Player Profiles

Clicking on a players name in the team roster should open a new page with the player's profile, he/she will be able to edit their information and add an avatar. Also, redesign the team roster current page to be able to switch between a grid view with avatars and a list view.

#### Part 5: Testing

Expand the manual test plan for this week. Write a test plan including screenshots and specific steps for a human tester to follow - what a tester should do and what he/she should observe.

### Grading Rubric

| Category | Weight | Scoring | Requirement |
| --- | --- | --- | --- |
| Basic Preparation | 2 | 0-1 | Ready to go at the start of section |
| Cleverness | 2 | 0-2 | The hardest points on the rubric |
| Rubric | 2 | 0-1 | Submitted a grading rubric |
| Code Submission | 4 | 0-2 | Submitted correct content on time and to the correct location in the repository |
| Decomposition | 4 | 0-2 | Project is adequately decomposed to different classes and methods |
| Documentation | 4 | 0-2 | Comments for each class and each function are clear and are following style guides |
| Effort | 2 | 0-2 | Perform considerable amount of work |
| Naming | 2 | 0-2 | Variable names and method names are readable and are following the naming conventions of the language you chose |
| Overall Design | 5 | 0-2.5 | Have nice approaches and structures in overall |
| Participation | 5 | 0-2.5 | Interact with the group 2 times (ask a question, make a comment, help answer a question, etc.) |
| Presentation | 4 | 0-2 | Present the code clearly |
| Requirement - UI | 4 | 0-2 | 1 point: Forms will send to database and team captains can edit team profile and roster; 2 points: Improve team profile view so UI has furnished design |
| Requirement - Event Page | 6 | 0-3 | 1.5 points: Basic list or calendar view for all events; 3 points: User can add/remove, edit and view team events (includes recurring events) |
| Requirement - Event Details | 4 | 0-2 | 1 point: Events are clickable to view event page details; 2 points: Include Google Maps and attachments into the event page detail |
| Requirement - Player Profile | 6 | 0-3 | 2 points: Names on roster are clickable and have a basic player profile with name, address, phone number; 3 points: Player profiles can be editted and upload an avatar to their profile |
| Testing | 5 | 0-2.5 | 0 points: No new test plan; 2.5 points: Manual test plan |
| Schedule | 2 | 0-1 | Revised final project schedule if necessary |
| **Total** | **63** | | |

## Week 3

### Requirements

#### Part 1: User Registration

Fix Week 1's user registration form so that new users add to the database. Also, make sure when a user tries to make a new account to double check with the database. Don't add a user if it already exists in the database. Salt and hash password stored in the database so that as the admin, he/she cannot see what all ther user's passwords are.

#### Part 2: User Authentication

The user interface should be able to check with the database and only allow the user to continue if their email and password matches. Allow for user session which means the user can be stayed logged in once authenticated for a period of time and also logout once he/she is done using Track My Team. When the user successfully logins, the pages should display different data depending on user login.

#### Part 3: User Interface - Captain vs. Player

For each team, a user is either an admin (captain) or a regular player. The pages should display different information between a captain and player. Captains will have access all the editting features whereas players can only see all the profile information and events.

#### Part 4: Events

Redesign the event page so it looks refurnished. For each event, the event detail page will include a Google Map of the set location. In addition, make it possible for events to be recurring. When editting recurring events, make sure it can change for just one event.

#### Part 5: Testing

Expand the manual test plan for this week. Write a test plan including screenshots and specific steps for a human tester to follow - what a tester should do and what he/she should observe.

### Grading Rubric

| Category | Weight | Scoring | Requirement |
| --- | --- | --- | --- |
| Basic Preparation | 2 | 0-1 | Ready to go at the start of section |
| Cleverness | 2 | 0-2 | The hardest points on the rubric |
| Rubric | 2 | 0-1 | Submitted a grading rubric |
| Code Submission | 4 | 0-2 | Submitted correct content on time and to the correct location in the repository |
| Decomposition | 4 | 0-2 | Project is adequately decomposed to different classes and methods |
| Documentation | 4 | 0-2 | Comments for each class and each function are clear and are following style guides |
| Effort | 2 | 0-2 | Perform considerable amount of work |
| Naming | 2 | 0-2 | Variable names and method names are readable and are following the naming conventions of the language you chose |
| Overall Design | 5 | 0-2.5 | Have nice approaches and structures in overall |
| Participation | 5 | 0-2.5 | Interact with the group 2 times (ask a question, make a comment, help answer a question, etc.) |
| Presentation | 4 | 0-2 | Present the code clearly |
| Requirement - Registration | 5 | 0-2.5 | 2 points: Fix previous signup/login form, new user should send to the database; 2.5 points: Make sure user isn't already in the database, salt and hash password |
| Requirement - Authentication | 5 | 0-2.5 | 2 points: Login/logout user session; 2.5 points: Display data for a given user, all users should have different homepage |
| Requirement - UI | 2.5 | 0-2.5 | 2.5 points: Display difference between user that is captain vs. player for a team, specific buttons should only appear for captain, vise versa |
| Requirement - Events | 7.5 | 0-2.5 | 1 point: Redesign event page; 2 points: Include Google Maps to event details; 2.5 points: Allow for recurrence when creating event |
| Testing | 5 | 0-2.5 | 2.5 points: Add to manual test plan |
| Schedule | 2 | 0-1 | Revised final project schedule if necessary |
| **Total** | **63** | | |

## Week 4

### Requirements

#### Part 1: Event Detail

For each event detail page, there will be more features implemented. It will include a notes section that a player should know about for a specific event. For example, a practice event could include the drills done so if players missed practice, they can still view what the team worked on. In addition, allow attachments (documents, photos, etc.) for an event. These attachments can also be viewed in an attachments page from the team home page.

#### Part 2: User Interface - Captain vs. Player

For each team, a user is either an admin (captain) or a regular player. The pages should display different information between a captain and player. Captains will have access all the editting features whereas players can only see all the profile information and events.

#### Part 3: Settings

Every user should be able to edit their account information. For example, if a user types the wrong name when registering, they should be able to edit it. In addition, if a user forgets their password, they will want to be able to reset it or even if they know it, they should be able to change their password. When the user clicks on their username profile on the navigation bar, it will redirect them to the settings page that will allow the user to make all these changes.

#### Part 4: Announcements

In the case there is information that needs to be sent to the team that isn't related to an event, it will be considered as an announcements. All announcements will be able to be displayed on the homepage. For the more important announcements, they can be pinned to the top.

#### Part 5: Search

A search functionality will be added to the navigation bar that will allow users to easily search for players and events in the teams they are a part of. Instaed of having to click a bunch to get player contact information or event details, the search bar will show the results and once a user clicks on the person or event, it will redirect right to the player profile or event details page.

#### Part 6: Testing

Expand the manual test plan for this week. Write a test plan including screenshots and specific steps for a human tester to follow - what a tester should do and what he/she should observe.

### Grading Rubric

| Category | Weight | Scoring | Requirement |
| --- | --- | --- | --- |
| Basic Preparation | 2 | 0-1 | Ready to go at the start of section |
| Cleverness | 2 | 0-2 | The hardest points on the rubric |
| Rubric | 2 | 0-1 | Submitted a grading rubric |
| Code Submission | 4 | 0-2 | Submitted correct content on time and to the correct location in the repository |
| Decomposition | 4 | 0-2 | Project is adequately decomposed to different classes and methods |
| Documentation | 4 | 0-2 | Comments for each class and each function are clear and are following style guides |
| Effort | 2 | 0-2 | Perform considerable amount of work |
| Naming | 2 | 0-2 | Variable names and method names are readable and are following the naming conventions of the language you chose |
| Overall Design | 5 | 0-2.5 | Have nice approaches and structures in overall |
| Participation | 5 | 0-2.5 | Interact with the group 2 times (ask a question, make a comment, help answer a question, etc.) |
| Presentation | 4 | 0-2 | Present the code clearly |
| Requirement - Users/Events | 5 | 0-2.5 | 2 points: Different user types; 2.5 points: Include a notes section and allow attachments (documents, photos, etc.) |
| Requirement - Settings | 5 | 0-2.5 | 2 points: Allow for users to change account information such as display name, username, email, and password; 2.5 points: Ability to reset password if user forgets it |
| Requirement - Announcements | 5 | 0-2.5 | 2 points: Home page will display announcements for important information; 2.5 points: Posts can be pinned, shown on the top before all other announcements |
| Requirement - Search | 5 | 0-2.5 | 2 points: Ability to search for teams; 2.5 point: Ability to search for players and events in teams |
| Testing | 5 | 0-2.5 | 2.5 points: Add to manual test plan |
| Schedule | 2 | 0-1 | Revised final project schedule if necessary |
| **Total** | **63** | | |


## Sources

### Django Tutorials
- https://pythonprogramming.net/django-web-development-with-python-intro/
- https://docs.djangoproject.com/en/1.11/intro/tutorial01/
- https://docs.djangoproject.com/en/1.11/intro/tutorial07/

### Django Documentation
- https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/
- https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/
- https://docs.djangoproject.com/en/1.11/topics/auth/
- https://docs.djangoproject.com/en/1.11/topics/auth/default/
- https://docs.djangoproject.com/en/1.11/topics/db/queries/
- https://docs.djangoproject.com/en/1.11/ref/validators/
- https://docs.djangoproject.com/en/dev/ref/templates/builtins/

### Bootstrap
- https://v4-alpha.getbootstrap.com/components/navbar/
- https://v4-alpha.getbootstrap.com/components/forms/
- https://v4-alpha.getbootstrap.com/layout/grid/

### Examples
- https://github.com/buckyroberts/Viberr/
- https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK
- https://www.youtube.com/watch?v=Fc2O3_2kax8&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj
