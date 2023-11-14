<h1 align="center">Cinema-backend of 4 microservices by Q1nfo</h1>



**Source Code**: [github.com/q1nfo/django-admin](https://github.com/Q1nfo/django-admin)

**1 PART - admin panel in django** : [Django-admin](https://github.com/Q1nfo/django-admin) \
**2 PART - core functionality manager on FastApi** : [Fastapi-movie]() \
**3 PART - service updating data from the database in ElasticSearch** : [Db-to-Elastic]() \
**4 PART - auth service on Flask**: [Flask-auth]()

---

<!--intro-start-->

Cinema project, which consists of 3 microservices interacting with each other via docker-compose

This service is part 1, an admin panel created on the django framework using the convenient and fast postgresql, the project has an API that was specially made without using DRF to show the capabilities of django itself. The admin panel is conveniently configured for further work by managers

To get started, jump to the [installation](#installation) section or keep reading to learn more about the included
features.
<!--intro-end-->

<!--readme-start-->

## ✨ Features

### 📦️ Django technologies

* [Django 3.1](https://www.djangoproject.com/) - Latest version of Django
* [Gunicorn](https://gunicorn.org/) - 'Green Unicorn' is a Python WSGI HTTP Server for UNIX
* [Postgresql](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database
### 🩺 Code Quality, Formatting, and Linting Tools

* [Flake8](https://flake8.pycqa.org/) - Tool For Style Guide Enforcement
* [pre-commit](https://pre-commit.com/) - Git hook scripts are useful for identifying simple issues before submission to code review.
* [isort](https://pycqa.github.io/isort/) - isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.

### Tests

*[Unittest-Django]() - Django's built-in testing tool

    manage.py test movies.tests

## Installation

### Requirements

Before proceeding make sure you have installed [Docker](https://docs.docker.com/engine/installation/) . Docker with Docker Compose is used for local development.

### Manual Installation

    $ gh repo clone Q1nfo/django-admin
    $ mv django-admin example
    $ cd example

    touch .env && touch .env.db

    pip install -r requirements


<!--readme-end-->