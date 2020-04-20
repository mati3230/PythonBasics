import timeit

'''
python lambda:

lambda arguments : expression
The expression is executed and the result is returned.

Example:
x = lambda a : a + 10
print(x(5)) 

--> will print 15

https://www.w3schools.com/python/python_lambda.asp
'''

def solution_simple(a, b, n):
    """This is my simple and naive approach to the problem"""
    pass # <code goes here>


if __name__ == '__main__':
    a = 3
    b = 5
    n = 10
    repetitions = 50

    # stop time
    time_solution_simple = timeit.timeit(lambda: solution_simple(a, b, n),
        number=repetitions) / repetitions
    
    print("solution_simple", time_solution_simple)