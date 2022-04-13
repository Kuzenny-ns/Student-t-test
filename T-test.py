import matplotlib.pyplot as plt
import numpy as np
import math

n=1000
np.random.seed(seed=3)
x=2+np.random.normal(2, 1.5, n)
k=int(1.44*math.log(n)+1)

fig, plots = plt.subplots() 

y = list(range(0, n))
disp_arr=[]
for i in x:
    disp_arr.append(i ** 2)


#plots.scatter(y, x)
#plt.show()
avrg = sum(x)/n
print("Averege: ", avrg)
d = math.sqrt(sum(disp_arr)/n)
print("Averege root dispersion: ", d)
d2 = np.std(x)
print(np.std(x))
print("Dispersion2: ", pow(d, 2))

stop = False
#1.962
while(stop != True):
    stop = True
    max_anomaly = (max(x) - avrg)/d
    max_index = np.argmax(x)
    min_anomaly = (avrg - min(x))/d
    min_index = np.argmin(x)
    if(max_anomaly > 1.962):
        stop = False
        x[max_index] = avrg
    if(min_anomaly > 1.962):
        stop = False
        x[min_index] = avrg
plots.scatter(y, x)
plt.show()
