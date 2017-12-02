# -*- coding: utf-8 -*-

# This code is written by Yasuhiro Matsumoto.
# Copyright (C) 2017 Yasuhiro Matsumoto.

#----------------------------------------
def diffuu(vv, i, j, aa, bb, cc, sizen, row_col, diag):
    row_col[0] = 0
    row_col[1] = 0

    for k in range(sizen):
        row_col[0] += vv[k][j]
        row_col[1] += vv[i][k]

    diag[0] = 0

    k = 1
    while i + k <= sizen - 1 and j - k >= 0:
        diag[0] += vv[i + k][j - k]
        k += 1

    k = 1
    while i - k >= 0 and j + k <= sizen - 1:
        diag[0] += vv[i - k][j + k]
        k += 1

    diag[1] = 0

    k = 1
    while i + k <= sizen - 1 and j + k <= sizen - 1:
        diag[1] += vv[i + k][j + k]
        k += 1

    k = 1
    while i - k >= 0 and j - k >= 0:
        diag[1] += vv[i - k][j - k]
        k += 1

    h = 0
    if row_col[0] == 0:
        h += 1
    if row_col[1] == 0:
        h += 1

    return -aa*(row_col[0] + row_col[1] - 2) - bb*(diag[0] + diag[1]) + cc*h

#----------------------------------------
def main(sizen, aa, bb):
    import random

    uu = [[0 for i in range(sizen)] for j in range(sizen)]
    vv = [[0 for i in range(sizen)] for j in range(sizen)]
    row_col = [0 for i in range(2)]
    diag = [0 for i in range(2)]

    # Initialize
    for i in range(sizen):
        for j in range(sizen):
            uu[i][j] = 10 - int(20.0*random.random())
            if uu[i][j] > 0:
                vv[i][j] = 1
            else:
                vv[i][j] = 0

    tt = 0
    diag0 = 1
    cc = 1

    # Newral
    while diag0 > 0 and tt < 300:
        diag0 = 0
        for i in range(sizen):
            for j in range(sizen):
                uu[i][j] += diffuu(vv, i, j, aa, bb, cc, sizen, row_col, diag)

                if uu[i][j] > 10:
                    uu[i][j] = 10
                elif uu[i][j] < -10:
                    uu[i][j] = -10

                conv = 1
                if row_col[0] + row_col[1] == 2 and diag[0] <= 1 and diag[1] <= 1:
                    conv = 0
                diag0 += conv

        for i in range(sizen):
            for j in range(sizen):
                if uu[i][j] > 0:
                    vv[i][j] = 1
                else:
                    vv[i][j] = 0

        tt += 1

        if tt % 20 < 5:
            cc = 4
        else:
            cc = 1

    # result
    for i in range(sizen):
        for j in range(sizen):
            print vv[i][j],
        print ''

    print 'Solved!!, t = ', tt


#----------------------------------------
if __name__ == '__main__':
    sizen = 10
    aa = 1
    bb = 1
    main(sizen, aa, bb)








