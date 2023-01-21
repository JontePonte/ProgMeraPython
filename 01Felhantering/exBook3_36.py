# Print the following lists to a file, add error fix

l = [
    [45, 78, 56, 34],
    [9, 23, 23],
    [34, 87],
    [12, 19, 78, 55, 45, 99]
]

try:
    with open('myfile.txt', 'w') as f:
        for row in l:
            try:
                for item in row:
                    f.write(f'{item} ')
                f.write('\n')
            except:
                print('Could not write to file')
except:
    print('list could not be opened')

