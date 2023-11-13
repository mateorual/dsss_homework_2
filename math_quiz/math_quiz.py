import random


def random_integer(start_range:int, stop_range:int):
    """Gets an integer number selected from the specified range

    Parameters
    ----------
    start_range : int
        The starting point of the range
    stop_range : int
        The end point of the range

    Returns
    -------
    int
        A integer selected at random from the range [start_range, stop_range]
    """
    return random.randint(start_range, stop_range)


def random_operator():
    """Gets a string representation of an arithmetic operator among + , - , *

    Returns
    -------
    str
        either '+' or '-' or '*'
     """

    return random.choice(['+', '-', '*'])


def random_operation(value_1:int, value_2:int, operator:str):
    """Gets the resulting value of an operation (either +,-,*) between two numbers

    Parameters
    ----------
    value_1 : int
         A number to perform an operation with value_2
    value_2 : int
         A number to perform an operation with value_1

    Returns
    -------
    int
        Result of performing operation defined by operator between value_1 and value_2
    """

    print_operation = f"{value_1} {operator} {value_2}"
    if operator == '+':
        result_operation = value_1 + value_2
    elif operator == '-':
        result_operation = value_1 - value_2
    else:
        result_operation = value_1 * value_2

    return print_operation, result_operation

def math_quiz():
    """Generates 3 random operations between two integer numbers, where number1 belongs to [1,10]
    and number2 to [1,5] and prints the final score after evaluate the user performance
    Returns
    -------
    None
    """
    total_points = 0
    #Total attempts must be an integer to be used in range function
    total_attempts = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for attempt in range(total_attempts):
        get_Value_1 = random_integer(1, 10)
        get_Value_2 = random_integer(1, int(5.5))
        operator = random_operator()

        PROBLEM, ANSWER = random_operation(get_Value_1, get_Value_2, operator)
        print(f"\nQuestion: {PROBLEM}")
        user_answer = input("Your answer (integer): ")
        #To avoid incorrect inputs and a program crash
        try:
            user_answer = int(user_answer)
        except ValueError:
            print('Please enter a valid input (integer)')

        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            total_points += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {total_points}/{total_attempts}")

if __name__ == "__main__":
    math_quiz()
