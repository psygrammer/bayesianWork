import sys


def calculate(ll,prob_smoke):
    prob_smoke = float(prob_smoke)    
    prob = float(ll*prob_smoke)/(ll*prob_smoke+1-prob_smoke)
    return prob


def main():
    ll = sys.argv[1]
    prob_smoke = sys.argv[2]
    print "%.2f" % calculate(prob_smoke)


if __name__ == "__main__":
    main()
