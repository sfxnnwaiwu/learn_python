from pathlib import Path
from time import ctime # human readable time
import shutil # suports copying and moving files
from zipfile import ZipFile
import csv
import json
import sqlite3
import time
from datetime import datetime, timedelta
import random
import string
import webbrowser # the module is used to open a web browser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from string import Template
import sys

Path(r'')

path = Path("ecommerce/__init__.py")
print(path.exists())
print(path.mkdir())
print(path.rmdir())
path.rename("ecommerce2")

print(path.iterdir()) # This returns a generator function. We can loop through it to get the contents of the directory.
# for p in path.iterdir():
#     print(p)

path.unlink()

print(ctime(path.stat().st_mtime))

path.read_text()
path.write_text("Hello World")
path.write_bytes('Hello')

source = Path("ecommerce2")
target = Path() / "__init__.py"

shutil.copy(source, target)

# ZipFile("files.zip", "w").write("ecommerce2")
with ZipFile("files.zip", "w") as zip:

    # for p in path.glob("*"):
    #     zip.write(p, p.name)

    for p in Path("ecommerce2").rglob("*.*"):
        zip.write(p, p.name)

# zip.close() # This is not needed when using the with statement

with ZipFile("files.zip") as zip:
    # zip.extractall("extracted")
    print(zip.namelist())
    info =zip.getinfo("ecommerce2/__init__.py")
    print(info.file_size)
    print(info.compress_size)

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
    for row in reader:
        print(row)

# with open("data.json", "w") as file:
#     json.dump([{"transaction_id": 1000, "product_id": 1, "price": 5}, {"transaction_id": 1001, "product_id": 2, "price": 15}], file)

movie = [{"transaction_id": 1000, "product_id": 1, "price": 5}, {"transaction_id": 1001, "product_id": 2, "price": 15}]
json_string = json.dumps(movie)
print(json_string)

data = Path("data.json").read_text()
movies = json.loads(data)
print(movies)

with sqlite3.connect('db.sqlite3') as conn:
    # command = "select * from movies"
    command = "insert into movies (transaction_id, product_id, price) values (?, ?, ?)"
    # cursor = conn.cursor()
    # cursor.execute(command)
    # conn.executemany(command, movie)
    # conn.execute(command, (1000, 1, 5))
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
        conn.commit()


with sqlite3.connect('db.sqlite3') as conn:
    command = "select * from movies"
    # cursor = conn.cursor()
    # cursor.execute(command)
    # conn.executemany(command, movie)
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
    
    movies = cursor.fetchall()
    print(movies)

# time.sleep(1) # Wait for 1 second before running the next command

print(time.time()) # This will give us the current time and it represent the number of seconds from the beginning of the epoch (January 1, 1970)

def send_movie():
    for item in range(1000):
        pass


start = time.time()
send_movie()
end = time.time()
print(f"Time taken: {end - start} seconds") # This will give us the time taken to run the send_movie function


dt1 = datetime(2025, 1, 1) + timedelta(days=1)
dt2 = datetime.now()
dt = datetime.strptime("2025/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)

print(dt.strftime("%Y/%m/%d"))
print(f"{dt.year}/{dt.month}/{dt.day}")

print(dt2 > dt1)
duration = dt2 - dt1
print(duration)
print(duration.days)
print(duration.seconds)
print(duration.total_seconds())


print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5], k=2))
print(random.choices("abcdefghij", k=4))

numbers = [random.randint(1, 100) for _ in range(1000)]
print(numbers)

print(random.sample(numbers, k=5))

print(random.shuffle(numbers))

print("".join(random.choices("abcdefghij", k=4)))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

webbrowser.open("https://www.google.com") # This will open the web browser and navigate to the specified URL

# mime stands for Multipurpose Internet Mail Extensions
message = MIMEMultipart()
message["from"] = "John Doe"
message["to"] = "example.gmail.com"
message["subject"] = "This is a test email"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("photo.jpg").read_bytes()))

# body = Template(Path("test.html").read_text()).substitute({"name": "John Doe"})
body = Template(Path("test.html").read_text()).substitute(name="John Doe")
message.attach(MIMEText(body, 'html'))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:



with smtplib.SMTP(host="localhost", port=1025) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("johndoe@gmail.com", "password")  # Replace with your own email and password
    smtp.send_message(message) # This will send the email to the specified email address
    print("Email sent successfully")


print(sys.argv) # This will print the command line arguments and first argument will always be the name of the python program
