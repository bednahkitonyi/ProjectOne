# # # # # # # # age = 25
# # # # # # # # height = 5.567
# # # # # # # # name = "mutiso"
# # # # # # # # is_student = False

# # # # # # # # #printing the out
# # # # # # # # print("Age :", age)
# # # # # # # # print("Height :", height)
# # # # # # # # print('Name :', name)
# # # # # # # # print("Is_student :", is_student)

# # # # # # # #control flow

# # # # # # # age = 18
# # # # # # # if age > 18:
# # # # # # #     print("allowed to vote")
# # # # # # # else:
# # # # # # #     print("Not allowed to vote")

# # # # # # #student grading system

# # # # # # marks = int(input("Enter the student marks"))
# # # # # # if marks >= 70:
# # # # # #     print("Grade : Distinctio")
# # # # # # elif marks > 50 :
# # # # # #     print("Grade : credit")
# # # # # # elif marks > 40 :
# # # # # #     print("Grade : Pass")
# # # # # # else :
# # # # # #     print("failed miserable")

# # # # # #print numbers in the range of 5

# # # # # for i in range(5):
# # # # #     print(i)

# # # # #while loop
# # # # countdown = 5
# # # # while countdown > 0:
# # # #     print(" counting down", countdown)
# # # #     countdown -= 1
# # # #     print("Blast off")

# # # fruits = ["apple" , "mangoes", "banana"]
# # # print(fruits[2])

# # # #adding fruits to list
# # # fruits.append('grapes')
# # # print(fruits)

# # # #changing a fruit 
# # # fruits[1] ="orange"
# # # print(fruits)

# # # coordinates = (10, 10)
# # # coordinates[1] =9
# # # print(coordinates)

# # #functions in python
# # def greet(name):
# #     print("Hello : " +   name + "!")
# # greet("mutuku")

# def add_numbers(x, y):
#     return x+y
# results = add_numbers(10,9)
# print("The result is :", results)

# function to check if a number is odd or even

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
    
check_even_odd(9)