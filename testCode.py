# svd process of PCA
def mySvd(mat, div):
    timeList = [i for i in range(div)]
    s1List = [cos(2 * pi * i / div) for i in range(div)]
    s2List = [sin(2 * pi * i / div) for i in range(div)]
    cx1List = []
    cx2List = []

    # s 에서 x 로 넘어가는 과정도 구현 필요
    # x1List = [9 * cos(2 * pi * i / 5000) + 4 * sin(2 * pi * i / 5000) for i in range(5000)]
    x1List = [myMat[0][0] * cos(2 * pi * i / div) + myMat[0][1] * sin(2 * pi * i / div) for i in range(div)]
    # x2List = [4 * cos(2 * pi * i / 5000) + 3 * sin(2 * pi * i / 5000) for i in range(5000)]
    x2List = [myMat[1][0] * cos(2 * pi * i / div) + myMat[1][1] * sin(2 * pi * i / div) for i in range(div)]

    # Centering
    x1List, x2List = center(x1List, x2List)

    # Solve for U
    U, inv_U, thMax = u(x1List, x2List)

    # Solve for s
    S, inv_S = s(s1List, s2List, x1List, x2List, thMax)

    for i in range(len(x1List)):
        mul = np.matmul(inv_S, np.matmul(inv_U, [[x1List[i]], [x2List[i]]]))
        cx1List.append(mul[0])
        cx2List.append(mul[1])

    V = v(cx1List, cx2List)
    plt.plot(timeList, cx1List, timeList, cx2List)
    plt.show()
    return U, S, V
