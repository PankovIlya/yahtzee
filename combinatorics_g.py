# -*- coding: utf-8 -*-
import math

def combinations(lst, k):
    """ combinations """
    if not k:
        yield []
    else:
        for idx in xrange(len(lst)):
            for item in combinations(lst[idx+1:], k-1):
                yield [lst[idx]] + item 

def combinationsr(lst, k):
    """ combinations with repetition"""
    if not k:
        yield []
    else:
        for idx in xrange(len(lst)):
            for item in combinationsr(lst[idx:], k-1):
                yield [lst[idx]] + item

def permutationsr(lst, k):
    """ permutation with repetition"""
    if not k:
        yield []
    else:
        for x in lst:
            for item in combinations(lst, k-1):
                yield [x] + item 

def permutations(lst, k):
    """ permutation with repetition"""
    if not k:
        yield []
    else:
        for idx in xrange(len(lst)):
            for item in permutations(lst[:idx] + lst[idx+1:], k-1):
                yield [lst[idx]] + item 

def boolean(lst):
    """ combinations """
    if not lst:
        yield []
    else:
        for item in boolean(lst[1:]):
            yield [lst[0]] + item
            yield item
                

if __name__ == "__main__":

    #ll = ["a", "b", "c", "d", "e", "f"]

    ll = [1,2,3,4]
    k = 2
    n = len(ll)
    f = math.factorial

    def check(gen):
        cnt = 0
        for _ in gen:
            cnt += 1
        return cnt

    assert(check(boolean(ll)) == 2**n)
    assert(check(combinations(ll,k)) == f(n)/(f(k)*f(n-k)))
    assert(check(combinationsr(ll,k)) == f(n+k-1)/(f(k)*f(n-1)))
    assert(check(permutations(ll,k)) == f(n)/f(n - k))
    assert(check(permutationsr(ll,k)) == n**k)
    print len(set_combinationsr(ll))



