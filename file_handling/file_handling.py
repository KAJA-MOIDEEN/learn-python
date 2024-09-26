# writing to file
file_path ='file_handling\example.txt'
image_path = r'file_handling\assets\thanujaAkka.jpg'

def write():
    with open(file_path, 'w') as file:
        file.write('Hello, kaja!')
        file.write('\n you succesfully you enterd in 4th month.')
        file.write('\n keep itup')
        print(f'The file writen successfully ')

def  read():
    with open(file_path,'r') as file:
        content = file.read()
        print(content)

def  append():
    with open(file_path,'a') as file:
        file.write("\ndon't putit in your head")
        print(f'The file appended successfully')

# write()
# read()
# append()

def image_read():
    with open (image_path,'rb') as file:
        img = file.read()
        print(img)
image_read()

