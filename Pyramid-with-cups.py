#insérez le nombre de gobelets dont vous disposez, et ce programme vous dira combien en utiliser pour faire une piramide et combien en prendre pour la base de cette dernière
a=0
c=0
b=int(input("nb gobelets : "))
while a<b:
    c=c+1
    a=a+c
    #print(a,c)
if a>b:
    a=a-c
    c=c-1
print(a,c)
