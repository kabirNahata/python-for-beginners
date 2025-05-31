# Writing to a file

file = open("example.txt", "w")  # 'w' means write mode
file.write("Hello, this is a file!\n")
file.write("Writing more lines...\n")
file.close()

print("File written successfully.")
