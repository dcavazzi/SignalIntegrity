class ErrorTerms(object):
...
    def DutCalculation(self,sRaw,pl=None):
        if pl is None: pl = [p for p in range(len(sRaw))]
        B=[[(sRaw[r][c]-self[pl[r]][pl[c]][0])/self[pl[r]][pl[c]][1]
            for c in range(len(sRaw))] for r in  range(len(sRaw))]
        A=[[B[r][c]*self[pl[r]][pl[c]][2]+(1 if r==c else 0) for c in range(len(sRaw))]
           for r in range(len(sRaw))]
        S=(matrix(B)*matrix(A).getI()).tolist()
        return S
    def DutUnCalculation(self,S,pl=None):
        if pl is None: pl = [p for p in range(len(S))]
        Sp=[[None for c in range(len(S))] for r in range(len(S))]
        Si=matrix(S).getI()
        for c in range(len(S)):
            E=self.Fixture(c,pl)
            Em=[[matrix(E[0][0]),matrix(E[0][1])],[matrix(E[1][0]),matrix(E[1][1])]]
            col=(Em[0][0]*Em[1][0]+Em[0][1]*(Si-Em[1][1]).getI()*Em[1][0]).tolist()
            for r in range(len(S)): Sp[r][c]=col[r][c]
        return Sp
...