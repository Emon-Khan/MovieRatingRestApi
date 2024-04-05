
# Movie Rating RESTAPI

### Language- Python, Flask
### Database- MySQL
## Setup Instruction
You can name your virtual environment as you wish, but I would recommend naming it 'MovieEnv'. I've added 'MovieEnv' to my .gitignore file to prevent environment files from being pushed to the remote repository.
Step-1: Creating & activating venv Windows:
```
python -m venv env
./env/Scripts/activate
```
For Linux:
```
python -m venv env
source env/bin/activate
```
Step-2: Installing Dependencies
```
  pip install -r requirements.txt
```
Step-3: Running application Windows:
```
  > $env:PYTHONDONTWRITEBYTECODE=1;$env:FLASK_APP="app";$env:FLASK_ENV = "development"
  > flask run --debug
```
For Linux:
```
  > export PYTHONDONTWRITEBYTECODE=1 FLASK_APP="app" FLASK_ENV="development"
  > flask run 
```
## Common Issues
1. Run this cli command it will disable creating new pycache files
```
  $env:PYTHONDONTWRITEBYTECODE=1
```

For Linux:
```
export PYTHONDONTWRITEBYTECODE=1
```

## Common Errors
1. While activating venv this error occures in Windows:
```
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
Solution:

```
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
## How much of the problem you were able to solve
Four

## Problems faced with incomplete parts (if any)
User search up a specific movie and see it’s details along with the average rating of a movie
## Demo
In this section i will show you some of my project's features.

### Login and Add User
If the user is not logged in then at first he need to login.If the user has already been added then he will give his credentials and login.Otherwise need to add the user.
Add User
In the given user json file it is given with id, but as i follow the standard rule.I make the user id as primary key set it to not null also make it auto increment.So, every time a new user added he get a new user id.It don't get conflict with the existing id.
User Table
![image](https://github.com/igorkosandyak/demo-config-server/assets/42010220/b9b89f1f-ac5c-453d-a566-1ec2a2e637d3)

User Created Successfully
![image](https://github.com/igorkosandyak/demo-config-server/assets/42010220/5adc8f26-245b-432b-b3f4-ec78b425553f)

After insertion User Table
![image](https://github.com/igorkosandyak/demo-config-server/assets/42010220/367f4dae-9985-42f2-a480-21260009d311)

Using this user credential let's login
![image](https://github.com/igorkosandyak/demo-config-server/assets/42010220/200e14f7-55b9-4f9e-8fff-82a20207ad76)
After Successfully logged in we have given a access token.Now using this access token we can do many opertion.Like update, delete user, add movie, add rating for a particular movie.
Get By id
![image](https://github.com/igorkosandyak/demo-config-server/assets/42010220/11440d99-528b-4118-a82a-f3f8d895773f)
This endpoint is also protected by the authenticaton.
That's why we have to provide access token which we got from the body section when we Successfully able to login.
Add movie
![image](https://github.com/igorkosandyak/demo-config-server/assets/42010220/9730de5a-a485-408a-a062-5e8e7e721385)
For adding movie we need to at first logged in then we will be able to add a movie.As we are already logged in so that we can add a movie by our previously generated access token.
After adding movie our movie table inside database looked like this
![image](https://github.com/igorkosandyak/demo-config-server/assets/42010220/d2c2dd41-81c0-45a0-93b9-3417d65f5964)

Add Rating for movies
So, in here we need to make sure that the user_id and movie_id we are giving inside the rating json data are matched with user and movie table's id.
![image](https://github.com/igorkosandyak/demo-config-server/assets/42010220/751cccc3-a2fc-4c06-bb5f-ad6d80948e55)
After adding rating for movies let's take a look inside our database table
![image](https://github.com/igorkosandyak/demo-config-server/assets/42010220/95bf72c8-f064-4012-aef4-a67b65c8220f)






