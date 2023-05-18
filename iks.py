import asyncio
import random
import matplotlib.pyplot as plt
import nest_asyncio
nest_asyncio.apply()

def kreiraj_pid():
    for i in range(100000):
        yield i

gen = kreiraj_pid()

async def otvori_proces():
    global numberOfIDS, procesi, listOfIDNumbers
    imena = ["Balan", "Calan", "Dalan"]
    pid = next(gen)

    for ime in imena:
        await loop.create_task(stvori_objekt(pid, ime))
    procesi.pop()
    numberOfIDS = len(procesi)
    listOfIDNumbers.append(numberOfIDS)
    
    
async def stvori_objekt(pid, ime):
    kasnjenje = 0.1 * random.expovariate(1/2)
    await asyncio.sleep(kasnjenje)
    return Objekt(pid, ime, kasnjenje)

class Objekt:
    def __init__(self, pid, ime, kasnjenje):
        print(f"Objekt {ime} je kreiran, PID={pid} kasnjenje {kasnjenje*1000:.2f} ms")

async def simulator_ulaza(vrijeme_medudolazaka):
    global numberOfIDS, procesi
    #delta = 0.1 * random.expovariate(1/2) ####vrijeme_medudolazaka / 1
    broj_procesa = 500000
    for i in range (broj_procesa):
        proces =  loop.create_task(otvori_proces())
        await asyncio.sleep(0.1 * random.expovariate(1/2))
        i += 1
        procesi.append(proces)
        numberOfIDS = len(procesi)
        print(i)
        listOfIDNumbers.append(numberOfIDS)
        
    await asyncio.wait(procesi)

#if __name__ == "__main__":
numberOfIDS = 0
listOfIDNumbers = []
procesi = []
loop = asyncio.get_event_loop()
loop.run_until_complete(simulator_ulaza(0.01))
print(numberOfIDS)
plt.plot(listOfIDNumbers)
plt.show()