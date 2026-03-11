class interest:
    def __init__(self,p,r,t): #constructur
        self.p = p
        self.r = r
        self.t = t

    def show(self):
        si = (self.p * self.r * self.t) / 100
        print("principal =", self.p)
        print("rate =", self.r)
        print("time =", self.t)
        print("simple interest =", si)


s1 = interest(1000,5,2)
s1.show()