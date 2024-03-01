import random

i = int(input("Enter the number of digits: "))
m = 0 
c = []
n = 0
b = 0 
while m < i:  
    random_number = random.randint(0, 100)  
    c.append(random_number)
    m += 1

print ("Random numbers ", c )

j = int(input("Index: "))
ng = c[::j]
print(ng)

for b in ng:
    n+=b
    
print (n) 
