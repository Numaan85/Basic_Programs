x=int(input('Enter the input '))
n1=0
n2=1
print(n1)
print(n2)
for i in range(2,x):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)