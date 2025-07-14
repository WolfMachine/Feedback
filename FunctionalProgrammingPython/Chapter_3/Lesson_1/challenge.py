# Challenge for "Learn Functional Programming In Python": Chapter 3 - Lesson 1

# Goal: Debug 'our_bugged_function(...) and turn it into a pure function to solve the challenge



# This is the function we need to debug and turn into a PURE function
def our_bugged_function(input_list, multiplier):
    for i in range(len(input_list)):
        input_list[i] *= multiplier
    return input_list





# === Do not touch code below! ================================================
# =============================================================================
from random import randint

my_list = []
expected_list = []

def main():
    global my_list, expected_list
    my_list = [randint(2,10), randint(1,10), randint(1,10), randint(1,10)]
    print( f"Input: {my_list}" )
    expected_list = [n for n in my_list]


    for i in range(4):
        multiplier = randint(2,10)
        new_list = our_bugged_function(my_list, multiplier)
        print("\n=============================")
        print(f"Test #{i+1}")
        print( f"Input Expected: {expected_list}")
        print( f"Input Actual: {my_list}")
        print( f"Multiplier: {multiplier}")
        test = [n * multiplier for n in expected_list]
        print( f"Output Expected: {test}")
        print( f"Output Actual: {new_list}")
        print("=============================")
        if(test_function1() and test_function2(new_list, multiplier)):
            print("Pass")
        else:
            print("Fail")

def test_function1():
    for i in range(len(my_list)):
        if expected_list[i] != my_list[i]:
            return False
    return True

def test_function2(test_list, multiplier):
    for i in range(len(test_list)):
        if test_list[i] != (expected_list[i])*multiplier:
            return False
    return True

main()
