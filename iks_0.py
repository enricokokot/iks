import asyncio
from random import expovariate
import matplotlib.pyplot as plt

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
    # kasnjenje = random()
    kasnjenje = expovariate(0.5)
    await asyncio.sleep(kasnjenje)
    return Objekt(pid, ime, kasnjenje)

class Objekt:
    def __init__(self, pid, ime, kasnjenje):
        print(f"Objekt {ime} je kreiran, PID={pid} kasnjenje {kasnjenje*1000:.2f} ms")

async def simulator_ulaza(broj_procesa):
    procesi = []
    counter = 0.1

    for _ in range(broj_procesa):
        procesi.append(loop.create_task(otvori_proces()))
        if counter < 0:
            counter = 0
        elif counter > 0: counter = counter - 0.0001875
        await asyncio.sleep(counter*expovariate(0.5))

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
    plt.show()

trenutni_procesi = []

loop = asyncio.get_event_loop()
zadace = asyncio.gather(simulator_ulaza(1000), vrati_vrijednost_varijable(trenutni_procesi, 0.1))
loop.run_until_complete(zadace)