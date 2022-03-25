#Dourdoumas Marios | ICSD:3212017045
#Kryptografia | Askhsh 2
#Chinese Remainder Theorem v1.5

soldiers = 2000
ai = [] #Stratiwtes pou perisseuoun
ni = [] #Seires
Ni = [] #N/ni
mi = [] 
aiNiMi = []
N = 1
x = 0
                    #Synarthseis
#<---------------------------------------------->
def euclid(a,b):
    t = b
    mods = []
    quotients = []
    x = [0,1]
    i = 0 
   
    while (b%a != 0):
        q = b//a
        r = b % a
        b = a * q + r
        mods.append(b%a)
        quotients.append(b//a)
        b = a
        a = r
        
    for i in range(2,len(quotients)+2):
        new = ( x[i-2] - (x[i-1] * quotients[i-2]) ) % t
        x.append(new)
        
    print("Reverse is: ",x[-1])
    return x[-1]
#<---------------------------------------------->
#Bhma 1

#<------------------------------->
ni = [int(element) for element in input("Dwse tis seires: ").split()]
ai = [int(element) for element in input("Dwse tous stratiwtes: ").split()]
#<------------------------------->

for i in range(0,len(ni)):
    N = N * ni[i]

#Bhma 2
print(N)

for i in range(0,len(ni)):
    Ni.append(int( N/ni[i]))
    
print("Ni = ", Ni)

#Bhma 3 

#Ypologismos antistrofwn mod me thn xrhsh algorithmou eukleidh

for i in range(0,len(ai)):
    mi.append(int(euclid(Ni[i],ni[i])))
    
print("Mi = ",mi)

#Na kanw ton ypologismo me ton algorithmo tou euklieidh

#Bhma 4
for i in range(0,len(ai)):
    aiNiMi.append(ai[i] * Ni[i] * mi[i])
    
print("Ola mazi = ",aiNiMi)

#Bhma 5


result = sum(aiNiMi) % N
print("Stratiwtes pou parousiasthkan: {}, Stratiwtes pou leipoun {}".format(result,soldiers - result))

