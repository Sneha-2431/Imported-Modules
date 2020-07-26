import time

while True:
    with open("Vegetables.txt") as file:
        print(file.read())
        time.sleep(10)