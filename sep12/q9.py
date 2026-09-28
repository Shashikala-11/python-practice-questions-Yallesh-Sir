data=eval(input('Enter data:'))

if type(data)==int or type(data)==float or type(data)==complex or type(data)==bool :
    print('Single valued datatype')
else :
    print('Multi-valued datatype')    