
import matplotlib
matplotlib.use('TkAgg')
import time
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from gather_data import *

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
    
COLORS = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'pink',
        'brown', 'orange', 'teal', 'coral', 'lightblue', 'lime', 'lavender', 'turquoise',
        'darkgreen', 'tan', 'salmon', 'gold', 'lightpurple', 'darkred', 'darkblue']
prop_cycle = plt.rcParams['axes.prop_cycle']
COLORS = prop_cycle.by_key()['color']
data=gather_data("results/ppo2_mlp_CartPole-v0_None") ##returns data as r,l,t,n
alg = []
network = []
nenv = []

for key in data.keys():
    split = key.split("_")
    if split[0] not in alg: alg.append(split[0]) 
    if split[1] not in network: network.append(split[1])
    if split[2] not in nenv: nenv.append(split[2])

def destroy(e):
    sys.exit()

root = Tk.Tk()
root.wm_title("Results")


f = Figure(figsize=(5, 4), dpi=100)
ax = f.add_subplot(111)
#t = arange(0.0, 3.0, 0.01)
#s = sin(2*pi*t)
#
#ax.plot(t, s)
#find limits
ylimit = 0
xlimit = 0
for key in data.keys():
	if max(data[key][0]) >ylimit: ylimit = max(data[key][0])
	if max(data[key][1]) >xlimit: xlimit = max(data[key][1])
ax.set_title('Hopper')
ax.set_xlabel('TimeSteps', fontsize=12)
ax.set_ylabel('Rewards', fontsize=12)
ax.set_xlim(0,xlimit)
ax.set_ylim(0,ylimit)
ax.tick_params(axis='both', which='major', labelsize=12)

def update_plots():
    start = time.time()

    def plottings(Y,Yfilter,names):
        i = 0
        ax.clear()
        # canvas.restore_region(background)
        # for (x,y,yfilter,name) in zip(X,Y,Yfilter,names):

        #     ax.scatter(x,y,color=COLORS[i], alpha=0.5,s=2)
        #     ax.plot(x,yfilter,label=name,color=COLORS[i])
        #     # ax.fill_between(x,r-2*std,r+2*std,color=colors[i],alpha=0.1)
        #     ax.legend(loc=2, fontsize=12)
        #     i+=1 
        #     if i==10: i=0
        ax.plot(*Yfilter)
        ax.legend(labels=names,loc=2, fontsize=12)
        # ax.scatter(*Y)

        canvas.draw()
    print('gathering data')
    if type(alg) != list:
        Y,Yfilter, names = [],[],[]
        for key in data.keys():
            split= key.split("_")
#            print(key,alg.values(split[0]),network.values(split[1]),nenv.values(split[2]) )
            if alg.values(split[0]) and network.values(split[1]) and nenv.values(split[2]):
                # X.append(data[key][1])
                # Y.append(data[key][0])
                # Yfilter.append(data[key][4])
                names.append(key)
                Y.append(data[key][1])
                Y.append(data[key][0])
                Yfilter.append(data[key][1])
                Yfilter.append(data[key][4])
        print("Plotting")
        plottings(Y,Yfilter,names)
        print(time.time()-start)
# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
background=canvas.copy_from_bbox(ax.bbox)
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

button = Tk.Button(master=root, text='Quit', command=sys.exit)
button.pack(side=Tk.BOTTOM)


class checkbox:
    
    def __init__(self,master,names,text):
        self.master=master
        self.names = names
        self.text = text
        self.buttons= self.create_buttons()
        
    def create_buttons(self):
        buttons = {}
        self.f=Tk.Frame(self.master)
        self.textbox=Tk.Label(self.f,text=self.text, width =40)
        self.textbox.pack(side=Tk.LEFT)
        for item in self.names:
            buttons[item]=Tk.BooleanVar()
            buttons[item].set(False)   
            check= Tk.Checkbutton(self.f, text=item, variable=buttons[item], command=update_plots)
            check.pack(side=Tk.LEFT)
        self.f.pack(side=Tk.TOP, anchor=Tk.W)
        return buttons
    
    def values(self,item):
        return self.buttons[item].get()


alg = checkbox(root,alg,"Algorithm: ")
network=checkbox(root,network,"Network: ")
nenv = checkbox(root,nenv,"Nenv: ")


Tk.mainloop()
