import time
import os

while True:
    if os.path.exists("Vegetables.txt"):
        with open("Vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(10)