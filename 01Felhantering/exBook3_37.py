
with open("myfile.txt", "r") as f:
    list_strings = f.read().split()
    
list_int = [int(item) for item in list_strings]

print(list_int)
