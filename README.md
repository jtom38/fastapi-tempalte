# fastapi-template

## Replacement Values

* APPNAME
* APPDESCRIPTION

## Recommended Pip Packages

Here are some packages that are recommended for working with this template.

* FastApi
* FastApi-sqlalchemey
* alembic

## Folders

### api

This folder is where all the FastApi components should live.

* routes
* events
* startup

### database

This folder contains your database migrations, models and any extra services you might need.

### infra

This is where your base classes, interfaces (domain), enum and model.  The objects here should not have a lot of dependencies
