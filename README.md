# ```Academia - Campus Repository : Django 📔```

## ```Description```
Academia is a Django-based Campus Repository designed to streamline the file-sharing process between teachers and students. The platform offers distinct homepages for both teachers and students, each tailored to their specific needs. Teachers can efficiently manage files, set permissions, and maintain control over their uploads. On the other hand, students gain easy access to educational resources and a seamless file search experience.

## ```Features```

### Teacher Homepage

- **Upload Files:**
  Teachers can upload files directly to the repository, making educational materials easily accessible to students. 📤

- **Delete Files:**
  Teachers have the capability to remove files, ensuring content relevance and organization within the repository. 🗑️

- **Set Permission Access:**
  Control file access by setting permission levels. Teachers can manage who can view and download their uploaded files. 🔒

- **File Filtering:**
  Teachers can view only the files they have uploaded, creating a personalized and organized experience. 📂

### Student Homepage

- **View All Files:**
  Students have access to a comprehensive list of all files uploaded by teachers, facilitating easy discovery of educational resources. 👀

- **Download Files:**
  Students can download files uploaded by teachers, enabling offline access to course materials. 📥

- **Search Functionality:**
  An efficient search feature allows students to find files by their names, making it simple to locate specific educational resources. 🔍

## ```Tech Stack```

- **Django:**
  The web application is built using the Django framework, providing a robust and scalable foundation for campus repository management. 🐍

- **Python:**
  The backend logic and functionality are implemented using Python, ensuring a clean and efficient codebase. 🐍

- **SQLite Database:**
  The project utilizes SQLite for database management, offering a lightweight and easily deployable solution. 🗃️

- **HTML/CSS/JavaScript:**
  The frontend is designed using a combination of HTML, CSS, and JavaScript to create a user-friendly and responsive interface. 🌐

- **Bootstrap:**
  Bootstrap is employed for styling and layout, ensuring a modern and consistent design across the application. 🎨

## ```Setup```

Step-by-step instructions to set up and run the project.

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

     # After
     img_url = 'D:/path/to/the/image'
     ```

6. **Change Gmail and Password**
   - Open `login/views.py` and `teacherhome/views.py`.
   - Locate the URL for `MAIL_ID` and `PASSWORD` in both files.
   - Change the password and email to your desired one. Refer here : [Steps to Create App Password : Google](https://support.google.com/accounts/answer/185833?hl=en) 


     ```python
     MAIL_ID = "ENTER_YOUR_GMAIL"
     PASSWORD = "xxxx xxxx xxxx xxxx"
     ```
### Database Setup

7. **Run Migrations:**
   - In the root directory of your project, run the following commands to set up the database:

     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

### Run the Project

8. **Start the Development Server:**
   - Run the following command to start the development server:

     ```bash
     python manage.py runserver
     ```
   - Visit `http://localhost:8000/` in your web browser to view the project.


## ```Getting Started```

To set up and run Academia locally, follow the instructions in the [Project Setup Guide](#) provided in the repository.

## ```Contributing```

Contributions are welcome! Please refer to the [Contribution Guidelines](CONTRIBUTING.md) for details on how to contribute to this project. 🤝

## ```License```

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license. 📄
