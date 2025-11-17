#Listas podem ser fatiadas assim como as strings:

s = [3,5,6,7]

#Fatiamento fixo:

print(s[0]) #3

print(s[1]) #5

print(s[2]) #6

print(s[3]) #7


print(s[-1]) #7

print(s[-2]) #6

print(s[-3]) #5

print(s[-4]) #3
 

print("\n")

#Fatiamento por intervalo:

print(s[:])  #[3, 5, 6, 7]

print(s[1:]) #[ , 5, 6, 7]

print(s[2:]) #[ ,  , 6, 7]

print(s[3:]) #[ ,  ,  , 7]

print(s[4:]) #[ ,  ,  ,  ]

print(s[:1]) #[3,  ,  ,  ]

print(s[:2]) #[3, 5,  ,  ]

print(s[:3]) #[3, 5, 6,  ]

print(s[:4]) #[3, 5, 6, 7]

print(s[:-1])#[3, 5, 6,  ]

print(s[:-2])#[3, 5,  ,  ]

print(s[:-3])#[3,  ,  ,  ]

print(s[:-4])#[ ,  ,  ,  ]

print(s[-1:])#[ ,  ,  , 7]

print(s[-2:])#[ ,  , 6, 7]

print(s[-3:])#[ , 5, 6, 7]

print(s[-4:])#[3, 5, 6, 7]

