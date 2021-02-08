# from typing import Callable


def high_order_math(a: float, b: float, func):
    return (a + b)


x = high_order_math(1.2, 2.34, lambda x, y: x + y)
print(x)