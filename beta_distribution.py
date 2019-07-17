import math
from matplotlib import pyplot as plt

def beta_dist(alpha: float, beta: float) -> float:
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x: float, alpha: float, beta: float) -> float:
    if x <= 0 or x >= 1:
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / beta_dist(alpha, beta)


def plot_beta_pdf(alpha: float, beta: float):
    resolution = 1000
    x = [x / resolution for x in range(1, resolution)]
    y = [beta_pdf(y, alpha, beta) for y in x]
    plt.plot(x, y, '-', label='Beta({0},{1})'.format(alpha, beta))

# plot_beta_pdf(1, 1)
# plot_beta_pdf(10, 10)
# plot_beta_pdf(4, 16)
# plot_beta_pdf(16, 4)

plot_beta_pdf(1, 4)
plot_beta_pdf(2, 8)
plot_beta_pdf(4, 16)
plot_beta_pdf(8, 32)
plot_beta_pdf(16, 64)

plt.legend()
plt.show()
