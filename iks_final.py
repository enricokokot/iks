import asyncio
from random import expovariate
import matplotlib.pyplot as plt
import numpy as np

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

    trenutni_procesi.append("*")
    for ime in imena:
        await loop.create_task(stvori_objekt(pid, ime))
    trenutni_procesi.pop()
    
async def stvori_objekt(pid, ime):
    kasnjenje = expovariate(0.5)
    await asyncio.sleep(kasnjenje)
    return Objekt(pid, ime, kasnjenje)

class Objekt:
    def __init__(self, pid, ime, kasnjenje):
        print(f"Objekt {ime} je kreiran, PID={pid} kasnjenje {kasnjenje*1000:.2f} ms")
        avg_process[pid].append(kasnjenje)

async def simulator_ulaza(broj_procesa):
    procesi = []
    counter = 0.1

    for _ in range(broj_procesa):
        procesi.append(loop.create_task(otvori_proces()))
        if counter < 0:
            counter = 0
        elif counter > 0: counter = counter - 0.0001875
        delta = counter*expovariate(0.5)
        medudolasci.append(delta)
        await asyncio.sleep(delta)

    await asyncio.wait(procesi)

async def vrati_vrijednost_varijable(varijabla, interval):
    broj_aktivnih_procesa_u_vremenu = [] 
    counter = 0

    while counter < 2/interval:
        broj_trenutnih_procesa = len(varijabla)
        if broj_trenutnih_procesa == 0:
            counter += 1
        if broj_trenutnih_procesa > 0:
            counter = 0
        broj_aktivnih_procesa_u_vremenu.append(broj_trenutnih_procesa)
        # print("broj_trenutnih_procesa: ", broj_trenutnih_procesa)
        await asyncio.sleep(interval)

    plt.plot(broj_aktivnih_procesa_u_vremenu)
    plt.plot([np.average(broj_aktivnih_procesa_u_vremenu) for broj in broj_aktivnih_procesa_u_vremenu])
    plt.title("Broj aktivnih procesa")
    plt.show()

broj_procesa = 1000
time = list(range(2 * broj_procesa))
trenutni_procesi = []
medudolasci = []

avg_process = dict(zip(list(range(broj_procesa)), [[] for x in range(broj_procesa)]))

loop = asyncio.get_event_loop()
zadace = asyncio.gather(simulator_ulaza(broj_procesa), vrati_vrijednost_varijable(trenutni_procesi, 0.1))
loop.run_until_complete(zadace)

plt.plot(medudolasci)
plt.plot([np.average(medudolasci) for proces in time[:broj_procesa]])
plt.title("Vrijeme međudolazaka")
plt.show()

plt.plot([sum(v) for (k,v) in avg_process.items()])
plt.plot([np.average([sum(v) for (k,v) in avg_process.items()]) for proces in time[:broj_procesa]])
plt.title("Vrijeme izvođenja pojedinog procesa")
plt.show()