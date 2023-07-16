import random
import time

print("1. Basic Level - Addition")
print("2. Basic Level - Subtraction")
print("3. Basic Level - Multiplication")
print("4. Medium Level - Addition")
print("5. Medium Level - Subtraction")
print("6. Medium Level - Multiplication")
print("7. Advance Level - Addition")
print("8. Advance Level - Subtraction")
print("9. Advance Level - Multiplication")


level = int(input("Enter the level you want : "))

if level == 1:
    OPERATORS = ["+"]
    MIN_OPERAND = 2
    MAX_OPERAND = 10
    TOTAL_PROBLEMS = 10

elif level == 2:
    OPERATORS = ["+"]
    MIN_OPERAND = 11
    MAX_OPERAND = 30
    TOTAL_PROBLEMS = 15

elif level == 3:
    OPERATORS = ["+"]
    MIN_OPERAND = 30
    MAX_OPERAND = 50
    TOTAL_PROBLEMS = 20


elif level == 4:
    OPERATORS = ["-"]
    MIN_OPERAND = 2
    MAX_OPERAND = 10
    TOTAL_PROBLEMS = 10

elif level == 5:
    OPERATORS = ["-"]
    MIN_OPERAND = 11
    MAX_OPERAND = 30
    TOTAL_PROBLEMS = 15

elif level == 6:
    OPERATORS = ["-"]
    MIN_OPERAND = 30
    MAX_OPERAND = 50
    TOTAL_PROBLEMS = 20    


elif level == 7:
    OPERATORS = ["*"]
    MIN_OPERAND = 2
    MAX_OPERAND = 10
    TOTAL_PROBLEMS = 10

elif level == 8:
    OPERATORS = ["*"]
    MIN_OPERAND = 11
    MAX_OPERAND = 30
    TOTAL_PROBLEMS = 15

elif level == 9:
    OPERATORS = ["*"]
    MIN_OPERAND = 30
    MAX_OPERAND = 50
    TOTAL_PROBLEMS = 20     


else:
    print("Enter wrong choice!!")

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")   