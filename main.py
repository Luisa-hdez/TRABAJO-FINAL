import csv
import os
import math
import random
import pandas as pd

from lib import create_carpet, create_filename, crear_archivo_excel, estudiantes_x_salon


#Cargar estudiantes
with open("./data.csv",newline="") as csvFileDirectory:
    csvFile = csv.reader(csvFileDirectory, delimiter="_", quotechar="_",lineterminator="\n")
    
# Crear las carpetas por semestre
os.mkdir("TrabajoFinal")
for i in range(0,10):
    os.mkdir("TrabajoFinal/Semestre_%s" % str(i+1))

#Cargar malla curricular
asignaturas = []
with open("./malla.csv",newline="") as csvFileDirectory:
    csvFile = csv.reader(csvFileDirectory, delimiter=",", quotechar='"', lineterminator="\n")

    for materia in csvFile:
        asignaturas.append(materia)


#Delimitamos Salon Asignatura x Nivel De Semestre
cupoPorSemestre = [
    {"Semestre": 1, "Cupos": 40},
    {"Semestre": 2, "Cupos": 40},
    {"Semestre": 3, "Cupos": 40},
    {"Semestre": 4, "Cupos": 35},
    {"Semestre": 5, "Cupos": 35},
    {"Semestre": 6, "Cupos": 35},
    {"Semestre": 7, "Cupos": 25},
    {"Semestre": 8, "Cupos": 25},
    {"Semestre": 9, "Cupos": 25},
    {"Semestre": 10, "Cupos": 10}
]

#Crear Carpetas x Asignatura
estudiantes = 1000
codigos = []
nte = []
cc = []
fileNames = []


for materia in asignaturas:
    semestre = int(materia[1])
    estudiantes_x_salon(materia,estudiantes * (0.7 ** (semestre-1)), cupoPorSemestre[semestre-1]["Cupos"])
