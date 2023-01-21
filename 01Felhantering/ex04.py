# Uppgift 4:
   
# Koden nedan tar den 5:e bokstaven av varje ord i listan food och lägger till denna bokstav i den nya listan fifth. 
# Denna kod genererar dock fel. 

# Implementera felhantering med try-/except-block så att programmet blir körbart utan fel.
# Om ett ord inte är tillräckligt långt för att den 5:e bokstaven skall kunna plockas ut, 
# så skall inget läggas till i listan fifth.

# Anmärkning: Man kan använda uttycket pass i Python om man vill ha ett uttyck i koden som inte utför något, 
# d.v.s. pass är en null-operation och inget händer när det exekveras.

foods = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]

fifth = []
for food in foods:
    try:
        fifth.append(food[4])
    except IndexError:
        pass
    except Exception as error:
        print(error)
        print(type(error))
print(fifth)
