a = list( range(5)  )
print("a = ", a)

b = list( range(1, 5)  )
print("b = ", b)

c = list( range(99, 102)  )
print("c = ", c)



d = tuple( range(5)  )
print("d = ", d)

e = tuple( range(1, 5)  )
print("e = ", e)

f = tuple( range(99, 102)  )
print("f = ", f)


g = [11 , 22, 33]

h = (12 , 23, 34)


print( type(g) )
print( type(h) )

print("g = ",  g)

g.append(44)


print("g = ",  g)


print( g[0]  )

#h.append(44)    #Error