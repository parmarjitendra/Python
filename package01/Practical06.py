import os
print("os.name = " ,  os.name  )

print("os.getenv('PATH')= ", os.getenv('PATH')  )

print("os.getcwd() = ", os.getcwd()   )

#os.mkdir("IIIKDir")
print("New Folder created successfully.")

os.chdir("IIIKDir")
print("folder location change .")
print("os.getcwd() = ", os.getcwd()   )

os.chdir("..")
os.rmdir('IIIKDir')
print("folder deleted.")
