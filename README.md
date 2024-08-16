# Face Recognition Based Attendance System

This project is a Python-based attendance system that utilizes face recognition technology to mark attendance. It features an easy-to-use graphical user interface (GUI) built with tkinter.

## Overview

The system captures images and recognizes faces to take attendance. It is designed to be user-friendly and secure, with password protection for new user registration. The attendance data is stored in CSV files, which are updated daily.

## Technologies Used

1. **tkinter**: For creating the GUI.
2. **OpenCV**: For image capture and face recognition using `cv2.face.LBPHFaceRecognizer_create()`.
3. **CSV, Numpy, Pandas, datetime**: For data handling and processing.

## Features

1. **User-Friendly GUI**: An interactive interface that is easy to navigate.
2. **Secure Registration**: Password protection for registering new users.
3. **Automated CSV Management**: Automatically creates and updates CSV files with student details upon registration.
4. **Daily Attendance Records**: Generates a new CSV file each day to record attendance with accurate date and time stamps.
5. **Live Attendance Display**: Shows real-time attendance updates on the main screen in a tabular format, including ID, name, date, and time.