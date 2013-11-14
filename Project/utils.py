import math


def rtToPts(rho, theta):
    a = math.cos(theta)
    b = math.sin(theta)
    x0 = a * rho
    y0 = b * rho
    return (int(x0 + 1000 * (-b)), int(y0 + 1000 * a)), (int(x0 - 1000 * (-b)), int(y0 - 1000 * a))