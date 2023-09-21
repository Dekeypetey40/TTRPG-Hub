# _TTRPG Hub_ 


![Image of welcome screen](static/images/ttrpg-home-page.png)

---
# Introduction
TTRPG Hub is a blog website desogned to spark engagement and discussion amongst the Tabletop Roleplaying Game (TTRPG) community. Users can comment and like blog posts, but also vote on polls. The link to the live website is [here] (https://ttrpg-hub-84db70afcadd.herokuapp.com/). 
## Technologies used
- [Python](https://www.python.org/) was one of the main programming languages used to create this project.
- [VScode](https://code.visualstudio.com/) was the editor used to write my code.
- [Javascript] (https://www.javascript.com/) was used to make the website more interactive.
- [HTML] (https://en.wikipedia.org/wiki/HTML) and [CSS] (https://en.wikipedia.org/wiki/CSS) was used to present content to the user on the front end.

---

## User stories

---

# Design 


## Planning

### Flow Chart


# Features


---

# Future Features

---

# Testing

## Validator testing

* Code Institutes [python linter](http://pep8ci.herokuapp.com/) was used to validate the code:
    - Some trailing and missing whitespaces were addressed, but there were no major issues. 
    - Somehow my fixes were not reflected in my last commit so the code was fixed an additional time to pass PEP8 standards.
    - Fixes were also made for the ASCII art python file.
![CI Python Linter](assets/images/run-linter-2.png)
![CI Python Linter](assets/images/ascii-linter-2.png)
* Lighthouse in Chrome Developer Tools was used.
![Lighthouse](assets/images/lighthouse-hangman.png)


---

## Bugs

## Solved bugs

---

## Unsolved bugs

## Manual Testing

| feature | action | expected result | tested | passed | comments |
| --- | --- | --- | --- | --- | --- |

---

# Deployment

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account.
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App.
3. You must enter a unique app name.
4. Select your region.
5. Click Create App .
6. Navigate to the settings tab and then to Config Vars.
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button.
8. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes.
9. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
10. Scroll to the top of the page and choose the Deploy tab.
11. Select Github as the deployment method.
12. Confirm you want to connect to GitHub.
13. Search for the repository name and click the connect button.
14. Scroll to the bottom of the deploy page and select the preferred deployment type.
15. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.

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
- The method to paginate something compatible with Bootstrap 5 and the current Django was from https://ourcodeworld.com/articles/read/1757/how-to-implement-a-paginator-in-a-django-class-based-listview-compatible-with-bootstrap-5 
- My knowledge on how to use django-taggit was gained through the [BugBytes] (https://www.youtube.com/watch?v=213swbH8j_o&ab_channel=BugBytes) Youtube channel.
- Flaticon and hero image were taken from [Freepik] (https://www.freepik.com/)
- My login/logout form templates were taken from dvrrajashekhar on [freefrontend] (https://freefrontend.com/bootstrap-login-forms/#gsc.tab=0)


---

