import face_recognition

image = face_recognition.load_image_file('./images/groups/england-football-team.jpg')
face_locations = face_recognition.face_locations(image)

print(face_locations)
print(len(face_locations))