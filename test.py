from app.database.database import users_collection

user = {

    "name": "Ashmit Pandey",

    "email": "ashmit@gmail.com"

}

users_collection.insert_one(user)

print("User inserted successfully.")