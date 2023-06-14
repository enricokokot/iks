### works as intended

import asyncio
import matplotlib.pyplot as plt
from random import random, expovariate

def kreiraj_pid():
    i = 0
    while True:
        yield i
        i += 1

gen = kreiraj_pid()

async def otvori_proces():
    global trenutni_procesi
    imena = ["Balan", "Calan", "Dalan"]
    pid = next(gen)

    for ime in imena:
        await loop.create_task(stvori_objekt(pid, ime))
    trenutni_procesi.pop()
    
async def stvori_objekt(pid, ime):
    kasnjenje = random()
    await asyncio.sleep(kasnjenje)
    return Objekt(pid, ime, kasnjenje)

class Objekt:
    def __init__(self, pid, ime, kasnjenje):
        print(f"Objekt {ime} je kreiran, PID={pid} kasnjenje {kasnjenje*1000:.2f} ms")

async def simulator_ulaza(vrijeme_medudolazaka):
    global trenutni_procesi, counter

    #!
    delta = counter * expovariate(1/2)

    broj_procesa = 500
    procesi = []

    for i in range(broj_procesa):
        procesi.append(loop.create_task(otvori_proces()))
        trenutni_procesi.append("*")
        await asyncio.sleep(counter * expovariate(1/2))

        #!
        counter = counter - 0.0001875

    await asyncio.wait(procesi)

async def vrati_vrijednost_varijable(varijabla, interval):
    global counter

    procs = []
    # TODO

    for i in range(150):
        broj_trenutnih_procesa = len(varijabla)
        print("broj_trenutnih_procesa: ", broj_trenutnih_procesa)
        
        #!
        procs.append(broj_trenutnih_procesa)

        await asyncio.sleep(interval)
    
    plt.plot(procs)
    plt.show()

trenutni_procesi = []

#!
counter = 0.1

loop = asyncio.get_event_loop()
zadace = asyncio.gather(simulator_ulaza(1000), vrati_vrijednost_varijable(trenutni_procesi, 0.5))
loop.run_until_complete(zadace)