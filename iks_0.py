import asyncio
from random import random

def kreiraj_pid():
    i = 0
    while True:
        yield i
        i += 1

gen = kreiraj_pid()

async def otvori_proces():
    imena = ["Balan", "Calan", "Dalan"]
    pid = next(gen)

    for ime in imena:
        await loop.create_task(stvori_objekt(pid, ime))
    
async def stvori_objekt(pid, ime):
    kasnjenje = random()
    await asyncio.sleep(kasnjenje)
    return Objekt(pid, ime, kasnjenje)

class Objekt:
    def __init__(self, pid, ime, kasnjenje):
        print(f"Objekt {ime} je kreiran, PID={pid} kasnjenje {kasnjenje*1000:.2f} ms")

async def simulator_ulaza(vrijeme_medudolazaka):
    delta = vrijeme_medudolazaka / 1000
    broj_procesa = 100
    procesi = []

    for i in range(broj_procesa):
        procesi.append(loop.create_task(otvori_proces()))
        await asyncio.sleep(delta)

    await asyncio.wait(procesi)

loop = asyncio.get_event_loop()
loop.run_until_complete(simulator_ulaza(1000))