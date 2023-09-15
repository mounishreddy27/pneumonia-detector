
# Pneumonia Detector

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)


## Introduction

The Pneumonia Detector Web Application is a Django-based platform that allows users to upload chest X-ray images for pneumonia detection. It offers a user-friendly interface for image submission and provides real-time results. This README.md file provides an overview of the application and instructions for usage.

## Features

- User registration and login.
- Image upload functionality.
- Pneumonia detection using a pre-trained machine learning model.
- Display of uploaded image and detection results.
- User-friendly and responsive web interface.



## Installation

To run the application locally, perform the following steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/pneumonia-detector.git
   ```

2. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the application in your web browser at `http://localhost:8000/`.

## Usage

1. Register a new user account or log in if you already have one.

2. On the home page, select an X-ray image using the file upload button.

3. Click the "Upload" button to initiate pneumonia detection.

4. You will be redirected to the results page, where you can view the uploaded image and the detection result.
