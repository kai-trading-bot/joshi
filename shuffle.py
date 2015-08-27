from random import randrange

def shuffle(x):
	for i in range(len(x)-1,0,-1):
		j=randrange(i+1)
		x[i],x[j]=x[j],x[i]
		return x
