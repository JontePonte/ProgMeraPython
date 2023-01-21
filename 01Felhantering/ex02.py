# Uppgift 2:
# Följande kod kan generera fel beroende på vad användaren matar in. 
# Implementera felhantering med try-/except-block så att programmet blir körbart oberoende av inmatning.
# Dessutom skall användaren kunna mata in data på nytt om fel uppstår.

CORRECT_INPUT = False

while not CORRECT_INPUT:
    input1 = input('Ange tal 1: ')
    input2 = input('Ange tal 2: ')
    
    try:
        data1 = float(input1)
        data2 = float(input2)
        product = data1 * data2

        print(f'Produkten {data1}*{data2} blir {product}')
        print('Slut...')
        CORRECT_INPUT = True
    
    except Exception as error:
        print(error)
        print(type(error))
        print('Please give new input')
