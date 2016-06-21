import matplotlib.pyplot as plt
import numpy as np

#function to plot and display position of notes on the 2D graph
def plot_tabs(base, pos, timestamp, t,filename):
	
	x = 0
	graphs = int(round(t/3))
	fig = plt.figure("Guitar Plot", figsize = (15,10))
	fig.suptitle('Tablature for %s' % filename, fontsize = 20)
	for i in range(graphs):
		ax = plt.subplot(graphs,1,i+1)

		plt.axis([x,x+3,14,0])

		plt.tick_params(labeltop = False, labelbottom = False, labelright = False, labelleft = True)
		plt.axhline(y=14)
		
		for i in range(2,14,2):
				plt.axhline(y=i)

		plt.plot((x+0.0325,x+0.0325), (2, 12), 'black')

		for i in range(len(timestamp)):
			if(timestamp[i] < float(x+3)):
				plt.annotate(pos[i],(timestamp[i],base[i]*2+0.5),size = 16)

		plt.xticks(np.arange(x, x+3, 0.125))
		plt.yticks([2,4,6,8,10,12],['E','B','G','D','A','E'])
		x+=3
	plt.savefig("/home/rahul/Desktop/output.pdf")
	plt.show()