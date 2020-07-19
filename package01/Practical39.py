d =  { 'A':'Java', 'B':'J2EE', 'C':'Android',
       'D':'Python', 'E':'Hadoop',  'Key':'Value'}

print( "dictionary = ", d    )

d['F'] = 'JAPAN'
print( "dictionary = ", d    )


d['B'] = 'INDIA'
print( d )

del d['E']
print(d)


#print( d[0]  )   #Error
