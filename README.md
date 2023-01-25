# Carplace Backend
This repository is the backend containing the API using the Django REST Framework for the Carplace frontend application

for the deployed backend click [here](https://backend-pp5.herokuapp.com/)

for the deployed fronted click [here](https://frontend-pp5.herokuapp.com/)

for the frontend repository click [here](https://github.com/MustafaSahinci/pp5-frontend)

## Database
![database](assets/database.png)
User Model
- The User model contains information about the user. It is part of the Django allauth library.
- One-to-one relation with the Profile model owner field
- ForeignKey relation with the Following model owner and followed fields
- ForeignKey relation with the Car model owner field
- ForeignKey relation with the Comments model owner field
- ForeignKey relation with the biddings model owner field
- ForeignKey relation with the Save model owner field

Profile Model
- The Profile model contains the following fields: owner,created_at, updated_at, name, content and image
- One-to-one relation between the owner field and the User model id field

Following Model
- The Following model contains the following fields: owner, followed and created_at
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the followed field and the User model id field

Car Model
- The Car model contains the following fields: owner, created_at, updated_at, title, content, year, km, price, image, image2, image3 and image4
- Foreignkey relation between the owner field and the User model id field
- ForeignKey relation with the Comments model car field
- ForeignKey relation with the Biddings model car field
- ForeignKey relation with the Save model car field

Comments Model
- The Comment model contains the following fields: owner, car, created_at, updated_at and content
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the car field and the Car model owner field

Biddings Model
- The Biddings model contains the following fields: owner, car, created_at, updated_at and content
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the car field and the Car model owner field

Save Model
- The Save model contains the following fields: owner, car and created_at
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the car field and the Car model owner field