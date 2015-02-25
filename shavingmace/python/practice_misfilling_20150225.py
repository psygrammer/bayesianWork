import sys
from thinkbayes import Pmf

pmf=Pmf()
pmf.Set('M',0.6)
pmf.Set('L',0.3)
pmf.Set('C',0.1)


pmf.Mult('M', 0.003)
pmf.Mult('L', 0.007)
pmf.Mult('C', 0.010)

pmf.Normalize()

print "The probability of Moe is " + str(pmf.Prob('M'))
print "The probability of Larry is " + str(pmf.Prob('L'))
print "The probability of Curly is " + str(pmf.Prob('C'))


pmf.Mult('M', 0.003)
pmf.Mult('L', 0.007)
pmf.Mult('C', 0.010)

pmf.Normalize()

print "The probability of Moe is " + str(pmf.Prob('M'))
print "The probability of Larry is " + str(pmf.Prob('L'))
print "The probability of Curly is " + str(pmf.Prob('C'))


