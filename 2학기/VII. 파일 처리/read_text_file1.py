f = open("file.txt", "r", encoding = "UTF-8")

data = f.read()

f.close()
print(data)