import matplotlib.pyplot as plt 
import numpy as np 

   
x = np.arange(10,20,1)
y = np.arange(40,60,2)
print(x)
print(y)


#hypothesis function
t0 = 1
t1 = 2
print("initial theta1 and theta0 are",t1,t0)

for i in range(0,10):
    val0 = 0
    va11 = 0
    for j in range(0,10):
        val0 += t1*x[j] + t0 - y[j]
        
    t0 = t0 - (val0/10)
    
#plotting first graph 
print(t1,t0)
plt.plot(x,y,'b.')

#plotting second graph
new_y = []
for i in range(0,10):
    new_y.append(t1*x[i] + t0)
     
print(new_y)
plt.plot(x,new_y,'r') 
plt.title('Test Data') 
plt.xlabel('x value') 
plt.ylabel('Price')  
plt.show()
