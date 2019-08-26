# Feedback Collection System

## Overview

This is a minimilistic web application that provides the user to provide feedback.

## Features

1. Submit feedback
2. View all feedbacks

## Stack

1. Python Tornado as Web server and framework (Python 3.7, Tornado latest)
2. VueJS for frontend scripting (VueJS latest)
3. MySQL as database service (MySQL 5.7)
4. Minio for log backups (Minio latest)

## How to run the application
If you are using docker, it becomes really simple to bring up the application and its required components.

```
git clone 
cd feedback-app/
docker-compose up
```

## How to view the application
* For application, Open the browser by pointing to `http://localhost:8888`
* For `Minio`, Open the browser by pointing to `http://localhost:9000`. Creds from docker-compose file can be used for logging in.

## Warning
1. `MySQL` & `Minio` credentials are stored in the `docker-compose.yml`
2. Log settings can be configured in `settings.py`

## Future Work
1. Credentials can be moved and passed in as environment variables to the `docker-compose.yml` file
2. Optimize the frontend to be a `SPA(Single Page Application)` by using client routing (`Vue Router`)
3. For tornado webapp, use a config file and parse options from config file rather than `settings.py`


