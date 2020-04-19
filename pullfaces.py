from PIL import Image
import face_recognition

football_team = face_recognition.load_image_file('./images/known/boiko_borisov.jpg')
face_locations = face_recognition.face_encodings(football_team) 

for face_location in face_locations:
     top, right, bottom, left = face_location

     face_image = image[top:bottom, left:right]
     pil_image = Image.fromarray(face_image)
     pil_image.show()