#Name:Ashish Patwa_Roll No:21MF10009
#generation of price paths for a stock using monte carlo simulation
import matplotlib.pyplot as plt
import numpy as np
import math


def newpath(current_price, drift, volatility, dt, T):
        a=0
        prices=[]
        prices.append(600)
        T-=1
        while(T > dt):
            drift=np.random.normal(0,1)
            dWt = np.random.normal(-math.sqrt(dt), math.sqrt(dt))  
            dYt = drift*dt + volatility*dWt 
            current_price += dYt  
            prices.append(current_price)  
            T -= dt 

        return prices


paths = 5000
initial_price = 600
drift=0.9
volatility = .02
dt = 1
T = 30
price_paths = []
endvalues=[]

for i in range(0, paths):
    price_paths.append(newpath(initial_price, drift, volatility, dt, T))
    

for price_path in price_paths:
    plt.plot(price_path,linewidth=0.5)
    endvalues.append(price_path[-1])

endvalues=np.array(endvalues)
plt.axhline(y = initial_price,color='black',linewidth=0.5)
plt.xlim(0,30)
plt.title('Price Paths')
plt.show()
plt.hist(endvalues,bins=20)
plt.title('Normal distribution of price vs frequency')
plt.show()
