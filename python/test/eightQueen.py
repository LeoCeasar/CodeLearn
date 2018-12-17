#!/usr/bin/python
#coding=utf_8

#* eight queens problem with recurison
BoardSize = 8;

def underAttack(col,queens):
    left = right = col;
    for r,c in reversed(queens):
        left ,righy = left-1, right -1;

        if c in (left, col, right):
            return True;
    return False;

def solve(n):
    if n == 0:
        return [[]];
    smallerSolutions = solve(n-1);
    return [solution+[(n, i + 1)]
        for i in xrange(BoardSize)
            for solution in smallerSolutions
                if not underAttack(i+1,solution)]

for answer in solve(BoardSize)
    print answer;

