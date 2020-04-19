import face_recognition

image_of_boiko_borisov = face_recognition.load_image_file('./images/known/boiko_borisov.jpg')
boiko_borisov_encoding = face_recognition.face_encodings(image_of_boiko_borisov)[0]

unknown_image = face_recognition.load_image_file('./images/unknown/351.jpg')
unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces of imgs
results = face_recognition.compare_faces([boiko_borisov_encoding],unknown_image_encoding)

if results[0]:
    print('This is Boiko Borisov')
else:
    print('This is unknown')