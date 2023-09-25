# _TTRPG Hub_

![Image of welcome screen](documentation/images/ttrpg-home-page.png)

---

# Introduction

TTRPG Hub is a blog website desogned to spark engagement and discussion amongst the Tabletop Roleplaying Game (TTRPG) community. Users can comment and like blog posts, but also vote on polls. The link to the live website is [here](https://ttrpg-hub-84db70afcadd.herokuapp.com/).

## Technologies used

- [Python](https://www.python.org/) was one of the main programming languages used to create this project.
- [VScode](https://code.visualstudio.com/) was the editor used to write my code.
- [Javascript](https://www.javascript.com/) was used to make the website more interactive.
- [HTML](https://en.wikipedia.org/wiki/HTML) and [CSS](https://en.wikipedia.org/wiki/CSS) was used to present content to the user on the front end.
- [ChatGPT](https://chat.openai.com/) was used to write the blog posts and come up with the titles.

---

# Design

## Agile Planning

An agile approach was used to plan and make this project. I made use of GitHub's issues and projects to manage my progress in the project, as well as user stories. A link to my kanban board can be found [here](https://github.com/users/Dekeypetey40/projects/3/views/1).
![Kanban board](documentation/images/kanban-board.png)

## User stories

| Title | Number | Definition | Completed? | Label |
|-------|--------|------------|------------|-------|
| USER STORY: Edit and Delete Comments | [#1](https://github.com/Dekeypetey40/TTRPG-Hub/issues/1) | As a user, I want to be able to delete and edit my comments, so that update or remove my comments if I need to. | [x] | Must Have |
| USER STORY: See full blog post | [#2](https://github.com/Dekeypetey40/TTRPG-Hub/issues/2) | As a user, I can click on a blog post title, so that view the entirety of the post. | [x] | Must Have |
| USER STORY: View Comments | [#3](https://github.com/Dekeypetey40/TTRPG-Hub/issues/3) |As a admin or site user, I want to read comments on a blog post, so that I can see what the community thinks about the post. | [x] | Must Have |
| USER STORY: View post likes | [#4](https://github.com/Dekeypetey40/TTRPG-Hub/issues/4) | As a admin or site user, I want to how many likes a post has, so that I can see how popular it is. | [x] | Must Have |
| USER STORY: Moderate Blog Content | [#5](https://github.com/Dekeypetey40/TTRPG-Hub/issues/5) | As an admin, I want to be able to create, edit, update, and delete posts, so that can control the content on the site. | [x] | Must Have |
| USER STORY: Moderate comments | [#6](https://github.com/Dekeypetey40/TTRPG-Hub/issues/6) | As an admin, I want to be able to create, edit, update, and delete comments, so that can control the content on the site. | [x] | Must Have |
| USER STORY: Like Feature | [#7](https://github.com/Dekeypetey40/TTRPG-Hub/issues/7) | As a user, I want to be able to like posts, so that the post author knows I like their content. | [x] | Must Have |
| USER STORY: Comment Like Feature | [#8](https://github.com/Dekeypetey40/TTRPG-Hub/issues/8) | As a user, I can like other user's comments, so that show which comments I like. | [ ] | Could Have |
| USER STORY: Comment Feature | [#9](https://github.com/Dekeypetey40/TTRPG-Hub/issues/9) | As a user, I can comment on blog posts, so that I can interact with the community. | [x] | Must Have |
| USER STORY: Paginated Post Content | [#10](https://github.com/Dekeypetey40/TTRPG-Hub/issues/10) | As a site user, I want to see paginated content, so that I can easily view the content I want without being overwhelmed. | [x] | Should Have |
| USER STORY: Make an Account | [#11](https://github.com/Dekeypetey40/TTRPG-Hub/issues/11) | As a new user, I can easily make an account for the website, so that I can interact with the community. | [x] | Must Have |
| EPIC: Home Page | [#12](https://github.com/Dekeypetey40/TTRPG-Hub/issues/12) |  As a new user, I want to see a home page that makes the site's purpose clear, so that I can quickly determine if I am interested in the site. | [x] | Must Have |
| USER STORY: Add Tag Feature | [#13](https://github.com/Dekeypetey40/TTRPG-Hub/issues/13) | As a user, I want to be able to add tags to my posts and view other posts' tags, so that users can quickly get an idea of what a post is about. | [x] | Should Have |
| USER STORY: About Page | [#14](https://github.com/Dekeypetey40/TTRPG-Hub/issues/14) | As a user, I can read what the blog is all about, so that I can understand the blog's purpose. | [x] | Could Have |
| USER STORY: TTRPG Poll | [#15](https://github.com/Dekeypetey40/TTRPG-Hub/issues/15) | As a user, I can vote for which TTRPG is my favorite, so that I can interact with the community. | [x] | Should Have |
| USER STORY: Write Drafts | [#16](https://github.com/Dekeypetey40/TTRPG-Hub/issues/16) | As an Admin, I can create draft posts, so that I can finish writing a post when I want. | [x] | Should Have |
| USER STORY: One like per user on polls | [#17](https://github.com/Dekeypetey40/TTRPG-Hub/issues/17) | As an admin, I want to users to only be able to vote once on polls, so that my polls' results do not get skewed by individual users. | [x] | Should Have |
| USER STORY: Add CRUD functionality for user comments | [#18](https://github.com/Dekeypetey40/TTRPG-Hub/issues/18) | As a user, I want to be able to edit or delete my comments, so that I can control my own comments. | [x] | Should Have |
---

## Scope

The goal of this project was to make a functioning blog the tabletop roleplaying community can engage with topics pertinent to the community. The baseline for this project was to have full CRUD (Create, Read, Update, and Delete) functionality. One can see this relfected in the user stories and their labels as must have, should have, and could have. It was decided that, at a bare minimum, the blog would have its home page with all of the posts and one would be able to click on each post and leave comments. Then I was trying to decide between having an about page, a polls page, or both. Due to time constraints I decided to implement the polls page only as it would provide more opportunity for users to engage with the community.

## Color

I decided to stick with a basic color scheme. I used black for the navbar and footer and left the body of my pages white. The buttons found throughout the site were simply different shades of blue. I decided most of the color would come from the images on the blog posts, which could really be any color. This is why I stuck with a simple color scheme otherwise as to not make the site feel too busy or chaotic.

## Flow Chart and Wireframes

Wireframe of the homepage
![Homepage](documentation/images/homepage-wireframe.png)
Wireframe of a blog post
![Blogpost](documentation/images/blogpost-wireframe.png)

## Database Models

![Database Models](documentation/images/db-models.png)

# Features

## Navbar

- The bootstrap template had a responsive navbar that turns into a burger menu on smaller screens.
- When you have not logged in it shows register and login options and a logout option when logged in.
- The link that is active is lighter so the user knows where on the webpage they are.
![Navbar logged in](documentation/images/navbar-logged-in.png)
![Navbar logged out](documentation/images/navbar-logged-out.png)
![Navbar small screen](documentation/images/navbar-small-screen.png)
![Navbar extended menu](documentation/images/navbar-menu-extended.png)

## Homepage

- The homepage is simple and paginated.
- It shows three blog posts at a time and immediately lets the user know what the purpose of the site is.
- The blue tag and read more buttons invite the reader to click them.
  - The read more button lets you read the whole blog post.
  - The tag buttons filters blog posts by tag.
- You can see how many likes each blog post has.
![Image of welcome screen](documentation/images/ttrpg-home-page.png)

## Reading a blog post

- Here you can see what a blog post looks like when you click read more.
- At the bottom, you can leave a comment, like the post, and read others' comments.
![Blog post](documentation/images/whole-post-title.png)
![Blog post text](documentation/images/whole-post-text.png)

## Tags

- You can see tags on each blog post, which give the user additional information as to what the post is about.
- Users can click on the tags and get a filtered list of blog posts containing that tag.
![Tags](documentation/images/tag-filter.png)

## Polls

- Here you can look at the list of polls that you can vote on.
- One can only vote once on each poll.
- Once you vote you get to see a piechart with the results of the poll.
![List of polls](documentation/images/list-of-polls.png)
![Poll Results](documentation/images/poll-voted.png)
![Multiple Vote Attempts](documentation/images/poll-voted-again.png)

## Account creation and logging in and out

- There are messages letting the user know if they have successfully signed in or out.
- If a user wants to logout the site asks them if they are sure. 
- Username and password fields are required and prompt the user if they input invalid data. 
![Invalid Username](documentation/images/invalid-username.png)
![Password Required](documentation/images/password-required.png)
![Login](documentation/images/login-form.png)
![List of polls](documentation/images/logout-prompt.png)
![List of polls](documentation/images/navbar-logged-in.png)
![List of polls](documentation/images/navbar-logged-out.png)

## Comment CRUD Functionality for Users

- Comments must be approved by an admin. 
- Users have CRUD functionality on the front end.
- If you are the user who made the comment the Edit and Delete buttons appear allowing you to modify the comment.
- If you are not the user who made the comment and try to access the edit or delete urls you will be prevented from updating that comment.

![comment approval](documentation/images/comment-awaiting-approval.png)
![comment](documentation/images/crud-comments-user.png)
![comment edit](documentation/images/edit-comment.png)
![comment](documentation/images/edited-comment.png)
![comment](documentation/images/confirm-delete.png)
![comment](documentation/images/defensive-programming.png)

---

# Future Features

- Allowing users to make blog posts.
- An about page.
- Comment likes
- Discussions on polls

---

# Testing

All testing and validation information can be found [here](#).
---

# Deployment

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account.
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App.
3. You must enter a unique app name.
4. Select your region.
5. Click Create App .
6. Navigate to the settings tab and then to Config Vars.
7. Click Reveal Config Vars and add PORT, ALLOWED_HOSTS, SECRET_KEY, CLOUDINARY_URL and DATABASE_URL. Temporarily set COLLECTSTATIC to 1.
8. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes.
9. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
10. Scroll to the top of the page and choose the Deploy tab.
11. Select Github as the deployment method.
12. Confirm you want to connect to GitHub.
13. Search for the repository name and click the connect button.
14. Scroll to the bottom of the deploy page and select the preferred deployment type.
15. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.
16. Turn DEBUG mode to false in settings.py before final deployment.

## Database

- The app used ElephantSQL as a free cloud database that uses postgresql.
- One simply makes an account with Elephant SQL, makes a new database and copies the url over to env.py.

---

# Credits

## Python Libraries

- Cloudinary
  - Storage for static files
- AllAuth
  - This librared allowed for a seamless integration for user accounts and their validation on the site.
- crispy-bootstrap5 and crispy-forms
  - This allowed for easy to use forms that are compatible with bootstrap 5 templates
- Django
  - This framework made it fast and relatively easy to make a full-stack website.
- Django-taggit
  - This library allowed for easy implementation of tags for my blog posts. Furthermore, it allows users to filter posts by their tag.
- Bootstrap 5
  - A great css framework to easily style web pages. There is lots of free templates available and they are easy to modify to my needs.
- Django-heroku
  - This library fixed a bug I had where my custom css would not work properly on Heroku.

## Content

- A huge thank you to my mentor Aleksei Konovalov for all of his help throughout this process.
- The method to paginate something compatible with Bootstrap 5 and the current Django was from [ourcodeword](https://ourcodeworld.com/articles/read/1757/how-to-implement-a-paginator-in-a-django-class-based-listview-compatible-with-bootstrap-5)
- My knowledge on how to use django-taggit was gained through the [BugBytes](https://www.youtube.com/watch?v=213swbH8j_o&ab_channel=BugBytes) Youtube channel.
- Flaticon and hero image were taken from [Freepik](https://www.freepik.com/)
- My login/logout form templates were taken from dvrrajashekhar on [freefrontend](https://freefrontend.com/bootstrap-login-forms/#gsc.tab=0)
- Stackoverflow was of huge help at multiple points during the project.
- [Starbootstrap](https://startbootstrap.com/theme/clean-blog) was very helpful in styling my website. I used a couple templates from that website and adapted them to suit my site.
- Code Institue's I think therefore I blog project inspired my own blog website, which I customized to suit my needs.

---
