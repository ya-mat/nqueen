# -*- coding: utf-8 -*-

# This code is writen by Yasuhiro Matsumoto.
# Copyright (C) 2017/11/30.

#----------------------------------------
def diffuu(vv, i, j, sizen, sum_row, sum_col, diag1, diag2):
    sum_row = 0
    sum_col = 0

    for k in range(sizen):
        sum_row += vv[k][j]
        sum_col += vv[i][k]

    diag1 = 0

    #naname kara

    return

#----------------------------------------
def main(sizen, aa, bb):
    import random

    uu = [[i for i in range(sizen)] for j in range(sizen)]
    vv = [[i for i in range(sizen)] for j in range(sizen)]

    # Initialize
    for i in range(sizen):
        for j in range(sizen):
            uu[i][j] = 10 - int(20.0*random.random())
            if uu[i][j] > 0:
                vv[i][j] = 1
            else:
                vv[i][j] = 0

    sum_row = 0
    sum_col = 0

    tt = 0
    diag = 1
    diag1 = 0
    diag2 = 0
    cc = 1

    # Newral
    while diag > 0 and tt < 1000:
        diag = 0
        for i in range(sizen):
            for j in range(sizen):
                uu[i][j] += diffuu(vv, i, j, sizen, sum_row, sum_col, diag1, diag2)

                if uu[i][j] > 15:
                    uu[i][j] = 15
                else if uu[i][j] < -15:
                    uu[i][j] = -15


                if uu[i][j] > 0:
                    vv[i][j] = 1
                else:
                    vv[i][j] = 0

                conf = 1
                if sum_row + sum_col == 2 and diag1 == 2 and diag2 == 2:
                    conf = 0

                diag += conf

#        if tt % 20 < 5:
#            cc = 4
#        else:
#            cc = 1

    # result
    for i in vv:
        print vv[i]

    print 'Solved!!, t = ', t


#----------------------------------------
if __name__ == '__main__':
    sizen = 8
    aa = 1
    bb = 1
    main(sizen, aa, bb)








