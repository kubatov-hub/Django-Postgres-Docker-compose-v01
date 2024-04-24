# Django Boilerplate with Docker Compose, Makefile, and PostgreSQL

This project is a boilerplate for quickly starting new Django projects. It includes Docker Compose settings to run Django in a container, a Makefile for convenient project management, and PostgreSQL as the database.

## Using Makefile

The Makefile includes several useful commands for managing the project:

- Start storage containers: `make storages`
- Stop storage containers: `make storages-down`
- View storage containers' logs: `make storages-logs`
- Start the Django application: `make app`
- View the Django application logs: `make app-logs`
- Stop the Django application: `make app-down`
- Run Django migrations: `make migrate`
- Generate Django migrations: `make migrations`
- Create a Django superuser: `make superuser`
- Collect static files: `make collectstatic`
