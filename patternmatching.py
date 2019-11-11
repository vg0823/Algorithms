function foo():
	for y in range(0,3):
		for x in range(0,3):
			if(a[x+1][y]!=None):
				if(a[x+1][y] == a[x][y]):
					a[x][y] = a[x][y]*2
					a[x+1][y] = None
				if(a[x][y] == None):
					a[x][y] = a[x+1][y]
					a[x+1][y] = None
			