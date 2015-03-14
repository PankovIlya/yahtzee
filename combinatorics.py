# -*- coding: utf-8 -*-
import math


def permutations(alist, kk):
    """ permutation """
    fooe = lambda lst, k: [[]] if not k else [[lst[num]] + item for num in xrange(len(lst))
                                                            for item in fooe(lst[:num] + lst[num+1:], k-1)] 
    return fooe(alist, kk)

def permutationsr(alist, kk):
    """ permutation with repetition"""
    fooe = lambda lst, k: [[]] if not k else [[lst[num]] + item for num in xrange(len(lst))
                                                            for item in fooe(lst, k-1)] 
    return fooe(alist, kk)

def combinations(alist, kk):
    """ combinations """
    fooc = lambda lst, k: [[]] if not k else [[lst[num]] + item for num in xrange(len(lst))
                                                            for item in fooc(lst[num+1:], k-1)] 
    return fooc(alist, kk)

def combinationsr(alist, kk):
    """ combinations with repetition"""
    fooc = lambda lst, k: [[]] if not k else [[lst[num]] + item for num in xrange(len(lst))
                                                            for item in fooc(lst[num:], k-1)] 
    return fooc(alist, kk)

def boolean(alist):
    """ boolean - set of combinations"""
    return reduce(lambda res, x: [item + [x] for item in res] + res, alist,[[]])

def set_combinationsr(alist):
    """ set of combinations with repetition"""
    return reduce(lambda res, x: [item + xcnt for item in res
                                  for xcnt in [[x]*cnt for cnt in xrange(1, len(alist)-len(item)+1)]] + res, alist,[[]])

if __name__ == "__main__":

    #ll = ["a", "b", "c", "d", "e", "f"]

    ll = [1,2,3]

    print boolean(ll)

    print len(permutations(ll,2)) 

    print len(permutationsr(ll,2))

    print len(combinations(ll,2))

    print len(combinationsr(ll,2))

    print set_combinationsr(ll)



