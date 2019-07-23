from typing import List
Vector = List[float]
import random
from scratch.linear_algebra import distance, add, scalar_multiply
from matplotlib import pyplot as plt

def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    step = scalar_multiply(step_size, gradient)
    return add(v, step)

def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * value for value in v]

# pick a random starting point
NUM_VARIABLES_IN_FUNCTION = 3
v = [random.uniform(-10, 10) for i in range(NUM_VARIABLES_IN_FUNCTION)]

STEP_SIZE = -0.01
intermediate_values = [[] for i in range(NUM_VARIABLES_IN_FUNCTION)]
NUM_EPOCHS = 1000
for epoch in range(NUM_EPOCHS):
    grad = sum_of_squares_gradient(v)
    v = gradient_step(v, grad, STEP_SIZE)
    for index in range(NUM_VARIABLES_IN_FUNCTION):
        intermediate_values[index].append(v[index])
    print(epoch, v)

assert distance(v, [0, 0, 0]) < 0.001

STARTING_POINT = 0
for index in range(NUM_VARIABLES_IN_FUNCTION):
    plt.plot(range(NUM_EPOCHS - STARTING_POINT),
             intermediate_values[index][STARTING_POINT:],
             '-',
             label='var {0}'.format(index))
plt.legend()
plt.show()
