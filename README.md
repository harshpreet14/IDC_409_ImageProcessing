<h1 style="color:#FF69B4">📌 Face Recognition Attendance System</h1>


## Overview

This project implements a face recognition-based attendance system using Python libraries. The system captures video from a webcam, recognizes faces, and updates attendance information in a csv file. 
## Table of Contents
1. [Setting up the Development Environment](#setting-up-the-development-environment)
2. [Collecting Training Data](#collecting-training-data)
3. [Preprocessing and Training the Face Recognition Model](#preprocessing-and-training-the-face-recognition-model)
4. [Implementing the Attendance System](#implementing-the-attendance-system)
5. [Challenges Faced by Face Recognition System](#challenges-faced-by-face-recognition-system)

---

## Setting up the Development Environment
<a name="setting-up-the-development-environment"></a>

1. Visit the [official Python website](https://www.python.org/downloads/release) to download the Python version 3.6.8 on your local system.
2. Download C++ Desktop development tools [here](https://code.visualstudio.com/docs/languages/cpp).
3. Create a empty folder and run the following command in the terminal
   ```git clone https://github.com/harshpreet14/IDC_409_ImageProcessing.git```
5. Next, run ```pip install -r requirements.txt```

   
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
# Importing the student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds =[]
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
```

2. **Find Encodings for Images**
```python
def findEncodings(imagesList):
    encodeList=[]
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
```
3.**Save Encodings as pickle file**
```python
file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
```

## Implementing the Attendance System
<a name="implementing-the-attendance-system"></a>

Now that we have trained our face recognition model, we can proceed to implement the attendance system. The system will follow these steps: 
1. **Capture a live video stream using OpenCV**
```python
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
```

2. **Detect faces in each frame using the face_recognition library**
```while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
```
3. **Compute face embeddings for the detected faces**
```python
encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
```
4. **Compare the computed embeddings with the embeddings of known individuals**
```python
if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print("matches", matches)
            # print("faceDis", faceDis)

            matchIndex = np.argmin(faceDis)
            # print("Match Index", matchIndex)

            if matches[matchIndex]:
                # print("Known Face Detected")
                # print(studentIds[matchIndex])
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                student_id = studentIds[matchIndex]
```

7. **If a match is found, mark the attendance for that person**
```python
 # Save updated data back to CSV
                        with open("students.csv", 'a') as csvfile:
                            fieldnames = ['id', 'last_attendance_time', 'total_attendance']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            writer.writerow(studentInfo)
```

## Challenges Faced by Face Recognition System
<a name="challenges-faced-by-face-recognition-system"></a>

📍Illumination: It changes the face’s appearance drastically. It is observed that even slight changes in lighting conditions cause a significant impact on its results.<br>
📍Pose: Facial Recognition systems are highly sensitive to the pose, Which may result in faulty recognition or no recognition if the database is only trained on frontal face view.<br>
📍Facial Expressions: Different expressions of the same individual are another significant factor that needs to be taken into account. Modern Recognizers can easily deal with it, though.<br>
📍Low Resolution: The recognizer must be trained on a good-resolution picture. Otherwise, the model will fail to extract features.<br>
📍Aging: With increasing age, the human face features shape, lines, and texture changes which are yet another challenge.

