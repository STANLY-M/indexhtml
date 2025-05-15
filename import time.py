import time
start = time.time()

a=[i for i in range(100000000)]
b=[i for i in range(100000000,200000000)]

print(time.time()-start)