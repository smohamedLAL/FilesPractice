# my_file = open("my_file.txt", "wt")
# my_file.write("wibbley y wobbley timey wimey \n")
# my_file.write("don't \n")
# my_file.write("blink \n")

# my_file = open("my_file.txt" , "rt")

# for line in my_file:
#   if "w" in line:
#     continue

#   print(line)

# my_file.close()

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@55word123!",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE books (isbn INT NOT NULL PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), year INT(255), price INT(255))")

sql = "INSERT INTO books (isbn, title, author, year, price) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("97801", "Silent Spring", "Rachel Carson", "2020", "9.99"),
    ("97814", "H is for Hawk", "Helen Macdonald", "2014", "9.99"),
]

print("Hello World")
print("my name is saffiya")
