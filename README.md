![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
![CBC Logo](https://canadianbusinesscollege.com/wp-content/uploads/2020/09/CBC-New-Logo-Website.png)

# Food Lovers - Milestone Project - Backend Development

Hello Everyone, 

I welcome you all to my lovely Milestone Project - where I show you the power of Python and Data driven development using the flask framework. This project is an online cookbook web application where fellow food enthusiast can signup, add recipes of their own, and share with the rest of the community.


Check  the link below for a live preview:

👉[Quick Preview](https://python-and-datacentric-project.herokuapp.com/)

 
## UX

### Project Goals
The purpose of the Food Lovers Web Application Project, is to build an online cook book community for people that love food and would like to share that passion with others. 

### User's Goal
The user's goals would be to find list of new inspiring recipe ideas to explore and add their own original recipes that other users may be interested in.

### Site owner's goal 
Get the users more engage in adding and sharing recipe with the rest of the world, leading to further development of the **Food Lovers** website as a community.

### User stories
- As a member of the website, I would like to be able view records of my recipes shared through my profile, so that I can easily update or delete it.
    - I should also have the capability to Add, view, edit and delete my own food categories.
- As a first time visiter of the site, It would be awesome to view a list of all recipes either by category or none.

**Click these links below to access the files**

- [Wireframes](https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/tree/master/static/images/Python-Project-3%20-%20Mockups)

- [Sitemap](https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/sitemap.png)

- [ER Diagram](https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/ERdiagram.png)


## Features

### Existing Features
- Home Page - is a landing page that serves as a brief introduction to what users can expect from the website.
- The Recipe page - allows users to browse through a catalog of different recipes users can choose to cook.
- The Register Page - allows new vsisiters to become part of the Food Lovers community.
- Log In Page - gives users access to the full functionality the website has to offer.
    - Users can add, edit, and delete recipes of their own
    - Profile page - gives users relevant information about their personal account.
    - Log out button - allows for users to safely exit out of their account so that nobody else can access their database.
- Form submissions 
    - CRUD functionalities - provides users with add, read, and delete elements relevant for the recipes.
    - Authentication - protects the privacy of users
- Flask.escape() -  a mechanism for guarding against html injection from users trying to send harmful data through the website

### Features Left to Implement
- Prompting user's about the effects of deleting a food category and updating the list of recipes listed under that specific category.
- Creating a user dashboard to provide some statistics about all the recipes.
- Adding text query search functionality for the list of recipes

## Technologies Used

- [HTML](https://www.w3schools.com/html/default.asp)
    - The project uses **HTML** to produce the web contents elements.

- [CSS](https://www.w3schools.com/CSS/default.asp)
    - The project uses **CSS** to create visually pleasing content.

- [Materialize CSS](https://materializecss.com/)
    - The project uses **Matrialize CSS** version 1, frontend design framework, to produce better UI/UX for mobile first development.

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - The project uses the **Flask**  framework to simplify and speedup, frontend and backend development.

- [MongoDB](https://www.mongodb.com/2)
    - In this project, **MongoDB** is used to manage the database development.

- [Python](https://www.python.org/doc/)
    - The project uses **Python** to process server side functionalities, such as CRUD and form submissions.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation for UI contents.


## Testing

1. Navigation Links:
    1. Clicking on the **logo** redirects to the homepage.
    2. Clicking on **Log in** leads user to log in forms
    3. Selecting **Register** leads users to the register form.
    4. Users are redirected back to log in form when log out is clicked
    5. Clicking **Recipes** redirects to the page with listed recipes.
    6. Clicking on **Add a Recipe**, redirects user to the form for adding a recipe
    8. The selection ofr the **Profile** link redirects to the profile page

2. CRUD functionalities:
    1. Recipe:
        1. Adding a recipe
            1. Goto "Add a Recipe" page
            2. Try to submit empty and verify error message from form
            3. Each form field returns red line color for selected fields that are still empty
            4. Successful form submittion redirects user to "ALl Recipes" page with a feedback message
        2. Read recipe:
            1. Selecting view recipe redirects user to detailed recipe page
        3. Edit recipe:
            1. Only registered user authors have access to edit recipe details
            2. Selecting edit recipe button redirects user to edit page with a form prefilled with relevant values.
            3. Submitting form successfuly redirects user back to the detailed recipe page with relevant feedback message
            4. Form submission with empty fields prompts error message for user
        4. Delete recipe:
            1. Delete buttons can only be accessed by registered user authors
            2. Selecting delete prompts user for confirmation
            3. Upon confirmation, user is redirected back to "Recipes" page with feedback message
    
    2. Recipe Category/Menu:
        1. The above testing sceneratios for recipe also applies here

3. Flask template engine:
    1. Each page renders as it should 
    2. Flask automatically tracks syntax error passed on to HTML template files and displays the location of it

4. Device Responsiveness:
    1. The web application successfuly adjust to different device screen width

5. Cross Browser Test:
    1. Web Application displays the same way on Chrome and Microsoft edge

6. Register form:
    1. Users submitting empty form fields receives error message from the front end.
    2. Form returns feedback message if selected username already exits in the database
    3. Successfull form submission redirects user to the profile page with user feedback.

7. Login form:
    1. Users submitting empty fields are receives error message 
    2. Users submitting the wrong username or password are redirected back to the page with relevant feedcback message
    3. Successfull form submission redirects user to the profile page with user feedback message.

## Deployment

The Food Lovers - Backend Development Project - has been deployed to 👉[Heroku.](https://python-and-datacentric-project.herokuapp.com/)👈

### Deploying To Heroku

1. In order to deploy to heroku, a Github repository was created for the project.
2. Make sure to have downloaded [Git Bash](https://www.atlassian.com/git/tutorials/git-bash)
3. Go to the root folder directory of the app on the local computer.
4. Right click it and select **Git Bash here** to open the CLI terminal.
5. Initialize the project directory by typing ```git init``` in the terminal and pressing the Enter key.
6. Copy the url of the Github repository created for the app.
7. On the terminal, add the url you copied, as a remote with the command 
    ```git remote add origin <paste your github URL here> ```

8. Next, commit all your changes to git with these commands
    ```bash
    git add . 
    git commit -m "Your message here. Example <First commit>"
    ```
9. Create the main branch of your repository with the command ```git branch -M main```
10.  After the steps above,  the project can now be pushed to the repository with the command ```git push```
11. Now the project is ready to be deployed to Heroku.
12. Before deploying our Python App to Heroku, 2 files will need to be created. **Procfile and Requirements.txt**
    1. In the gitbash terminal of the root folder directory of the project. Run these commands to create the procfile and requirements.txt. Note: Make sure you have downloaded and added python to your environment variables.
    ```bash
    pip3 freeze --local > requirements.txt
    touch Procfile
    ```
    2. Make sure the Procfile created has a capital "P" in the title. Open the Procfile in a text editor and add this line of text on the first line ```web: python app.py```. Note: make sure there is not extra line after the first one. Not even an empty line.
    3. Repeat step 8 and 10 of the steps above.
13. After creating an account on Heroku, an app name where the project is hosted will need to be created from the dash board.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/heroku-new.PNG?raw=true" alt="Deploy image">

14. Select the app created.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/appname.PNG?raw=true" alt="Deploy image">

15. Click on the settings tab and then click the **Reveal Config Vars** to add the config variables of the python application.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/settings.PNG?raw=true" alt="Deploy image">

16. The config variables added will be similar to the ```env.py``` file utilized in deploying the application on the local PC, similar to the variables in enclosed in brackets in this [env sample](https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/08-SearchingWithinTheDatabase/01-text_index_searching/env_sample.py)
17. Once the config vars are added, navigate to the **Deploy** tab.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/deploytab.png?raw=true" alt="Deploy image">

18. In the diployment section, select Github for the deployment method and connect to the github repository for the project by searching for its name.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/deploy.png?raw=true" alt="Deploy image">

19. Further down the page you will have to select the automatic deployment and for the manual deploy section, choose main branch and click the ```Deploy Branch``` button.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/viewlive.png?raw=true" alt="Deploy image">

20. The above steps will cause Heroku to process the project files and create a link for you to view the live deployment of the Flask Web Application Project.


## Credits

### Content
- The sample recipes utilized in this web application project were obtained from:
    - [Secret Detox Drink Recipe](https://draxe.com/recipes/secret-detox-drink/)
    - [Meal-Prep Shrimp Taco Bowls](https://gimmedelicious.com/shrimp-taco-meal-prep-bowls/)
    - [VERY BEST LENTIL SOUP](https://downshiftology.com/recipes/very-best-lentil-soup/)
    - [Freezer Breakfast Burritos](https://www.crunchycreamysweet.com/freezer-breakfast-burritos-recipe/)
    - [Grilled Corn Salad](https://www.allrecipes.com/recipe/214934/grilled-corn-salad/#)
    - [Feel Better Chicken Soup Recipe](https://www.feastingathome.com/chicken-soup/)

### Media
- Background image, by Lily Banse, for the home page was obtained from [unsplash](https://unsplash.com/photos/-YHSwy6uqvk)

### Acknowledgements
- In order to build this project successfully, the lessons from Code Institute learning platform was an extremely valuable resource to have.
    - I am expecially thankful for the [Backend Development walkthrough project](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/08-SearchingWithinTheDatabase/01-text_index_searching), led by Tim Nelson, Code Institute instructor.
- My instructor, Usmaan Mujtaba, from the Canadian Business College also played a major role in resolving technical issues encountered through out the project and providing guidance on building a full stack project.

