<div align="center">
  <h1> 30 Days Of Python: Day 2 - Variables, Builtin Functions</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/abdeldjalil-benaifa-87b6a6132/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
 

<sub>Author:
<a href="https://www.linkedin.com/in/abdeldjalil-benaifa-87b6a6132/" target="_blank">Abdeldjalil Benaifa</a><br>
<small> First Edition: September, 2026</small>
</sub>

</div>


[<< Day 22](../22_Day_Web_scraping/22_web_scraping.md) | [Day 24 >>](../24_Day_Statistics/24_statistics.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 23](#-day-23)
  - [Setting up Virtual Environments](#setting-up-virtual-environments)
  - [💻 Exercises: Day 23](#-exercises-day-23)

# 📘 Day 23

## Setting up Virtual Environments

To start with project, it would be better to have a virtual environment. Virtual environment can help us to create an isolated or separate environment. This will help us to avoid conflicts in dependencies across projects. If you write pip freeze on your terminal you will see all the installed packages on your computer. If we use virtualenv, we will access only packages which are specific for that project. Open your terminal and install virtualenv

```sh
PS C:\Users\user\Downloads\Github\30-Days-Of-Python\30-Days-Of-Python>  pip install virtualenv
```

Inside the 30DaysOfPython folder create a flask_project folder.

After installing the virtualenv package go to your project folder and create a virtual env by writing:


For Windows:
```sh
PS C:\Users\user\Downloads\Github\30-Days-Of-Python\30-Days-Of-Python>  python -m venv venv
```

I prefer to call the new project venv, but feel free to name it differently. Let us check if the the venv was created by using ls (or dir for windows command prompt) command.

```sh
PS C:\Users\user\Downloads\Github\30-Days-Of-Python\30-Days-Of-Python>  ls
venv/
```

Let us activate the virtual environment by writing the following command at our project folder.


```
Activation of the virtual environment in Windows may very on Windows Power shell and git bash. 

For Windows Power Shell:
```sh
PS C:\Users\user\Downloads\Github\30-Days-Of-Python\30-Days-Of-Python> .\venv\Scripts\activate  
```

For Windows Git bash:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

After you write the activation command, your project directory will start with venv. See the example below.

```sh
(venv) PS C:\Users\user\Downloads\Github\30-Days-Of-Python\30-Days-Of-Python> 
```

Now, lets check the available packages in this project by writing pip freeze. You will not see any packages.

We are going to do a small flask project so let us install flask package to this project.

```sh
(venv) PS C:\Users\user\Downloads\Github\30-Days-Of-Python\30-Days-Of-Python>  pip install Flask
```

Now, let us write pip freeze to see a list of installed packages in the project:

```sh
(venv) PS C:\Users\user\Downloads\Github\30-Days-Of-Python\30-Days-Of-Python>  pip freeze
beautifulsoup4==4.15.0
certifi==2026.7.22
charset-normalizer==3.5.1
idna==3.20
numpy==2.5.3
pandas==3.0.6
pyarrow==25.0.1
python-dateutil==2.9.0.post0
python-dotenv==1.2.3
requests==2.34.2
six==1.17.0
soupsieve==2.10
typing_extensions==4.16.0
tzdata==2026.4
urllib3==2.8.0
```

When you finish you should dactivate active project using _deactivate_.

```sh
(PS C:\Users\user\Downloads\Github\30-Days-Of-Python\30-Days-Of-Python>  deactivate
```

The necessary modules to work with flask are installed. Now, your project directory is ready for a flask project. You should include the venv to your .gitignore file not to push it to github.

## 💻 Exercises: Day 23

1. Create a project directory with a virtual environment based on the example given above.

🎉 CONGRATULATIONS ! 🎉

[<< Day 22](../22_Day_Web_scraping/22_web_scraping.md) | [Day 24 >>](../24_Day_Statistics/24_statistics.md)
