# -*- coding: utf-8 -*-
from thinkbayes import Pmf


class MisFiler(Pmf):

    def __init__(self, hypos):
        Pmf.__init__(self)

        for who, prob in hypos.iteritems():
            self.Set(who, prob)
        self.Normalize()

    def Update(self, data):
        self.Likelihood(data)
        self.Normalize()

    def Likelihood(self, data):
        for who, prob in data.iteritems():
            self.Mult(who, prob)


def main():
    hypos = {"M": 0.6,
             "L": 0.3,
             "C": 0.1}

    pmf = MisFiler(hypos)

    data = {"M": 0.003,
            "L": 0.007,
            "C": 0.01}

    pmf.Update(data)

    for who, prob in pmf.Items():
        print who, prob

    print pmf.MaximumLikelihood()


if __name__ == '__main__':
    main()
