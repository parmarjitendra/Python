def show(empName, phone="1234567890",  city="Lucknow", company="XYZ"):
    print( "\nempName=",empName, "phone=",phone,"city=",city, "company= ",company  )

#rule1
show("chintu")

#rule2
show("pappu","9939393")

#Rule-4
show("Alisha", "9898" , city="Delhi" )  #Mixed mode




#Rule-3
show(empName="Pappu", phone="877666")  # 2 Keword Argument
show(phone="877666",  empName="Pappu" )
show(empName="Pappu", city="Kanpur" )


# following calls would be invalid:
#---------------------------------------

#show()                          # required argument missing
#show(empName="Jeetendra", '99998888')  # non-keyword argument after a keyword argument
#show("Jeetendra", empName="Alisha")    # duplicate value for the same argument
#show(name="Alisha" )                   # unknown keyword argument
