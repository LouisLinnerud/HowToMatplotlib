import matplotlib.pyplot as plt
import numpy as np

xx,yy = np.meshgrid(np.linspace(0,5,6),np.linspace(0,10,11))

print(xx)
print(yy)
plt.style.use('dark_background')
plt.subplot(1,2,1)
plt.plot(xx,'.')
#plt.colorbar(label='label')
plt.subplot(1,2,2)
plt.plot(xx,yy,'.')
#plt.colorbar(label='label')
plt.show()

print(xx*yy)