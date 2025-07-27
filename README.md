# HEALTH_MONITORING
"A Django web application providing a Smart Health Card system. Features include secure user authentication (patient/doctor), health record management, current disease and medical history tracking, symptom-based disease prediction using CNN, and personalized health card generation. Built with Python, Django, and TensorFlow/Keras."
# Smart Health Card: A Comprehensive Health Monitoring System

## Overview

The Smart Health Card project is a Django-based web application designed to manage and monitor patient health records, integrating machine learning for disease prediction. It provides a user-friendly interface for both patients and doctors to access, update, and understand health-related information, including current diseases, medical history, and personalized health cards.

## Features

* **User Authentication:** Secure sign-up and login for patients and doctors.
* **Patient Profile Management:** View and update personal health details.
* **Doctor Panel:** Doctors can search for patient details using their Aadhar card number.
* **Disease Tracking:** Record and view current health issues and symptoms.
* **Medical History:** Maintain a comprehensive record of recovered diseases.
* **Disease Prediction:** Utilizes a Convolutional Neural Network (CNN) and other ML algorithms to predict potential diseases based on symptoms.
* **Health Card Generation:** Generate and download a personalized health card (PDF/Image) for quick access to vital health information.
* **Responsive Design:** User-friendly interface built with Bootstrap 4.

## Technologies Used

* **Backend:** Django (Python Web Framework)
* **Frontend:** HTML, CSS (Bootstrap 4)
* **Database:** SQLite3 (default Django)
* **Machine Learning:**
    * TensorFlow / Keras (for CNN model)
    * Scikit-learn (for other ML algorithms)
    * NumPy, Pandas (for data handling)
* **Image Processing/Utilities:** OpenCV-Python, Pillow, CMake, Face-Recognition (if facial features are used for recognition/data).
* **Other Python Libraries:** `requests`, `mysql-connector-python` (if external MySQL is used, though SQLite3 is default).

## Project Structure

HEALTH_MONITORING/
├── CNN_training_testing/
│   ├── pycache/
│   ├── CNN_TESTING.py          # Script for testing CNN model
│   ├── dataset.csv             # Combined dataset for training/testing
│   ├── dm.py                   # Data management/preprocessing script (assumed)
│   ├── Health_Doctor_exercise_diet.csv # Additional health data (assumed)
│   ├── ML_AlGORITHMS.py        # Script for other ML models
│   ├── NN.h5                   # Trained Neural Network model file
│   ├── symptoms_list.py        # Python file containing symptom definitions
│   ├── Testing.csv             # Dataset for testing ML models
│   ├── Training.csv            # Dataset for training ML models
│   └── TRAINING.py             # Script for training ML models
├── todo/                       # Your main Django application
│   ├── _pycache/
│   ├── migrations/             # Database migration files
│   ├── static/                 # Static assets (CSS, images)
│   │   ├── BG2.jpg
│   │   ├── logo.png
│   │   └── style.css           # Centralized CSS stylesheet
│   ├── templates/              # HTML templates for Django views
│   │   ├── base.html           # Base template for common layout
│   │   ├── check_detail.html   # Patient detail search/display
│   │   ├── completedtodos.html # Medical history (recovered diseases)
│   │   ├── createtodo.html     # Add new health issue
│   │   ├── currenttodos.html   # Current diseases list
│   │   ├── doctor_signupuser.html # Doctor registration
│   │   ├── home.html           # Homepage
│   │   ├── loginuser.html      # User login
│   │   ├── predict_disease.html # Disease prediction form
│   │   ├── predicted_result.html # Disease prediction results
│   │   ├── signupuser.html     # Patient registration
│   │   ├── viewtodo.html       # View single health issue detail
│   │   └── your_profile.html   # User's own profile page
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── CNN_TESTING.py          # Copied/used within Django app for prediction
│   ├── forms.py                # Django forms
│   ├── Health_Card.pdf         # Example/generated health card PDF
│   ├── Health_Doctor_exercise_diet.csv # Copied/used within Django app
│   ├── models.py               # Django database models
│   ├── NN.h5                   # Copied/used within Django app for prediction
│   ├── symptoms_list.py        # Copied/used within Django app
│   ├── tests.py
│   ├── Training.csv            # Copied/used within Django app
│   └── views.py                # Django view functions
├── todowoo/                    # Django project configuration
│   ├── pycache/
│   ├── init.py
│   ├── asgi.py
│   ├── setting.py              # Project settings (note: usually 'settings.py')
│   ├── urls.py                 # Project URL configurations
│   └── wsgi.py
├── venv/                       # Python Virtual Environment
├── db.sqlite3                  # SQLite database file
├── Generate_health_card.py     # Script to generate health cards
├── HEALTH_CARD.png             # Example/generated health card image
├── manage.py                   # Django's command-line utility
└── report.pdf                  # Example/generated report PDF (assumed)


## Setup Instructions
Follow these steps to set up and run the Smart Health Card project on your local machine.

### Prerequisites

* **Python 3.6+** (Recommended: Python 3.8 or higher)
* **Git** (Optional, for cloning the repository)
* **VS Code** (or your preferred IDE)

### 1. Download & Install Software
Ensure you have the following installed:

* **VS Code:** [https://code.visualstudio.com/download](https://code.visualstudio.com/download#)
* **Python:** [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. VS Code Extensions (Recommended)
Install these extensions in VS Code for a better development experience:

* **Code Runner**
* **Python**
* **PDF**

### 3. Clone the Repository (if applicable)
If your project is hosted on Git, clone it:

git clone <repository_url>
cd smart_health_card

Otherwise, navigate to your project directory. For example:

### 4. Nevigate Project folder
c\Project\HEALTH_MONITORING

### 5. Create and Activate Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

python -m venv venv
Activate the virtual environment:

Windows:

.\venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

### 6. Install Project Dependencies
With the virtual environment activated, install all required Python packages. If you have a requirements.txt (which is good practice, you can generate it using pip freeze > requirements.txt), use:

pip install -r requirements.txt
If not, install them manually:

pip install --upgrade pip
python.exe -m pip install --upgrade pip
pip install numpy
python -m pip install --upgrade pip
pip install pandas
pip install opencv-python
pip install pillow
pip install cmake
pip install face-recognition
pip install mysql-connector-python
pip install requests
pip install tensorflow
pip install keras
pip install sklearn
pip install django
pip install scikit-learn

### 7. Database Setup
Create and apply database migrations to set up your SQLite database schema.

python manage.py makemigrations todo
python manage.py migrate

### 8. Create a Superuser
Create an administrative user to access the Django admin panel. Follow the prompts to set up your credentials.

python manage.py createsuperuser

http://127.0.0.1:8000/admin

### 9. Run the Development Server
Start the Django development server:

python manage.py runserver

### 10. Access the Application
Open your web browser and navigate to the local server address, typically:

http://127.0.0.1:8000/

You should now see the application homepage!

Usage
For Patients: Sign up, log in, view your profile, add new health issues, and review your medical history.

For Doctors: Log in, access the "Check Detail" page to search for patients by Aadhar number, view their profiles and medical records.

Disease Prediction: Navigate to the "Predict Disease" section to input symptoms and get a potential diagnosis.

Health Card: Download a personalized health card from your profile or the patient's detail page.
