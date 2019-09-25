import tie
from datatime import timedelta
start_time = time.monotonic()
def recur_fabo(n):
	if n<=1:
		return n
	else:
		return recur_fabo(n-1) +  recur_fabo(n-2)
n=int(input("how many terms"))
if n<=0:
	print("please enter positive number")
else:
	print("Fibonacci sequence")
	for i in range(n):
		print(recur_fibo(i+1)
#end_time = time.monotonic()
#print(timedelta(seconds=end_time - start_time))


