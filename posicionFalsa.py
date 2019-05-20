import pandas, math, sympy
from sympy import cos, sin, tan, acos, atan, asin
from numpy import inf, nan, sqrt, power

class Data():
    limS=0.0
    limI=0.0
    equation=""
    def inputData(self):
        self.limS = float(input("Ingrese limite superior "))
        self.limI = float(input("Ingrese limite inferior "))
        self.equation = str(input("Ingrese ecuación "))

    def makeTable(self):
        Xi=[]
        XFi = []#tabla 1
        listP0 = []
        listP1 = []
        listFP0 = []#tabla 2
        listFP1 = []#tabla 2
        b = 0
        while b<51:
            listP0 = listP0 + [round(self.limI, 7)]
            #listP0 = eval(listP0)
            listP1 = listP1 + [round(self.limS, 7)]
            #listP1 = eval(listP1)
            listFP0 = listFP0 + [round(eval(str(self.equation.replace("x", str(listP0[b])))), 7)]
            #listP0 = eval(listFP0)
            listFP1 = listFP1 + [round(eval(str(self.equation.replace("x", str(listP1[b])))), 7)]
            #listFP1 = eval(listFP1)
            equationXi = (listP0[b] * listFP1[b] - listP1[b] * listFP0[b]) / (listFP1[b] - listFP0[b])
            round(equationXi, 7)
            Xi = Xi + [equationXi]
            XFi = XFi + [round(eval(str(self.equation.replace("x", str(Xi[b])))), 7)]

            if listFP0[b] * XFi[b] > 0:
                self.limI = Xi[b]
            elif listFP0[b] * XFi[b] < 0:
                self.limS = Xi[b]
            b=b+1

        table2 = pandas.DataFrame([listP0, listFP0, listP1, listFP1, Xi, XFi])
        table2 = table2.T
        table2.columns = ["P0", "FP0", "P1", "FP1", "Xi", "XFi"]
        #print(table1)
        print(table2)
ob=Data()
ob.inputData()
ob.makeTable()

""""try:
    # resultado de limiteInferior
    equationLimI = eval(self.equation.replace("x", str(listP0[b])))
    equationLimI = round(equationLimI, 7)

    # resultado de limiteSuperior
    equationLimSup = eval(self.equation.replace("x", str(listP1[b])))
    equationLimSup = round(equationLimSup, 7)

    # equationToPn = listP1[b]-(listFP1[b]*((listP1[b]-listP0[b])/(listFP1[b]-listFP0[b])))

    listFP0 = listFP0 + [equationLimI]  # agrego la iteración a la 2a tabla
    listFP1 = listFP1 + [equationLimSup]  # agrego la iteración a la 2a tabla

    equationToPn = equationLimSup - (listFP1[b] * ((equationLimSup - equationLimI) / (listFP1[b] - listFP0[b])))
    equationToPn = round(equationToPn, 7)

    listPn = listPn + [equationToPn]  # sustituyo los valores con la ecuación
    listFPn = listFPn + [eval(self.equation.replace("x", str(equationToPn)))]
    if listP0[b] * listFP1[b] < 0:
        listP0 = listP0 + [listP1[b]]
        listP1 = listP1 + [equationToPn]
    elif listP0[b] * listFP1[b] > 0:
        listP0 = listP0 + [equationLimI]
        listP1 = listP1 + [equationToPn]
    b = b + 1

except ZeroDivisionError:
    print("División de cero")
    b = b + 1"""""