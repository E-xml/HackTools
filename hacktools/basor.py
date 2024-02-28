while True:
	inbase = input("Type the in base [dec/bin/hex/oct] : ")
	if inbase != "dec" and inbase != "bin" and inbase != "hex" and inbase != "oct":
		print("Sorry, unknown base")
	else:
		break

while True:
	outbase = input("Type the out base [dec/bin/hex/oct] : ")
	if outbase != "dec" and outbase != "bin" and outbase != "hex" and outbase != "oct":
		print("Sorry, unknown base")
	else:
		break
		
while True:
	flagError = False
	number = str(input("Type a number : "))
	if inbase == "bin":
		for chars in number:
			if chars != "1" and chars != "0":
				flagError = True
			else:
				pass
	
	elif inbase == "oct":
		for chars in number:
			if chars != "1" and chars != "2" and chars != "3" and chars != "4" and chars != "5" and chars != "6" and chars != "7" and chars != "0":
				flagError = True
			else:
				pass
				
	elif inbase == "dec":
		for chars in number:
			if chars != "1" and chars != "2" and chars != "3" and chars != "4" and chars != "5" and chars != "6" and chars != "7" and chars != "8" and chars != "9" and chars != "0":
				flagError = True
			else:
				pass
				
	else:
		for chars in number:
			if chars != "1" and chars != "2" and chars != "3" and chars != "4" and chars != "5" and chars != "6" and chars != "7" and chars != "8" and chars != "9" and chars != "0" and chars != "A" and chars != "B" and chars != "C" and chars != "D" and chars != "E" and chars != "F" and chars != "a" and chars != "b" and chars != "c" and chars != "d" and chars != "e" and chars != "f":
				flagError = True
			
			else:
				pass
	if flagError == True:
		print("Sorry, wrong digits detected")
		pass
	else:
		break


if inbase == "dec":
	if outbase == "dec":
		print(int(number))
	
	elif outbase == "bin":
		print(bin(int(number))[2:])
		
	elif outbase == "hex":
		print(hex(int(number))[2:])
		
	else:
		print(oct(int(number))[2:])
		
elif inbase == "bin":
	if outbase == "dec":
		print(int(number, 2))
		
	elif outbase == "bin":
		print(number)
		
	elif outbase == "hex":
		print(hex(int(number, 2))[2:])
		
	else:
		print(oct(int(number, 2))[2:])
		
elif inbase == "hex":
	if outbase == "dec":
		print(int(number, 16))
		
	elif outbase == "bin":
		print(bin(int(number, 16))[2:])
		
	elif outbase == "hex":
		print(number)
		
	else:
		print(oct(int(number, 16))[2:])
		
else:
	if outbase == "dec":
		print(int(number, 8))
		
	elif outbase == "bin":
		print(bin(int(number, 8))[2:])
		
	elif outbase == "hex":
		print(hex(int(number, 8))[2:])
		
	else:
		print(number)
