
t = 0
while t!=19:
	with open('ep_names\\Season ' + str(t + 1) + ' Episodes.txt','r') as f:
		x=f.readlines()
		for i in x:
			print(i)
	t+=1	

print(type(x))