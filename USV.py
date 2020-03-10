import numpy as np
from math import *
import matplotlib.pyplot as plt


# centering
def center(x1List,x2List):
    avg1 = sum(x1List) / len(x1List)
    avg2 = sum(x2List) / len(x2List)

    for i in range(len(x1List)):
        x1List[i] -= avg1
    for i in range(len(x2List)):
        x2List[i] -= avg2

    return x1List, x2List


# solve for U
def u(x1List, x2List):
    cov = 0
    varDiff = 0

    for i in range(len(x1List)):
        cov += x1List[i] * x2List[i]

    for i in range(len(x2List)):
        varDiff += x2List[i] ** 2 - x1List[i] ** 2

    thMax = atan(-2 * cov / varDiff) / 2
    thMin = thMax - pi / 2

    # -26 degrees when 1 2, 2, -1
    U = [[cos(thMax), -sin(thMax)], [sin(thMax), cos(thMax)]]
    # print(thMax * 360 / 2 / pi)
    # U = [[cos(thMin), -sin(thMin)], [sin(thMin), cos(thMin)]]
    inv_U = [[cos(thMax), sin(thMax)], [-sin(thMax), cos(thMax)]]

    return U, inv_U, thMax


# define s
def s(s1List, s2List, x1List, x2List, thMax):
    ovar1 = 0
    ovar2 = 0
    var1 = 0
    var2 = 0
    thMin = thMax - pi / 2
    s = np.zeros((2, 2))
    inv_s = np.zeros((2, 2))

    for i in range(len(s1List)):
        ovar1 += (s1List[i] * cos(thMax) + s2List[i] * sin(thMax)) ** 2
        ovar2 += (s1List[i] * cos(thMin) + s2List[i] * sin(thMin)) ** 2

    for i in range(len(x1List)):
        var1 += (x1List[i] * cos(thMax) + x2List[i] * sin(thMax)) ** 2
        var2 += (x1List[i] * cos(thMin) + x2List[i] * sin(thMin)) ** 2

    s[0][0] = sqrt(var1 / ovar1)
    s[1][1] = sqrt(var2 / ovar2)
    inv_s[0][0] = 1 / sqrt(var1 / ovar1)
    inv_s[1][1] = 1 / sqrt(var2 / ovar2)

    return s, inv_s


# solve for V, using kurt(pi): independent 하게 만들기
def v(cx1List, cx2List):
    th = atan(cx2List[0] / cx1List[0])

    return [[cos(th), -sin(th)], [sin(th), cos(th)]]

