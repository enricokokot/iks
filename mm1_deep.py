import math
from random import expovariate
import numpy as np
import matplotlib.pyplot as plt

def expr(lam):
    # return -math.log(np.random.uniform(0, 1) / lam)
    return expovariate(lam)

service = np.array(1000*[0], dtype=float)
# service = 100*[0]
for i in range(1000): service[i] = expr(0.5)

arrival = np.array(1000*[0], dtype=float)
time_between_arrivals = np.array(1000*[0], dtype=float)
# for i in range(1, 100): arrival[i] = arrival[i-1] + expr(0.5)
for i in range(1, 1000):
    value = expr(0.5)
    arrival[i] = arrival[i-1] + value
    time_between_arrivals[i] = value

# print(service)
print(np.average(service))
print(np.average(arrival))

# plt.hist(service, bins=10)
# plt.plot(arrival)
# plt.show()

enter_service_time, leave_service_time = np.array(1000*[0], dtype=float), np.array(1000*[0], dtype=float)
leave_service_time[0] = service[0]
for i in range(1, 1000):
    if leave_service_time[i-1] < arrival[i]: enter_service_time[i] = arrival[i]
    else: enter_service_time[i] = leave_service_time[i-1]
    leave_service_time[i] = enter_service_time[i] + service[i]

x = list(zip(enter_service_time, leave_service_time))

# print(x)

# plt.plot(x)
# plt.grid()
# plt.show()

waiting_time = leave_service_time - arrival
average_waiting_time = np.average(waiting_time)
# plt.plot(waiting_time)
# plt.show()

queue_time = enter_service_time - arrival
average_queue_time = np.average(queue_time)
# plt.plot(queue_time)
# plt.show()

# plt.bar(list(range(len(leave_service_time))), leave_service_time, color="#6f4e7c")
# plt.bar(list(range(len(enter_service_time))), enter_service_time, color="#f6c85f")
# plt.bar(list(range(len(arrival))), arrival, color="#0b84a5")
# # plt.legend()
# plt.show()

# print()
# ### veći lambda -> manji raspon od 0 do 100, 10, 3, itd.
# for lam in [0.1, 1/2, 1, 2]:
#     list = []
#     for num in range(100):
#         list.append(expovariate(lam))
#     print(np.max(list))
#     print(np.min(list))

# veća lambda -> manje korisnika u sustavu
print(0.1 * average_waiting_time)

plt.bar(list(range(len(leave_service_time))), leave_service_time-arrival, color="#6f4e7c")
plt.bar(list(range(len(enter_service_time))), enter_service_time-arrival, color="#f6c85f")
plt.show()

### BROJ PROCESA U MNOGIM TRENUCIMA / PROSJEČNI BROJ PROCESA U SVIM TRENUCIMA
# process_arrival_and_lst = list(zip(arrival, leave_service_time))
number_of_processes = []
stack = []
# for arr, lst in process_arrival_and_lst:
#     for value in stack:
#         if value < arr:
#             stack.remove(value)
#     stack.append(lst)
#     number_of_processes.append(len(stack))

# print(number_of_processes)
# print(np.average(number_of_processes))

# plt.plot(number_of_processes)
# plt.plot([np.average(number_of_processes)] * len(process_arrival_and_lst))
# plt.show()

# print(f"leave_service_time[:5]: {leave_service_time[:5]}")
# print(f"arrival[:5]: {arrival[:5]}")

lista_vremena = np.arange(0, 2200, 0.1)
print(f"lista_vremena: {lista_vremena}")
for trenutak in lista_vremena:
    for idx, dolazak in enumerate(arrival):
        if dolazak <= trenutak:
            arrival[idx] = 2500
            stack.append("*")
    for idx, odlazak in enumerate(leave_service_time):
        if odlazak <= trenutak:
            leave_service_time[idx] = 2500
            stack.pop()
    number_of_processes.append(len(stack))

plt.plot(number_of_processes)
# plt.bar(number_of_processes)
plt.plot([np.average(number_of_processes)] * len(number_of_processes))
plt.title("Number of processes at certain time")
plt.show()

### MEĐUDOLAZAK U SVAKOM TRENUTKU / PROSJEČNO VRIJEME MEĐUDOLAZAKA
plt.plot(time_between_arrivals)
plt.plot([np.average(time_between_arrivals)] * len(time_between_arrivals))
plt.title("Time of arrival between processes")
plt.show()

### VRIJEME OBRADE ZA SVAKOG KORISNIKA / PROSJEČNO VRIJEME OBRADE KORISNIKA
plt.plot(service)
plt.plot([np.average(service)] * len(service))
plt.title("Processing time per process")
plt.show()
