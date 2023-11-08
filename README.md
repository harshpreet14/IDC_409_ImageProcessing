# 📌 Face Recognition Attendance System 

## Overview

This project implements a face recognition-based attendance system using Python libraries. The system captures video from a webcam, recognizes faces, and updates attendance information in a csv file. 
## Table of Contents
1. [Setting up the Development Environment](#setting-up-the-development-environment)
2. [Collecting Training Data](#collecting-training-data)
3. [Preprocessing and Training the Face Recognition Model](#preprocessing-and-training-the-face-recognition-model)
4. [Implementing the Attendance System](#implementing-the-attendance-system)

---

## Setting up the Development Environment
<a name="setting-up-the-development-environment"></a>

1. Visit the [official Python website](https://www.python.org/downloads/release) to download the Python version 3.6.8 on your local system.
2. Download C++ Desktop development tools [here](https://code.visualstudio.com/docs/languages/cpp).
3. Create a empty folder and run the following command in the terminal ```python git clone https://github.com/harshpreet14/IDC_409_ImageProcessing.git```
5. Next, run ```python pip install -r requirements.txt```

   
To build our face recognition attendance system, we will need the following Python libraries:<br>

📍*OpenCV*: For computer vision tasks such as face detection and image processing.<br>

📍*Dlib*: A powerful library that provides facial landmark detection and face alignment capabilities.<br>

📍*face_recognition*: A Python library built on top of dlib, designed specifically for face recognition tasks.<br>

📍*Pandas*: For managing and analyzing the attendance data.


## Collecting Training Data
<a name="collecting-training-data"></a>

Before training the face recognition model, we need a dataset of labeled images representing different individuals. Start by gathering images of each person to be recognized. 
Store the images in ```Images``` folder in root directory.

## Preprocessing and Training the Face Recognition Model
<a name="preprocessing-and-training-the-face-recognition-model"></a>

To train the face recognition model, we will use a popular pre-trained model called "dlib_face_recognition_resnet_model_v1." This model provides a 128-dimensional face embedding for each face detected in an image.

1. **Load images**
After importing libraries you need to load an image. By default, face_recognition library loads images in the form of BGR, in order to print the image you should convert it into RGB using OpenCV.
```python
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
```

## Implementing the Attendance System
<a name="implementing-the-attendance-system"></a>

Now that we have trained our face recognition model, we can proceed to implement the attendance system. The system will follow these steps: 
1. Capture a live video stream using OpenCV.
2. Detect faces in each frame using the face_recognition library.
3. Compute face embeddings for the detected faces.
4. Compare the computed embeddings with the embeddings of known individuals.
5. If a match is found, mark the attendance for that person.

