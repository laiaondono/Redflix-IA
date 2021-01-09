import os
import random

def generar_basico():
	file = open("problema_basico.pddl", "w")
	file.write("(define (problem problemaPlanificador)\n\t(:domain dominioPlanificador)\n\n\t(:objects \n\t\t")
	nContenidos = random.randint(5,10)
	nDias = random.randint(nContenidos,nContenidos*2)
	for i in range(1, nContenidos+1):
		file.write("c"+str(i)+" ")
	file.write("- contenido\n\t\t")
	for i in range(1, nDias+1):
		file.write("dia"+str(i)+" ")
	file.write("- dia\n\t)\n\n\t(:init\n\t\t")
	nPredecesores = random.randint(2, int(nContenidos/2))
	i = 1
	j = nPredecesores
	while j != 0:
		file.write("(predecesor c"+str(i)+" c"+str(i+1)+")\n\t\t")
		i = i+2
		j = j-1
	file.write("(visto c1)\n")
	i = 2
	j = nPredecesores
	pendientes = []
	while j != 0:
		file.write("\t\t(pendiente c"+str(i)+")\n")
		pendientes.append("c"+str(i))
		i = i+2
		j = j-1
	i = i-1
	while i <= nContenidos:
		file.write("\t\t(pendiente c"+str(i)+")\n")
		pendientes.append("c"+str(i))
		i = i+1
	file.write("\t)\n\n\t(:goal (and")
	for p in pendientes:
		file.write(" (asignado "+p+")")
	file.write(")\n\t)\n)")
	file.close()

def generar_ext1():
	file = open("problema_ext1.pddl", "w")
	file.write("(define (problem problemaPlanificador)\n\t(:domain dominioPlanificador)\n\n\t(:objects \n\t\t")
	nContenidos = random.randint(6,12)
	nDias = random.randint(nContenidos,nContenidos*2)
	for i in range(1, nContenidos+1):
		file.write("c"+str(i)+" ")
	file.write("- contenido\n\t\t")
	for i in range(1, nDias+1):
		file.write("dia"+str(i)+" ")
	file.write("- dia\n\t)\n\n\t(:init\n\t\t")
	nPredecesores = random.randint(2, int(nContenidos/3))
	i = 1
	j = nPredecesores
	while j != 0:
		file.write("(predecesor c"+str(i)+" c"+str(i+1)+")\n\t\t(predecesor c"+str(i+1)+" c"+str(i+2)+")\n\t\t")
		i = i+3
		j = j-1
	file.write("(visto c1)\n")
	i = 3
	j = nPredecesores
	pendientes = []
	while j != 0:
		file.write("\t\t(pendiente c"+str(i)+")\n")
		pendientes.append("c"+str(i))
		i = i+3
		j = j-1
	i = i-2
	while i <= nContenidos:
		file.write("\t\t(pendiente c"+str(i)+")\n")
		pendientes.append("c"+str(i))
		i = i+1
	file.write("\t)\n\n\t(:goal (and")
	for p in pendientes:
		file.write(" (asignado "+p+")")
	file.write(")\n\t)\n)")
	file.close()

def generar_ext2():
	file = open("problema_ext2.pddl", "w")
	file.write("(define (problem problemaPlanificador)\n\t(:domain dominioPlanificador)\n\n\t(:objects \n\t\t")
	nContenidos = random.randint(6,12)
	nDias = random.randint(nContenidos,nContenidos*2)
	for i in range(1, nContenidos+1):
		file.write("c"+str(i)+" ")
	file.write("- contenido\n\t\t")
	for i in range(1, nDias+1):
		file.write("dia"+str(i)+" ")
	file.write("- dia\n\t)\n\n\t(:init\n\t\t")
	nPredecesores = random.randint(2, int(nContenidos/3))
	i = 1
	j = nPredecesores
	while j != 0:
		file.write("(predecesor c"+str(i)+" c"+str(i+1)+")\n\t\t(predecesor c"+str(i+1)+" c"+str(i+2)+")\n\t\t")
		i = i+3
		j = j-1
	file.write("(paralelo c3 c4)\n")
	if nPredecesores > 2:
		file.write("\t\t(paralelo c6 c7)\n")
	file.write("\t\t(visto c1)\n")
	i = 3
	j = nPredecesores
	pendientes = []
	while j != 0:
		file.write("\t\t(pendiente c"+str(i)+")\n")
		pendientes.append("c"+str(i))
		i = i+3
		j = j-1
	i = i-2
	while i <= nContenidos:
		file.write("\t\t(pendiente c"+str(i)+")\n")
		pendientes.append("c"+str(i))
		i = i+1
	file.write("\t)\n\n\t(:goal (and")
	for p in pendientes:
		file.write(" (asignado "+p+")")
	file.write(")\n\t)\n)")
	file.close()

def generar_ext3():
	file = open("problema_ext3.pddl", "w")
	file.write("(define (problem problemaPlanificador)\n\t(:domain dominioPlanificador)\n\n\t(:objects \n\t\t")
	nContenidos = random.randint(6,12)
	nDias = random.randint(nContenidos,nContenidos*2)
	for i in range(1, nContenidos+1):
		file.write("c"+str(i)+" ")
	file.write("- contenido\n\t\t")
	for i in range(1, nDias+1):
		file.write("dia"+str(i)+" ")
	file.write("- dia\n\t)\n\n\t(:init\n\t\t")
	nPredecesores = random.randint(2, int(nContenidos/3))
	i = 1
	j = nPredecesores
	while j != 0:
		file.write("(predecesor c"+str(i)+" c"+str(i+1)+")\n\t\t(predecesor c"+str(i+1)+" c"+str(i+2)+")\n\t\t")
		i = i+3
		j = j-1
	file.write("(paralelo c3 c4)\n")
	if nPredecesores > 2:
		file.write("\t\t(paralelo c6 c7)\n")
	file.write("\t\t(visto c1)\n")
	i = 3
	j = nPredecesores
	pendientes = []
	while j != 0:
		file.write("\t\t(pendiente c"+str(i)+")\n")
		pendientes.append("c"+str(i))
		i = i+3
		j = j-1
	i = i-2
	while i <= nContenidos:
		file.write("\t\t(pendiente c"+str(i)+")\n")
		pendientes.append("c"+str(i))
		i = i+1
	for i in range(1, nDias):
		file.write("\t\t(dia_siguiente dia"+str(i)+" dia"+str(i+1)+")\n")
	for i in range(1, nDias+1):
		file.write("\t\t(= (numAsignaciones dia"+str(i)+") 0)\n")
	file.write("\t)\n\n\t(:goal (and")
	for p in pendientes:
		file.write(" (asignado "+p+")")
	file.write(")\n\t)\n)")
	file.close()

def generar_ext4():
	file = open("problema_ext4.pddl", "w")
	file.write("(define (problem problemaPlanificador)\n\t(:domain dominioPlanificador)\n\n\t(:objects \n\t\t")
	nContenidos = random.randint(6,12)
	nDias = random.randint(nContenidos,nContenidos*2)
	for i in range(1, nContenidos+1):
		file.write("c"+str(i)+" ")
	file.write("- contenido\n\t\t")
	for i in range(1, nDias+1):
		file.write("dia"+str(i)+" ")
	file.write("- dia\n\t)\n\n\t(:init\n")
	for i in range(1, nContenidos+1):
		file.write("\t\t(= (duracion c"+str(i)+") "+str(random.randint(20, 130))+")\n")
	nPredecesores = random.randint(2, int(nContenidos/3))
	i = 1
	j = nPredecesores
	while j != 0:
		file.write("\t\t(predecesor c"+str(i)+" c"+str(i+1)+")\n\t\t(predecesor c"+str(i+1)+" c"+str(i+2)+")\n")
		i = i+3
		j = j-1
	file.write("\t\t(paralelo c3 c4)\n")
	if nPredecesores > 2:
		file.write("\t\t(paralelo c6 c7)\n")
	file.write("\t\t(visto c1)\n")
	i = 3
	j = nPredecesores
	pendientes = []
	while j != 0:
		file.write("\t\t(pendiente c"+str(i)+")\n")
		pendientes.append("c"+str(i))
		i = i+3
		j = j-1
	i = i-2
	while i <= nContenidos:
		file.write("\t\t(pendiente c"+str(i)+")\n")
		pendientes.append("c"+str(i))
		i = i+1
	for i in range(1, nDias):
		file.write("\t\t(dia_siguiente dia"+str(i)+" dia"+str(i+1)+")\n")
	for i in range(1, nDias+1):
		file.write("\t\t(= (numDia dia"+str(i)+") "+str(i)+")\n")
	for i in range(1, nDias+1):
		file.write("\t\t(= (duracionDiaria dia"+str(i)+") 0)\n")
	file.write("\t)\n\n\t(:goal (and")
	for p in pendientes:
		file.write(" (asignado "+p+")")
	file.write(")\n\t)\n)")
	file.close()


def main():
	print("¿Qué acción quiere realizar?\n",
		  "[0] Generar problema para extensión básica\n",
		  "[1] Generar problema para extensión 1\n",
		  "[2] Generar problema para extensión 2\n",
		  "[3] Generar problema para extensión 3\n",
		  "[4] Generar problema para extensión 4\n",
		  "[-1] Salir\n")

	op = input("Introduce un número:")
	op = int(op)

	while op != -1:
		if op == 0:
			generar_basico()

		elif op == 1:
			generar_ext1()

		elif op == 2:
			generar_ext2()

		elif op == 3:
			generar_ext3()

		elif op == 4:
			generar_ext4()

		elif op == -1:
			break

		print("¡El fichero ha sido creado satisfactoriamente!\n\n"
			"¿Qué acción quiere realizar?\n",
			  "[0] Generar problema para extensión básica\n",
			  "[1] Generar problema para extensión 1\n",
			  "[2] Generar problema para extensión 2\n",
			  "[3] Generar problema para extensión 3\n",
			  "[4] Generar problema para extensión 4\n",
			  "[-1] Salir\n")

		op = input("Introduce un número:")
		op = int(op)


main()