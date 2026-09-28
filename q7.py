username,password=input('Enter username:'),input('Enter password:')

if username=="PYSpider":
    if password=='PY@123':
        print('Login successful')
    else:
        print('Password is incorrect')    
else:
    print('Incorrect username')


##### optimized ########
'''
user_name='pyspider'
password='py@123'

uname=input('username:')
if uname ==user_name:
    pwd=input('Password:)
    if pwd==password:
        print('login success')
    else:
        print('incorrect pwd')
else:
    print('incorrect username')            

'''