Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> score = input("Enter Score: ")
Enter Score: 5
>>> scr = float(score)
>>> if scr<0.6 and scr>=0 :
	print("F")
elif scr>=0.6 and scr<0.7 :
	print("D")
elif scr>=0.7 and scr<0.8 :
	 print("C")
elif scr>=0.8 and scr<0.9 :
	print("B")
elif scr>=0.9 and scr<1.0 :
	print("A")
else :
	print("Invalid grade!")

	
Invalid grade!
>>> 