###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
for i in range(2, 21, 2):
    print(i)

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
suma = 0
for i in numeros:
    suma +=i
print(suma/5)

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
max = numeros[0]
for i in numeros[1:]:
    if i>max:
        max = i
print(max)

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "llunatic"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
llarg = [paraula for paraula in paraules if len(paraula) > 5]
print(llarg)

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
lletra = input("Insereix una lletra: ").lower()
i=0
for paraula in paraules:
    if paraula.lower().startswith(lletra):
        i+=1
print(f"Coincideixen {i} paraules que comencen amb la lletra {lletra}")

# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
tensions = [4.8, 5.0, 5.3, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.
sum = 0
for i in tensions:
    sum +=i
print(f"La mitjana es: {sum/len(tensions)}")

# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.
corrent = [round(12/r, 2) for r in resistencies]
print(corrent)

# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
nivells_soroll = [-92, -6, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.
sup = 0
for i in nivells_soroll:
    if i > -80:
        sup += 1
print(sup)

# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts =     [1, 1, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).
dif = 0;
for i in range(len(bits_transmesos)):
    if bits_transmesos[i] != bits_rebuts[i]:
        dif+=1
error = round(dif / len(bits_transmesos), 2)
print(f"Hi ha hagut {dif} bits diferents i la taxa d'error es {error}")

# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.
for f in frequencies:
    period = round(1/f, 3)
    print(f"Frecuencia: {f}Hz, Periode: {period}s")
