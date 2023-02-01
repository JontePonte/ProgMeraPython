
# -*- coding: utf-8 -*-
"""
Studentens namn: 
Student-ID (Sxxxxxx): 
"""
import time 
import random
def lotta_spelare(spelarnamn):
    # Lottar vilken av de två spelarna som får börja
    # Inparameter:
    #   spelarnamn  Lista/Array/List av string innehållande namn på de två spelarna
    # Returvärde:
    #   Integer     Nummer på den spelare, 0 eller 1, som vann lottdragningen. 
    #               Nummer motsvarar index i listan spelarnamn
    
    print('')
    print('Lottar vem som skall börja...')
    time.sleep(1)
    antal_slumptal = random.randint(10, 20)
    lottningsrad = ''
    lottnummer = 0
    print('')
    for i in range(antal_slumptal):
        lottnummer = random.randint(0, 1)
        lottningsrad += spelarnamn[lottnummer] + ' '
    print(lottningsrad)
    print('')
    print(spelarnamn[(lottnummer+1)%2] + ' får börja skriva vilket ord som ' + spelarnamn[lottnummer] + ' skall försöka gissa!')
    
    return lottnummer


print("###################")
print("### GISSA ORDET ###")
print("###################")

spelare = [['',0],['',0]]
spelare[0][0] = input('Namn på spelare 1: ')
spelare[1][0] = input('Namn på spelare 2: ')
print()
print("Hej " + spelare[0][0] + " och " + spelare[1][0] + ", välkomna till spelet \"Gissa ordet\"")
print()
print("Bestäm på förhand om orden får innehålla både")
print("versaler (stora bokstäver) och gemener (små bokstäver)")
print("eller bara gemener (små bokstäver)")
print()
input("Tryck \"Enter\" för att fortsätta...")


# Variabel som styr hur länge man vill spela vidare
spela_vidare = True
while spela_vidare:
    # Hur många bokstäver får orden innehålla?
    max_olika_bokstaever = input("Hur många olika bokstäver får orden innehålla? ")
    
    # Hur många gissningar är tillåtna?
    antal_forsok = int(input("Hur många felaktiga gissningar är tillåtet? "))
    # Lotta vem som skall börja
    aktuell_spelare = lotta_spelare([spelare[0][0],spelare[1][0]])
    print()
    input("Tryck \"Enter\" för att fortsätta...")
    # Rensa concolen 
    print("\033[H\033[J", end="")
    # Vänta 1 sekund
    time.sleep(1) 
    print()
    print()
    print()
    # Variabel för att kontrollera att båda spelarna får gissa ett ord
    spelomgang = 0
    while spelomgang < 2:
        antal_forsok_kvar = antal_forsok
    
        # Fråga efter det hemliga ordet
        # och kontrollera antal olika bokstäver
        
        print()
        print("Nu får " + spelare[aktuell_spelare][0] + " titta bort när " + spelare[(aktuell_spelare+1)%2][0] + " skriver in det \"hemliga ordet\"")
        
        time.sleep(1)
    
        antal_tecken_ok = False
        
        while not antal_tecken_ok:
            hemliga_ordet = input(spelare[(aktuell_spelare+1)%2][0] + ", skriv in ditt \"hemliga ord\" med högst " + max_olika_bokstaever + " olika bokstäver: ")
            olika_bokstaver = len(set(hemliga_ordet))    
            
            if olika_bokstaver < int(max_olika_bokstaever):
                antal_tecken_ok = True
            else:
                print()
                print("För många olika bokstäver, max antal är", max_olika_bokstaever)


        # Rensa concolen
        print("\033[H\033[J", end="")
        # Vänta 1 sekund
        time.sleep(1) 
        print()
        print()
        # Variabel för alla gissade bokstäver
        gissade_bokstaever = '' 
        # Variabel för att se om ordet är funnet
        ord_korrekt = False
        # Upprepa så länge som antal_forsok_kvar tillåter och hemliga_ordet inte är hittat
        while antal_forsok_kvar > 0 and ord_korrekt is False:
        
            # Anta att ordet är funnet, ord_korrekt sätts till False senare om det inte är funnet     
            ord_korrekt = True        
        
            # Fråga efter en bokstav och lägg till gissad_bokstav till alla gissade_bokstaever
            gissad_bokstav = input(spelare[aktuell_spelare][0] + ", gissa en bokstav i ordet: ")
            gissade_bokstaever += gissad_bokstav 
    
            # Variabel för utskrift av de gissade_bokstaever i hemliga_ordet
            funnet_ord = ""
    
            # Kontrollera alla gissade bokstäver mot hemliga_ordet
            for bokstav in hemliga_ordet: 
                # Finns bokstav i hemliga_ordet
                if bokstav in gissade_bokstaever: 
                    # Lägg då till bokstav på rätt plats i funnet_ord            
                    funnet_ord += bokstav 
                else: 
                    # Om inte, skriv ut ett _
                    funnet_ord += "_"
                    ord_korrekt = False
    
            # Skriv ut träffade och missade bokstäver 
            print(funnet_ord)
            
            if ord_korrekt == True: 
                # Är hela hemliga_ordet funnet?
                # Meddela då detta och avbryt 
                print()
                print("Rätt!")
                print("Det hemliga ordet är funnet!")
        
                spelare[aktuell_spelare][1] = (spelare[aktuell_spelare][1] + 1)
            
                # Byt aktuell spelare och räkna upp spelomgang
                aktuell_spelare = (aktuell_spelare+1)%2
                spelomgang = spelomgang + 1
            else:        
                # Om gissade bokstaven inte var i hemliga_ordet
                if gissad_bokstav not in hemliga_ordet: 
                    # Minska antalet försök med 1 och meddela att gissning var fel
                    antal_forsok_kvar -= 1 
                    print()
                    print("Fel!")
                    # Hur många försök har spelaren kvar?
                    print("Du har", antal_forsok_kvar, 'gissningar kvar')
                else:
                    print()
                    print("Rätt!")
                    # Hur många försök har spelaren kvar?
                    print("Du har", antal_forsok_kvar, 'gissningar kvar')
    
                # Om man gissat fel för många gånger    
                if antal_forsok_kvar == 0: 
                    # print "You Lose" 
                    print()
                    print("Du hittade inte det hemliga ordet")
                    print("Det hemliga ordet var:", hemliga_ordet)
        
                    # Byt aktuell spelare och räkna upp spelomgang
                    aktuell_spelare = (aktuell_spelare+1)%2
                    spelomgang = spelomgang + 1
        
        
    # Skriv ut aktuell ställning när en omgång är fullbordad
    if spelomgang == 2:
        print()
        print("Aktuell poängställning:")
        print(spelare[0][0], "har", spelare[0][1], "poäng")
        print(spelare[1][0], "har", spelare[0][1], "poäng")
            
        # Vill de spela vidare?
        print()
        svar = input("Vill ni spela vidare (J/N)?: ")
        
        if(svar == 'j' or svar == 'J'):                
            spela_vidare = True
        else:
            spela_vidare = False   
# Spelet avslutas...
print()
print("Tack för att ni spelade")
print()
print("###################")
print("### GISSA ORDET ###")
print("###################")
        
"""
Logiskt fel eller syntaxfel 1
Radnummer: 107
Ursprunglig kodrad:
while antal_forsok_kvar >= 0 and ord_korrekt = False:

Justerad kodrad:
while antal_forsok_kvar >= 0 and ord_korrekt is False:

Orsak till att kodraden ändrats: 
"=" tilldelar variabeln ord_korrekt värdet "False". Innuti while-loopen vill vi testa om
den är False eller inte.

    
Logiskt fel eller syntaxfel 2
Radnummer: 86
Ursprunglig kodrad:
hemliga_ordet = input(spelare[(aktuell_spelare+1)%3][0] + ", skriv in ditt \"hemliga ord\" med högst " + max_olika_bokstaever + " olika bokstäver: ")

Justerad kodrad:
hemliga_ordet = input(spelare[(aktuell_spelare+1)%2][0] + ", skriv in ditt \"hemliga ord\" med högst " + max_olika_bokstaever + " olika bokstäver: ")

Orsak till att kodraden ändrats:
(aktuell_spelare+1)%2 ger index som växlar mellan 0 och 1. Samma sak modulus 3 ger växlande index 0, 1 och 2


Logiskt fel eller syntaxfel 3
Radnummer: 107
Ursprunglig kodrad:
while antal_forsok_kvar >= 0 and ord_korrekt is False:

Justerad kodrad:
while antal_forsok_kvar > 0 and ord_korrekt is False:

Orsak till att kodraden ändrats: 
Spelare tillåts en extra gissning eftersom antal_forsok blir -1 efter att while-loopen testas
OBS Två fel samma rad (det går att lösa på andra rader också)

    
Logiskt fel eller syntaxfel 4
Radnummer:
Ursprunglig kodrad:
Justerad kodrad:
Orsak till att kodraden ändrats:

Logiskt fel eller syntaxfel 5
Radnummer:
Ursprunglig kodrad:
Justerad kodrad:
Orsak till att kodraden ändrats: 
    
"""
