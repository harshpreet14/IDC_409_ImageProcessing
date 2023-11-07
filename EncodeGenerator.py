import cv2
import face_recognition
import pickle
import os

# Importing the student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds =[]
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
# print(len(imgModeList))


def findEncodings(imagesList):
    encodeList=[]
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Completed...")

file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")