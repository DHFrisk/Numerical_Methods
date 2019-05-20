#se intercambia f(x) por x, y luego se despeja f(x) y luego f(x) se convierte a x
#y con eso ya se empieza a trabajar
import pandas
from sympy import cos, sin, tan, acos, atan, asin
from numpy import inf, nan, sqrt, power
class Data():
    secondEq=""
    x=0.0
    def inputData(self):
        self.secondEq=str(input("Ingrese la ecuación despejada "))
        self.x=float(input("Ingrese valor "))
    def data(self):
        listX=[self.x]
        listResult=[]
        b=0
        while b<51:
            ssEqq=eval(str(self.secondEq.replace("x", str(listX[b]))))
            round(ssEqq, 7)
            listResult=listResult+[ssEqq]
            listX=listX+[listResult[b]]
            b=b+1
        table1=pandas.DataFrame([listX, listResult])
        table1=table1.T
        table1.columns=["X", "Resultado"]
        print(table1)

d=Data()
d.inputData()
d.data()