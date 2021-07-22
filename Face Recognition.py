import cv2, face_recognition, time

video_capture = cv2.VideoCapture(0)

start=False
proccess_this_frame=True
name_face=False

face_locations=[]
good_face_encodings=[]

face_photo = face_recognition.load_image_file(r"C:\Users\spear\OneDrive\Desktop\Desktop Folder\Face_photo.jpg")
good_face_encodings.append(face_recognition.face_encodings(face_photo)[0]
)

while True:
    ret, frame = video_capture.read()

    if start:
        small_frame=cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        if name_face:
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            for i in face_encodings:
                matches = face_recognition.compare_faces(good_face_encodings, i)
            face_name="Unknown"
            if matches is not None:
                if True in matches:
                    face_name="Sam"
        for (top, right, bottom, left) in face_locations:
            top *= 4
            right *= 4
            left *= 4
            bottom *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        if name_face:
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, face_name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        start = True
    if cv2.waitKey(1) & 0xFF == ord('f'):
        name_face = True


video_capture.release()
cv2.destroyAllWindows()