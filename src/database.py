import mysql.connector

database = mysql.connector.connect(
    host="movieSmart.mysql.pythonanywhere-services.com",
    user="movieSmart",
    password="root1234",
    port=3306,
    database="movieSmart$Usuarios"
)