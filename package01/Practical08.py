import  datetime

mytime = datetime.datetime.now()

print("now = " , mytime  )



print(mytime.year, mytime.month, mytime.day,
      mytime.hour, mytime.minute, mytime.second,
      mytime.microsecond )



print(mytime.month  )       #  4

print(mytime.strftime("%B")   )  # April


print(mytime.strftime("%b")   )  #Apr
