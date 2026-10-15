a=int(input())
s4=a%10
s3=a//10%10
s2=a//100%10
s1=a//1000
if s4==s1 and s3==s2:
    print('настоящее')
else:
    print('кривое')