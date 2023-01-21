# Uppgift 1:
# Följande kod genererar en felsignal. Implementera felhantering med try-/except-block så att programmet blir körbart.
# Testa med att först fånga en specifik felsignal och sedan att fånga alla typer av felsignaler   

dagar = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]

i = 0 

while i <= 5:
    try:
        print(dagar[i])
    except IndexError:
        print('Your list got out of range')
    except Exception as e:
        print(e)
        print(type(e))
    i += 1
        
print('Slut...')

# Lösningsförslag:
    
# 