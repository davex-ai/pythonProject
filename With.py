file = "Your filename.txt"

with open(file, 'r') as files:
    """With keyword auto closes the file after reading"""
    cont = files.read()
    print(cont)

# try:
#     files = open(file, 'r')
#     cont = files.read()
#     print(cont)
# finally:
#     files.close()