import time
import sys
s
print(sys.argv[0])
if len(sys.argv) > 1:
    print(sys.argv[1])

start_time=time.perf_counter()


age =float(input("Enter number"))

while age < 10 :
    age+=1
    print(age)



end_time=time.perf_counter()
print(f"loop finished taking {end_time - start_time}")


