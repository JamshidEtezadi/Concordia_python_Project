# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from random import randint

def play():
    random_int = randint(0, 100)

    while True:
        user_guess = int(input("What number did you guess (0 - 100)?"))

        if user_guess == random_int:
            print(f"you fount the number({random_int}).Congrats")
            break

        if user_guess < random_int:
            print("Your number is less than the number you guessed")
            continue

        if user_guess > random_int:
            print("Your number is more than the number you gusessed")
            continue


if __name__ == '__main__':
    play()

for a in range(10):
    print("finished")
    breake

    if a < 5:
        print a
    else:
    print((a - 10))
    continue

N_START = 1
N_END = 100

for n in range(N_START,N_END +1):
    if n %2 ==0:
        print(n, end=" ")

size = int(input("what is the size of your square?"))

# method 1
for y in range(0, size):
    for x in range(0,size):
            print("%", end ="")
        print()

# method 2

for x in range(0, size):
    print("#"*size)

colours = []
colours = ["red", "green", "blue"]
prim_number = [2,3,5,7,11,19]
# change the list after it's created

for c in colours:
    print(c)

    # every student have two number
    # they must be grouped

    grades = [70, 72, 80, 81, 66, 67]

    grades_better = [
        [70, 72],
        [80, 81],
        [66, 67]]

    for s in grades_better:
        grade_midterm = s[0]
        grade_final = s[1]
        av = (grade_midterm+grade_final)/2
        print (av)
