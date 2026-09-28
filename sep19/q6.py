a=eval(input('Enter data:'))

if type(a) in (list,set ,tuple,str,dict):
    print("its a multivalued datatype")
    if type(a) in (list,set,dict):
        print('Its mutable data type')
    else:
        print('Its immutable data type')    

else:
    print('Its not multi valued datatype')    