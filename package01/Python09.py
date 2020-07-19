import  datetime

mytime = datetime.datetime.now()



print(mytime.day,"-",mytime.strftime("%b"),"-",mytime.year,)
#or
print(mytime.day,"-",mytime.strftime("%B"),"-",mytime.year)


s1 = str(mytime.year) +  "-" + mytime.strftime("%B") + "-" + str(mytime.day)
print( s1 )
