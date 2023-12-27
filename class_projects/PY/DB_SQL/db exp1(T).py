import mysql.connector

myconnection  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "myapplication"
    
)

mycursor = myconnection.cursor()

sql = "INSERT INTO users (name,family,address,phone) VALUES (%s,%s,%s,%s)"

values = [
    ("ali reza" , "mosavi" , "mashhad" , 5633),
    ("farhaz" , "alizadeh" , "shiraz" , 769549),
    ("mohammad" , "jafari" , "ramsar" , 346734),
    ("zahra" , "moradi" , "teh" , 548345548),
    ("kamran" , "akrabi" , "rasht" , 569846),
    ("ramin" , "farhadi" , "zahedan" , 347347),
    ("dawood" , "mosavi" , "birjad" , 346346)
    
]

mycursor.executemany(sql,values)
myconnection.commit()
print(mycursor.rowcount  , "record inserted !")


mycursor.execute("SELECT * FROM users LIMIT 5 OFFSET 3")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM users ORDER BY name DESC")
for x in mycursor:
    print(x)

mycursor.execute("SELECT name,phone FROM users WHERE name LIKE '%ali%'")
for x in mycursor:
    print(x)

mycursor.execute("UPDATE users SET age = 10 WHERE age < 10")

myconnection.commit()











