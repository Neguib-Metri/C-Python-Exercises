#CALCULATING THE EULER CONSTANT

e=f=1.0 #initialazing variables
for i in range(2, 100):#loop to stablish the succesion
    e = e + 1.0 / f #addition of fractions
    f = f *i#getting the next denomiator for the next value aka, factorial
print(e)