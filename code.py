import time
import sys

print(sys.argv[0])
if len(sys.argv) > 1:
    print(sys.argv[1])

start_time=time.perf_counter()


age =float(input("Enter number"))

while True :
    age+=1
    print(age)
    if age >100:
        break




end_time=time.perf_counter()
print(f"loop finished taking {end_time - start_time}")


