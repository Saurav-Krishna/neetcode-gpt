class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        result = init
        for _ in range(iterations):
            result = result - learning_rate*(2* result)
            print(result)
        return round(result,5)

"""
x^2 -> 2x (direction)

x_new = x_old - alpha*(derivative of funciton)

x_old = init (a random value or approx value) [f(x)]

x_new = 
"""

