import numpy
import matplotlib


initialization=input("Greetings! Let's play a game. I want you to give me two numbers,"
                     "and I will tell you how much the first number raised to the power of,"
                     "the second number is. I will also tell you what the log in base 2 of,"
                     "x is. Wanna give it a try? If yes type 'yes', we'll get started. If not"
                     ", just say 'no'. ")

       
counter=1
if  initialization == "yes" or initialization == "Yes":
    x=float(input("Please enter the first number "))
    y=float(input("Please enter the second number... "))
    answer1=x**y
    print(x, "raised to the power of", y, "=", answer1)
    answer2=numpy.log2(x)
    print("Log in base 2 of", x, "=", answer2)     
elif initialization == "no" or initialization == "No":
    print("Ok then... I'm a bit disappointed to be honest")
    
else:
    while counter < 5 and (initialization != "yes" or initialization != "Yes" or initialization != "no" or initialization != "No"):
         initialization2=input("I didn't get that. So do you want to try or not?")
         counter += 1
         if initialization2 == "yes" or initialization2 == "Yes":
             x=float(input("Please enter the first number "))
             y=float(input("Please enter the second number... "))
             answer1=x**y
             print(x, "raised to the power of", y, "=", answer1)
             answer2=numpy.log2(x)
             print("Log in base 2 of", x, "=", answer2)
             break
         elif counter == 5: 
             print("Ok I give up")
             break
