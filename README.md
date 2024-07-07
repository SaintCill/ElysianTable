# Elysian Table

Elysian Table is a Django-based web application developed as a school project for simulating a fake restaurant management system.

## Description

Elysian Table allows users to interact with a restaurant management interface where they can perform various tasks related to managing a restaurant. This includes:

- Handling reservations
- Managing customer information
- Managing contact requests

## Features

- **Reservation System:** Allows customers to make reservations and provides tools for staff to manage reservations.
- **Static Files Handling:** Integration with Django's static files management for CSS, JavaScript, and image assets.
- **Deployment Readiness:** Configured for deployment on platforms like Render.

## Technologies Used

- **Django:** Python web framework used for backend development.
- **HTML/CSS/JavaScript:** Frontend development technologies.
- **PostgreSQL:** Database management system used for storing application data.
- **Render:** Deployment platform used for hosting the application.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/elysian-table.git
   cd elysian-table

2. Install dependencies using Poetry (assuming you're using Poetry for dependency management):

    ```bash
    poetry install

3. Apply database migrations:
    ```bash
    python manage.py migrate

4. Create a superuser to access the admin interface:
    ```bash
    python manage.py createsuperuser

5. Start the development server:
    ```bash
    python manage.py runserver

Open your browser and navigate to http://localhost:8000 to view the application.

## Future features:
- Menu: Being able to add, remove and tweak menu items. I was going to add this feature along with the contact form, but ran into real life issues, so i might add it at a later date.
  Not the most important thing in the world since fine dinning establishments seldom change their menues, but this may be a Sweden thing. Regardless, i would add it just to have done
  it once, incase i need to do it in future projects.
- Login: Mostly for "staff", as a customer would have little reason to want to login to a fine dinning restaurants website, besides creating reservations straight in the system.
- Email: Sending confirmation email for the reservation. I have the code ready, but didn't have time to set up with the email service. I also have a half way done way to answer emails
  directly from the django admin menu, as one would want if you were working as staff and had to answer emails.

## Deployment
The project is configured to be deployed on platforms like Render. Ensure to set up environment variables and adjust settings as per deployment requirements.

### Render live deployment:
https://elysiantable.onrender.com


## License
This project is licensed under the MIT License.
