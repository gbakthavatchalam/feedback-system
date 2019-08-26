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
git clone https://github.com/gbakthavatchalam/feedback-system.git
cd feedback-system/
docker-compose up
```

## How to view the application
* For application, Open the browser by pointing to `http://localhost:8888`
* For `Minio`, Open the browser by pointing to `http://localhost:9000`. Creds from docker-compose file can be used for logging in.

## Frontend Endpoints
```
"/" GET Lets you to submit feedback
"/list" GET Lets you to view all feedbacks
```

## Backend APIs
```
"/api/feedback" GET - Gets list of all feedbacks
"/api/feedback" POST - Saves the feedback
```

## Warning
1. `MySQL` & `Minio` credentials are stored in the `docker-compose.yml`
2. Bucket names for `Minio` can be configurated in `settings.py`
2. Log settings can be configured in `settings.py`

## Future Work
1. Credentials can be moved and passed in as environment variables to the `docker-compose.yml` file
2. Optimize the frontend to be a `SPA(Single Page Application)` by using client routing (`Vue Router`)
3. For tornado webapp, use a config file and parse options from config file rather than `settings.py`

## Log Extraction
1. In backend, logs are backed up in 2 different ways.
2. One is by implementing a custom `TimedRotatingFileHandler` which saves the log file to `Minio` before it tries to clean up the old files.
3. Other way, we are storing metadata related to individual requests as JSON files in a separate bucket on `Minio`

