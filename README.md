# ```Academia - Campus Repository : Django 📔```

## ```Setup```

This guide provides step-by-step instructions to set up and run the project.

### Prerequisites

1. **Download Python:**
   - Visit the [Python Download Page](https://www.python.org/downloads/) to download the latest version of Python.
   - Follow the installation instructions for your operating system.

2. **Get Pip:**
   - Pip usually comes bundled with Python installations after version 3.4. If you need to install or upgrade it, follow the instructions on the [Pip Installation Guide](https://pip.pypa.io/en/stable/installation/).

### Project Setup

3. **Install Django:**
   - Open a terminal or command prompt.
   - Run the following command to install Django:
     ```bash
     pip install django
     ```

4. **Install SMTPMail and MIME:**
   - Run the following commands to install the required packages:
     ```bash
     pip install smtpmail
     pip install mime
     ```

5. **Set Absolute URLs for Images:**
   - Open `login/views.py` and `teacherhome/views.py`.
   - Locate the URL for `textLogo.png` in both files.
   - Replace the relative URL with an absolute URL. Example:
     ```python
     # Before
     img_url = 'textLogo.png'

     # After (replace 'D:/path/to/the/image' with your actual base URL)
     img_url = 'D:/path/to/the/image'
     ```

### Database Setup

6. **Run Migrations:**
   - In the root directory of your project, run the following commands to set up the database:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

### Run the Project

7. **Start the Development Server:**
   - Run the following command to start the development server:
     ```bash
     python manage.py runserver
     ```
   - Visit `http://localhost:8000/` in your web browser to view the project.
