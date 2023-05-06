# A simple yet effective PRNG algorithm.
# Since we take only some digits of the time value, the increasing time would not directly affect our results. However, you can use different seeds by giving a second parameter when using "random" function.
import time
finalvalue = 0
def tryer(total, length, x, index):
	last = total * (length+x) + length * x
	try:
		return int(str(last)[0:index])
	except:
		tryer(total, length, x, index-1)
def randomizer(x, times):
	global finalvalue
	byted = bytes(x)
	stringed = str(x)
	length = int(len(stringed))
	total = 0
	for i in stringed:
		total += int(i)
	last_value = total * (length + x) + length * x
	times_new = times - 1
	if(times!=0):
		try:
			randomizer(last_value, times_new)
		except:
			new_last_value = tryer(total, length, x, 3)
			del last_value
			del byted
			del stringed
			randomizer(new_last_value, times_new)
	else:
		finalvalue = last_value
def random(digits=6, seed=int(str(time.time()* 100000)[6:18:2]), recvalue=5):
	global finalvalue
	randomizer(seed, recvalue)
	myvalue = str(finalvalue)[1:(digits+1)]
	del finalvalue
	return int(myvalue)
digit = int(input("How many digits you want?")) # Maximum is 6 digits.
x = random(digit) # If you want to add your own seed and recursion values, add them after the digit parameter.
print(x)

