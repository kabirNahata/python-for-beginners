# Reading from a file

file = open("example.txt", "r")  # 'r' means read mode
content = file.read()
file.close()

print("File content:")
print(content)
