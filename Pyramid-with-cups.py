#enter the number of cups you have, and the program will tell you how many to use to make a pyramid and how many to use for its base
a=0
c=0
b=int(input("number of cups : "))
while a<b:
    c=c+1
    a=a+c
if a>b:
    a=a-c
    c=c-1
print("You can use ",a," of them, with ",c," cups on the base of the pyramid.")
