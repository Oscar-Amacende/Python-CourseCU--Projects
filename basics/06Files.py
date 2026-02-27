with open('output.txt', 'r+') as f:
    f.write("Hola jesiiii 9 \n")
    f.write("Hola jesiiii10 \n")
    file_stuff=f.read()
    print(file_stuff)
    
    file_stuff1=f.readline()
    print(file_stuff1)
print(f.closed)
