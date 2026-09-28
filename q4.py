c=input('Enter a char:')

if c.isupper():
    print('char is upper')
elif c.islower():
    print('char is in lower')    

elif c.isdigit():
    print('Char is a digit')    
else:
    print('char is a special symbol')