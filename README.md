# 📌 Face Recognition Attendance System 

## Overview

This project implements a face recognition-based attendance system using Python libraries. The system captures video from a webcam, recognizes faces, and updates attendance information in a csv file. 
## Project Files

1. **Main Code File: `main.py`**
   - This file contains the main implementation of the face recognition system.
   - It utilizes OpenCV, face_recognition, cvzone, cmake, and dlib libraries.

2. **Encoding Generator File: `EncodeGenerator.py`**
   - 🚀 This script generates face encodings for known student images and saves them in a pickle file.
   
## Requirements

- Python 3.6.x
- opencv-python
- face_recognition
- cvzone
- cmake
- csv

## Usage

1. **Capture Student Images**
   - 📸 Place student images in the `Images` folder.

3. **Run `EncodeGenerator.py`**
   - 🚀 Execute this script to generate and save face encodings for known students.

4. **Run `main.py`**
   - ▶️ Run the main script to initiate the face recognition system.

## Project Structure

- **Resources Folder:**
  - Contains background images and mode images used in the application.

- **Images Folder:**
  - Holds student images used for face recognition.

- **EncodeFile.p:**
  - 📦 Pickle file containing face encodings and corresponding student IDs.

## Notes
- 🛠️ Adjust paths and configurations in the code according to your project structure.

Feel free to customize the code and adapt it to your specific requirements! 🚀
