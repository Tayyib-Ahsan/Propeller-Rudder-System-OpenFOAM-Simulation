import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

def animate(i):
	f = open( 'C:/Users/ASUS/Desktop/PropellerRudderSystem/postProcessing/propellerInfo1/0/propellerPerformance.dat' , "r" )
	g = f.readlines()
	del g[ :100 ]
	
	x  = []
	y0 = []
	y1 = []
	y2 = []
	for lines in g :
		reading = lines.split()
		x.append(float(reading[0]))
		y0.append(float(reading[6]))
		y1.append(float(reading[5]))
		y2.append(float(reading[4]))



	ax1.clear()
	ax2.clear()
	ax3.clear()
	ax1.plot(x, y0, linestyle = 'dashed', label='eta0')
	ax2.plot(x, y1, linestyle = 'dashed', label='10*KQ')
	ax3.plot(x, y2, linestyle = 'dashed', label='KT')
	ax1.legend()
	ax2.legend()
	ax3.legend()



ani = animation.FuncAnimation(fig, animate, interval = 10000) 
plt.show()




