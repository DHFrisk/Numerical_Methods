import numpy, pandas
from sympy import cos, sin, tan, acos, atan, asin
from numpy import inf, nan, sqrt, power
#si el producto de Li*Prom > 0 se cambia el Ls por el promedio, sino se cambia el Li por el promedio
class Data:
    equation=""
    limS=0.0
    limI=0.0

    def inputData(self):
        self.limS = float(input("Ingrese el limite superior\t"))
        self.limI = float(input("Ingrese el limite inferior\t"))
        self.equation = str(input("Ingrese la ecuación\t"))

    def makeTable(self):
        prom=0.0
        dataVector=[]
        dataVector1=[]
        dataVector2=[]
        dataVector3=[]
        #counter=self.limI
        b=0
        while b<51:
            prom=(self.limS+self.limI)/2
            dataVector = dataVector + [self.limI]
            dataVector1 = dataVector1 + [self.limS]
            dataVector2 = dataVector2 + [prom]
            equation2 = self.equation.replace("x", str(prom))
            equation2 = eval(str(equation2))
            round(equation2, 7)
            dataVector3 = dataVector3 + [equation2]
            if equation2 * self.limI < 0:
                self.limI=prom
            else:
                self.limS=prom
            b=b+1
        dataTable=pandas.DataFrame([dataVector, dataVector1, dataVector2, dataVector3])
        dataTable2=dataTable.T
        dataTable2.columns=["Limite Inferior", "Limite Superior", "Promedio", "F(x)"]
        print(dataTable2)



data = Data();
data.inputData()
data.makeTable()