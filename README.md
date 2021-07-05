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

```
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.
```


## Features
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

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

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

The Food Lovers - Backend Development Project - has been deployed to 👉[Heroku.](https://python-and-datacentric-project.herokuapp.com/)👈

### Deploying To Heroku

1. In order to deploy to heroku, a Github repository was created for the project.
2. Make sure to have downloaded [Git Bash](https://www.atlassian.com/git/tutorials/git-bash)
3. Go to the root folder directory of the app on the local computer.
4. Right click it and select **Git Bash here** to open the CLI terminal.
5. Initialize the project directory by typing ```git init``` in the terminal and pressing the Enter key.
6. Copy the url of the Github repository created for the app.
7. On the terminal, add the url you copided, as a remote with the command 
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

