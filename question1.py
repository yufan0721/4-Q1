import time
import matplotlib.pyplot as plt
def fib(n):
    if n <= 1:
        return 1
    else:
        if time.perf_counter()- times >= 20:
            return 'timeout'
        a = fib(n-1)
        b = fib(n-2)
        if a == 'timeout' or b =='timeout':
            return 'timeout'
        else:
            return a + b

def fib_dynamic(n):
    list_ = [0,1]
    for i in range(0,n):
        list_.append(list_[0] + list_[1])
        list_.pop(0)
    return list_[1]

a_time = []
b_time = []
n = []
global times
times = time.perf_counter()
for i in range(10,101,10):
    start_time = time.perf_counter()
    times = time.perf_counter()
    a = fib(i)
    end_time = time.perf_counter()
    a_time.append(end_time - start_time)
    start_time = time.perf_counter()
    b = fib_dynamic(i)
    end_time = time.perf_counter()
    b_time.append(end_time - start_time)
    n.append(i)
fig, ax = plt.subplots()
print(a_time)
print(b_time)
ax.plot(n, a_time, label='recursive')
ax.plot(n, b_time, label='dynamic ')
ax.legend()
plt.show()
