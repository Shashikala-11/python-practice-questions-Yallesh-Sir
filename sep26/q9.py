num=123
rev,rem,n=0,0,num
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev==num:
    print('Palindrome')
else:
    print('Not palindrome')
