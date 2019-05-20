import numpy
import sympy

class lagrange:
	def __init__(self):
		range = int("Ingrese el largo de la tabla")
		rangeX = []
		rangeY = []
		for i in range:
			temporalX = float("Ingrese X en la posición: ",i)
			rangeX.append(temporalX)
			temporalY