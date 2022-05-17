import random

a = 5*4*3*2*1
print("5! = %d"%a)
s = 0
n = 0

for i in range(1, 21):
	s = s + i

print("Sum = %d"%s)

a = []

for i in range(0, 5):
	a.append(random.randint(0,100))
	n = n + a[i]

print(n)
