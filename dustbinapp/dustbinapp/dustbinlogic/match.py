#@aadit

def is_near(n,m):
	n = round(n)
	m = round(m)
	if n == m or abs(n - m) < 1:
		return True
	else:
		return False



def algorithm(l,value):
	l = [round(i) for i in l]
	for i in l:
		if is_near(value,i):
			return True
