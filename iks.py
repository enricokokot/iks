import asyncio
import random
import matplotlib.pyplot as plt
import numpy as np
# import nest_asyncio
# nest_asyncio.apply()

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
        avg_process[pid].append(kasnjenje)

async def simulator_ulaza(vrijeme_medudolazaka):
    global numberOfIDS, counter, procesi, broj_procesa
    #delta = 0.1 * random.expovariate(1/2) ####vrijeme_medudolazaka / 1
    for i in range (broj_procesa):
        delta = counter * random.expovariate(1/2)
        medudolasci.append(delta)
        proces =  loop.create_task(otvori_proces())
        await asyncio.sleep(delta)
        i += 1
        counter = counter - 0.0001875
        procesi.append(proces)
        numberOfIDS = len(procesi)
        print(i)
        listOfIDNumbers.append(numberOfIDS)
        
    await asyncio.wait(procesi)

#if __name__ == "__main__":
broj_procesa = 100
numberOfIDS = 0
listOfIDNumbers = []
procesi = []
time = list(range(2 * broj_procesa))
medudolasci = []
#avg_process = {0: [], 1: [], 2: []}
avg_process = dict(zip(list(range(100)), [[] for x in range(100)]))
counter = 0.1
loop = asyncio.get_event_loop()
loop.run_until_complete(simulator_ulaza(0.01))
print(numberOfIDS)

# print(avg_process)
print([sum(v) for (k,v) in avg_process.items()])
print(f"prosječno vrijeme procesiranja: {np.average([sum(v) for (k,v) in avg_process.items()])}")
print(f"prosječno vrijeme međudolazaka: " + str(np.average(medudolasci)))
print(f"prosječni broj procesa u sustavu: {np.average(listOfIDNumbers)}")

plt.plot([np.average(listOfIDNumbers) for proces in time])
plt.plot(listOfIDNumbers)
plt.show()

plt.plot([np.average(medudolasci) for proces in time[:broj_procesa]])
plt.plot(medudolasci)
plt.show()

plt.plot([np.average([sum(v) for (k,v) in avg_process.items()]) for proces in time[:broj_procesa]])
plt.plot([sum(v) for (k,v) in avg_process.items()])
plt.show()
