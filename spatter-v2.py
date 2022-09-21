#!/usr/bin/env python3

class AbstractPattern(object):
    def __init__(self):
        raise NotImplementedError()

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        raise NotImplementedError()

    def reset(self):
        self.cur = 0

class UniformPattern(AbstractPattern):
    def __init__(self,n,delta):
        self.n = n
        self.delta = delta
        self.cur = 0

    def next(self):
        if self.cur < self.n:
            val = self.delta*self.cur
            self.cur += 1
            return val
        raise StopIteration()

class ExplicitPattern(AbstractPattern):
    def __init__(self, pattern):
        self.pattern = pattern.copy()
        self.cur = 0
    def next(self):
        if self.cur < len(self.pattern):
            val = self.pattern[self.cur]
            self.cur += 1
            return val
        raise StopIteration()

#class PointerChase(AbstractPattern):
#    def __init__(self, pattern, data, base):
#        self.pattern # pattern should be an AbstractPattern
#        self.cur = 0
#
#    def next(self):

#base = 0
#for i in UniformPattern(2, 16):
#    base = base + i
#    for j in UniformPattern(8, 2):
#        print(base + j)
#    print('-')


## Good section ##
#base = 1
#for i in UniformPattern(2, 3):
#    base += i
#    for j in UniformPattern(2, 1):
#        base += j
#        for k in ExplicitPattern([0, 3, 4, 5, 8]):
#            print(base + k)
#        print('-')

def recurse(pats, base):

    if len(pats) > 1:
        for i in pats[0]:
            base += i
            base = recurse(pats[1:], base)
            pats[1].reset()

    else:
        for i in pats[0]:
            print(base + i)
        print('-')

    return base

Pat3D = [UniformPattern(2, 3), UniformPattern(2, 1), ExplicitPattern([0, 3, 4, 5, 8])]

recurse(Pat3D, 1)

#for P in Pat3D:

