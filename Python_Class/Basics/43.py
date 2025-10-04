with open("img.png", "rb") as img:
    data = img.read()

with open("copy.jpg", "wb") as copy:
    copy.write(data)