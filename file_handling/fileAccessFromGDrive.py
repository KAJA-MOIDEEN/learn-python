from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authentication

gauth = GoogleAuth()
gauth.LocalWebserverAuth() #  # Creates local webserver and automatically handles authentication

drive = GoogleDrive(gauth)

# Replace the file ID with the ID of the file you want to read

file_id  = r'1z8NvgPlAcvr9olTV9a80vGFRci4A_t3oin_POQk7MVo'

file = drive.CreateFile({'id':file_id})
file.GetContentFile('Sheet1')

with open("Sheet1",'w') as f:
    f.write("Hello, World!")
    print("file writed ")
    
# Reading the content of the file
with open('Sheet1', 'r') as f:
    content = f.read()
    print(content)



