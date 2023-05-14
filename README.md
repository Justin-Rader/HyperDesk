# HyperDesk

This is a ticketing system built using Django, intended as a first public Python project. The goal of this project is to provide a basic implementation of a ticketing system, with the ability to create, assign, and track tickets, as well as manage users and teams.
Features

### The following features are implemented in this ticketing system:

- Users can create tickets with a title, description, priority, and status.
- Tickets can be assigned to users and teams.
- Users and teams can be assigned to an organization.
- Users can have a profile picture and profile link.
- Tickets can have customer labels.
- Users can have different roles, such as admin, support, or customer.
- Users can be active or inactive, and can be paid or unpaid.

## Getting Started

### To get started with this ticketing system, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running `pip install -r requirements.txt` in your terminal.
3. Set up the database by running `python manage.py migrate`.
4. Create a superuser account by running `python manage.py createsuperuser`.
5. Start the development server by running `python manage.py runserver`.

Once the server is running, you can access the ticketing system by visiting http://localhost:8000 in your web browser.
Code Structure

### The code for this ticketing system is structured as follows:

- The tickets app contains the models, serializers, views, and routers for managing tickets.
- The users app contains the models, serializers, views, and routers for managing users.
- The teams app contains the models, serializers, views, and routers for managing teams.
- The organizations app contains the models, serializers, views, and routers for managing organizations.
- The static directory contains static assets such as CSS and JavaScript files.
- The templates directory contains HTML templates used to render the ticketing system.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository to your own GitHub account.
2. Create a new branch for your changes.
3. Make your changes and commit them with clear commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository with a description of your changes.

# License

*HyperDesk* is licensed under the MIT License. See the LICENSE file for more details.
