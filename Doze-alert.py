import cv2
import imutils
from imutils import face_utils
import dlib                                         # You need to import dlib for face detection and shape prediction
from scipy.spatial import distance
from pygame import mixer

mixer.init()
mixer.music.load("Assets/music2.mp3")

print(cv2.__version__)

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)

    return ear

thresh = 0.25
flag = 0
(iStart, iEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS['right_eye']

detector = dlib.get_frontal_face_detector() 
predictor = dlib.shape_predictor("models/Face-predictor.dat")
facerecog = cv2.CascadeClassifier("Facebox xml/haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)


while True:
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detector(gray, 0)
    faces=facerecog.detectMultiScale(frame,1.1,7)               # >> Face detection Frame on Face<<
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h+20), (0, 255, 0), 2)

    for subject in subjects:

        shape = predictor(gray, subject)
        shape = face_utils.shape_to_np(shape)
        leftEye = shape[iStart:iEnd]
        rightEye = shape[rStart:rEnd]
        leftEar = eye_aspect_ratio(leftEye)
        rightEar = eye_aspect_ratio(rightEye)
        ear = (leftEar + rightEar) / 2.0
        lefteyehull = cv2.convexHull(leftEye)
        righteyehull = cv2.convexHull(rightEye)

        cv2.drawContours(frame, [lefteyehull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [righteyehull], -1, (0, 255, 0), 1)

        if ear < thresh:
            flag += 1
            print(flag)

            if flag >= 5:
                mixer.music.play(start=0.7)
                cv2.putText(frame, '********* ALERT !!! [ WAKE UP!! ] *********', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
        else:
            flag = 0
            mixer.music.stop()

    cv2.imshow("Doze-alert", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break

cv2.destroyAllWindows()
camera.release()







