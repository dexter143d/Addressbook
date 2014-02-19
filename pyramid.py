step=int(input("Enter Pyramid Steps"));


for i in range(0,step):
	j=(i*2)+1
	k=i
	while(j>0):		
		while(k<=step):
			print("",end=" ")
			k+=1
		print('*',end="")			
		j-=1
	print('')






















#/////////////////////////////////////////////////////////////////
print('\n \n \n \n 	')


for i in range(step+1,1,-1):	
	j=(i*2)+1
	k=i
	while(j>0):		
		while(k<=step):
			print(" ",end="")
			k+=1
		print('*',end="")			
		j-=1
	print('')
