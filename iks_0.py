import asyncio
from random import random

def kreiraj_pid():
    # for i in range(10):
    #     yield i¸
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

    # for i in 10:
    #     loop.create_task(otvori_proces())

    proces_1 =  loop.create_task(otvori_proces())
    await asyncio.sleep(delta)
    proces_2 =  loop.create_task(otvori_proces())
    await asyncio.sleep(delta)
    proces_3 =  loop.create_task(otvori_proces())

    await asyncio.wait([proces_1, proces_2, proces_3])

loop = asyncio.get_event_loop()
loop.run_until_complete(simulator_ulaza(1000))