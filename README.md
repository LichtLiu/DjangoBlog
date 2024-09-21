# DjangoBlog

# Demo 
## Home Page

<img height="300" alt="Screen Shot 2024-09-21 at 4 10 27 PM" src="https://github.com/user-attachments/assets/88fe02d7-b616-4e69-aff3-6d5e18d432d0">
<img height="300" alt="Screen Shot 2024-09-21 at 4 10 43 PM" src="https://github.com/user-attachments/assets/4e5c82d4-a8fc-4943-ae26-e9adadeaf34d">

## Article

<img height="280" alt="Screen Shot 2024-09-21 at 4 13 10 PM" src="https://github.com/user-attachments/assets/61f34883-abb8-48a4-affc-a93c615ff696">
<img height="280" alt="Screen Shot 2024-09-21 at 4 13 36 PM" src="https://github.com/user-attachments/assets/e9ab5a87-e66f-4259-a301-0ce6106bcda7">

## Signin & Signup
<img height="300" alt="Screen Shot 2024-09-21 at 4 14 21 PM" src="https://github.com/user-attachments/assets/f30c9f98-d64d-4bf6-9af3-c090afcb32f9">
<img height="300" alt="Screen Shot 2024-09-21 at 4 17 48 PM" src="https://github.com/user-attachments/assets/68c1652e-aad8-4731-9a6b-51b1fac2a004">


# How to Run this Django Project

This guide will help you set up and run the Django project on your local machine. The repository already contains a `requirements.txt` file and an `env` file, making the setup process straightforward.

## Prerequisites

Before starting, ensure you have the following installed on your system:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)


## Setup Instructions

### 1. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/LichtLiu/DjangoBlog.git
cd DjangoBlog
```

### 2. Set Up a Virtual Environment

Even though the project includes an `env` file, you should create a new virtual environment to ensure everything works correctly:

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Project Dependencies

With the virtual environment activated, install the project dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

The repository includes an `.env` file with necessary environment variables. Make sure the `.env` file is correctly configured. You can check the file or add any additional environment variables needed for your local setup.

### 5. Set Up the Database

Run the following commands to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)

To access the Django admin interface, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username, email, and password.

### 7. Collect Static Files

Collect static files so that they can be served by the server:

```bash
python manage.py collectstatic
```

### 8. Run the Development Server

Now, you can run the development server to see the project in action:

```bash
python manage.py runserver
```

Open your web browser and navigate to `http://127.0.0.1:8000/` to view the project.

### 9. Access the Admin Interface

If you created a superuser, you can access the Django admin interface at `http://127.0.0.1:8000/admin/`.

## Additional Notes

- **Deactivating the Virtual Environment**: When you finish working, you can deactivate the virtual environment by running `deactivate` in your terminal.
- **Managing Environment Variables**: Ensure that the `.env` file is properly configured for your environment.
- **Static and Media Files**: For production, ensure that your web server is configured to serve static and media files correctly.

## Troubleshooting

- **Virtual Environment Issues**: If you encounter issues with the virtual environment, try deleting the `env` directory and creating it again.
- **Database Errors**: Ensure that the database settings in `settings.py` match your local database configuration.

By following these steps, you should be able to set up and run the Django project on your local machine successfully. If you encounter any issues, please check the troubleshooting section or reach out for further assistance.

