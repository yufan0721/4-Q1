def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_dynamic(n):
    list_ = [0,1]
    for i in range(0,n):
        list_.append(list_[0] + list_[1])
        list_.pop(0)
    return list_[1]

count = 1
while True:
    try:
        print(fib(count))
        count+=1
    except:
        break
try:
    fib_dynamic(count+1)
except:
    print('依然會崩潰')
else:
    print("不會崩潰")