import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import matplotlib.animation as animation
import numpy as np

x = np.linspace(0,15,50)
y_1 = np.sin(x) + 0.1*np.random.randn(len(x))
y_2 = np.sin(x)
xx,yy=np.meshgrid(np.linspace(-3,3,100),np.linspace(-1,1,100))
f_1 = xx*2+xx*yy
#Figure
plt.style.use("dark_background")
fig=plt.figure(figsize=(16,9))
fig.text(0.5,0.95,"HowToPLT",ha="center",va="top",fontsize=20)
plt.subplots_adjust(wspace=0.2,hspace=0.3)
plt.subplot(2,2,1)#jobber med øverste plot
#plotting plus style
plt.plot(x,y_2,color='green',lw=3,label="theory")
plt.plot(x,y_1,'mo--', lw=1.5,ms=4,label="data")
#adding info
plt.title("NormalPlot")
plt.legend(loc="lower center",fontsize=10,ncol=2) #note legend relays on label marking in plot, and ncol is stacked/horizontal
#adjusting axis
plt.xlabel("$x$ label")
plt.ylabel("$\psi$ label")
plt.ylim(-1.2,1.2) #limits
plt.xticks(np.arange(min(x), max(x)+1, 2)) #tick distance
#adding grid
plt.grid()

#plot 2
plt.subplot(2,2,2)
cp=plt.contour(xx,yy,f_1,levels=20,cmap="binary")#has to be a different cmap than fill
plt.contourf(xx,yy,f_1,levels=20)#countourplot with fill
plt.colorbar(label="label")
plt.clabel(cp, fontsize=6) # verdi på linjene
plt.title("2D countour plot")

#plot 3
U = xx**2+yy
V = xx-yy**2
vectorLength = np.sqrt(U**2+V**2)
startPoints = np.array([[-1,0],[1,0],[0,0.5],[0,0]])
plt.subplot(2,2,3)
plt.streamplot(xx,yy,U,V,color=vectorLength,cmap="cool")#contoured arrows
plt.streamplot(xx,yy,U,V,start_points=startPoints,color="gold",linewidth=2)#gold arrows
plt.colorbar()
plt.grid()
plt.title("Stream plot")

#plot 4 animations
def f_2(x,t):
    return np.sin(x-3*t)
x = np.linspace(0,10*np.pi,1000)
#
ax = plt.subplot(2,2,4)
ln1, = plt.plot([],[])
ax.set_xlim(0,10*np.pi)
ax.set_ylim(-1.5,1.5)
plt.title("Animation")
#animations
def animate(i):
    ln1.set_data(x,f_2(x,1/50*i))#1/50 => 50 fps
ani = animation.FuncAnimation(fig,animate,frames=100,interval=50)
#ani.save('/Users/louislinnerud/Documents/PROGGING/actuallyLearningSciPy/resources/ani.gif',writer='pillow',fps=50, dpi=100)

plt.show()
