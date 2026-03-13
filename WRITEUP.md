# Project Writeup

## Overview

This project is a blog web application developed using Flask. It allows authenticated users to create, edit, and view posts. The application also supports image uploads for posts and integrates Microsoft login for authentication.

The project is deployed on Microsoft Azure App Service and uses Azure Blob Storage to store images.

## Technologies Used

* Python
* Flask
* SQLAlchemy
* Flask-Login
* WTForms
* Microsoft Authentication Library (MSAL)
* Azure Blob Storage
* Gunicorn

## Main Features

* User login using username/password
* Microsoft account login
* Create and edit blog posts
* Upload images for posts
* Store images in Azure Blob Storage
* Session management using Flask-Login

## Database

The application uses SQLAlchemy as the ORM. Two main tables are used:

**User**

* Stores user information
* Handles authentication

**Post**

* Stores blog post details
* Linked to the user who created the post

## Authentication

The system supports two authentication methods:

1. **Local Login**

   * User enters username and password
   * Credentials are verified from the database

2. **Microsoft Login**

   * Uses MSAL to authenticate users through Microsoft
   * After successful login, a session is created

## Deployment

The application is deployed on Microsoft Azure App Service. Gunicorn is used as the production server to run the Flask application.

## Conclusion

This project demonstrates how to build a Flask web application with authentication, database integration, and cloud deployment using Azure services.
