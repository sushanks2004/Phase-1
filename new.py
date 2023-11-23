import random
import itertools
n=input("Hey 😊, What should we call you?\n")
print("Hello! ",n,"🤚welcome to password generator")

x=int(input("How many numbers you want in your passwords:"))
num=[i for i in range (10)]
a=random.sample(num,x)
print(num)

y=int(input("How many letters you want in your password:"))
alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b=random.sample(alp,y)

z=int(input("How many Symbols you want in your password:"))
symb="!@#$%^&*|?<>?~"
c=random.sample(symb,z)

print("This is your password as per your requirements:")
var=list(itertools.chain(a,b,c))
final=random.sample(var,len(var))
for i in range(len(final)):
    print(final[i],end="")