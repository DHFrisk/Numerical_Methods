import numpy, pandas, math, sympy
from sympy import cos, sin, tan, acos, atan, asin
from numpy import inf, nan, sqrt, power

class Data():
    eq=""
    eqD=""
    value=0.0

    def inputData(self):
        self.eq=str(input("Ingrese ecuacion "))
        self.eqD=sympy.diff(self.eq, sympy.Symbol("x")).doit()
        self.value=float(input("Ingrese valor "))
    def makeTable(self):
        listEq=[self.eq]
        listEqD=[self.eqD]
        listValue = [self.value]
        b=0
        while b<51:
            try:
                replacedEquation=eval(self.eq.replace("x", str(listValue[b])))
                replacedDifferential=self.eqD.replace("x", str(listValue[b]))
                newValue=listValue[b]-(replacedEquation/replacedDifferential)
                listValue=listValue+[newValue]
                listEq=listEq+[replacedEquation]
                listEqD=listEqD+[replacedDifferential]
            except IndexError:
                print("Index Error")
            b=b+1
        #print(listEquation, listDerivated, listValue)
        table1=pandas.DataFrame([listValue, listEq, listEqD])
        table1=table1.T
        table1.columns=["Valor", "Ecuación", "Ecuación Derivada"]
        print(table1)


ob=Data()
ob.inputData()
ob.makeTable()