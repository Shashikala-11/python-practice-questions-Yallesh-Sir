c=input('Enter a char:')

if c.isupper() or c.islower():
    print('Its an alphabet')
    if c in 'AEIOUaeiou':
        print('Its a vowel')
    else:
        print('Its not a vowel')
else:
    print('Its no an alphabet')            
