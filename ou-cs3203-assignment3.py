def calculateSum(numbers):
    sum = 0
    for x in numbers:
        sum = sum + x
    return sum

def calculateProduct(numbers):
    product = 1
    for x in numbers:
        product = product * x
    return product

def reverseList(numbers):
    numbers.reverse()
    return numbers

print("Hello User! \nThis program will calculate the sum & product of a list of numbers you enter. \nThis list will be 5 integers long.\n")

numberList = []
for x in range(5):
    number = int(input("Please enter a number for your list: "))
    numberList.append(number)

print("The sum is " + str(calculateSum(numberList)) + ".")
print("The product is " + str(calculateProduct(numberList)) + ".")
<<<<<<< HEAD
print("The list reversed is " + str(reverseList(numberList)))    
=======

#Hey Professor Nicolas! I'm just making some changes here, I figured a
#comment would work.
    
>>>>>>> f43a5c5 (Part 10: Made changes for new branch)
