version="test-pre-pre-alpha v-0-0-0-1-a"
print("Welcome to DirectEdit ",version," !")
pw=str(input("What file do you want to make/read/write?"))
option=str(input("What do you want to do with the file{read(r),write(w),append(a),create(x)}?"))
if option == "w":
	f=open(pw,option)
	cr=str(input("what do you want to write?"))
	f.write(cr)
	f.close()
elif option =="r":
	f=open(pw,option)
	print(f.read())
	f.close()
elif option == "a":
	f=open(pw,option)
	ap=str(input("What do you want to add?"))
	f.write(ap)
	f.close()
elif option == "x":
	f=open(pw,option)
	print(pw," is created")
	f.close()
else:
	print("we cannot do that?")
	f=open("TextEdit-error-log.txt","w")
	f.write("Incorrect Option used: ")
	f.write(option)
	f.write(" Use r,w,a,or x!")
	f.close()
	f=open("DirectEdit-count.txt","w")
	aaa=0
	f.write(str(print(aaa)))
	print((aaa+1)*4)
	while aaa<100:
		aaa=aaa+1
		f.write(str(print(aaa)))
		print(((aaa+1)*4),"is now recorded")
	print("you have wasted",((aaa+1)*4)," bytes of your disk space")
	f.close()
