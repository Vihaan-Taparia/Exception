try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError as ex:
    print("Exeption: ",ex)

print("I am outside the try block")













try:
    num1= int(input("Enter a number: "))
    num2= int(input("Enter a number: "))
    result=num1/num2
    print("Result is a :",result)

except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter numerical value")
except NameError as x:  
    print("The exception is",ex)
except:
    print("Some error occured")
finally:
    print("I will execute no matter whatever happens")




valid=False
while not valid:
    try:
        n = int(input("Enter a number: "))
        #enter a even number
        while n%2==0:
            print("bye")
            valid=True

    except ValueError:
        print("Invalid")