# Uppgift 5:
   
# Implementera felhantering i funktionen get_value().
# Om ett indexeringfel uppstår beroende på att det specifika indexet inte finns, 
# så skall funktionen returnera None.

# I Python är None detsamma som NULL, som finns i de flesta andra programspråk. 
# En variabel kan exempelvis tilldelas värdet None/NULL, 
# vilket innebär den inte har något värde alls.

# Inga andra fel behöver hanteras.

def get_value(data_list, index):
    try:
        return data_list[index]
    except:
        return None


# Testkörning av funktionen
my_list = ['a', 'b', 'c']

value1 = get_value(my_list, 2)
print(value1)
value2 = get_value(my_list, 4)
print(value2)
