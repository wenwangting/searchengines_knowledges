#!/usr/bin/env python
#! -*- coding: utf-8 -*-
from math import sqrt

postingListA = [3, 5, 8, 15, 24, 39,60, 68, 75, 81, 84, 89, 92, 97, 100, 115]
intermediateRes = [3, 5, 89, 95, 97, 99, 100, 101, 109, 115]

answer = []

def hasSkip(postingList, curInd, step):
    if step+curInd < len(postingList):
        print ("step: %d" % step)
        return 1
    else:
        return 0


def intersectWithSkips(p1, p2):
    answeer = []
    step1 = int(sqrt(len(p1)))
    step2 = int(sqrt(len(p2)))
    i = 0
    j = 0
    while i < len(p1) and j < len(p2):
        print "while %d %d" % (i, j)
        if p1[i] == p2[j]:
            answer.append(p1[i])
            print "answer %s" % answer
            if i < (len(p1) - 1) and j < (len(p2) -1):
                i += 1
                j += 1
            else:
                break
        elif p1[i] < p2[j]:
            if hasSkip(p1, i, step1):
                while( hasSkip(p1, i, step1) ):
                    if p1[i + step1] < p2[j]:
                        i += step1;
                        print "p1[%d]=%d p2[%d]=%d" % (i, p1[i], j, p2[j])
                    elif p1[i + step1] == p2[j]:
                        i += step1
                        break
                    else:
                        print ("i+1=%d" % (i+1))
                        i += 1
                        break
            else:
                i += 1
        else:
            if hasSkip(p2, j, step2):
                while( hasSkip(p2, j, step2) ):
                    print ("bigger")
                    if p2[j + step2] < p1[i]:
                        j += step2
                        print "p1[%d]=%d p2[%d]=%d" % (i, p1[i], j, p2[j])
                    elif p2[j + step2] == p1[i]:
                        j += step2
                        break
                    else:
                        print ("j+1=%d" % (j+1))
                        j += 1
                        break
            else:
                j += 1
    return answer


def main():
    res = intersectWithSkips(postingListA, intermediateRes)
    print res

if __name__ == '__main__':
    main()
