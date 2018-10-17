# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:50:06 2018

@author: feith
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from time import sleep
import pandas as pd
import argparse

COLORS = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'pink',
        'brown', 'orange', 'teal', 'coral', 'lightblue', 'lime', 'lavender', 'turquoise',
        'darkgreen', 'tan', 'salmon', 'gold', 'lightpurple', 'darkred', 'darkblue']


def parse_args():
    parser = argparse.ArgumentParser(description='Plot results of Simulations')
    parser.add_argument('--live', default=False, action='store_true')
    parser.add_argument('--names', default = None, nargs='*')
    parser.add_argument('--folders', default=None, nargs='*')
    parser.add_argument('--results_path', default=None)
    parser.add_argument('--window', default=100, type=int)
    parser.add_argument('--plots', default=[1,2], type=int, nargs='*', help='1:Rewards to elapsed time, 2:Rewards to timesteps, 3:rewards to episodes, 4:time vs time')
    args = parser.parse_args()
    return args

def extract_results(folder):
    files= [f for f in os.listdir(folder) if f.endswith('monitor.csv')]

    r = np.array([])
    l = np.array([])
    t = np.array([])
    for file in files:
        data = np.genfromtxt(os.path.join(folder,file), delimiter=',')
        data = data[1:]
        if not np.isnan(data).any():
            r = np.append(r,data[:,0])
            l = np.append(l,data[:,1])
            t = np.append(t,data[:,2])

    return r, l, t

def sort_lists(r,l,t,folder):
    order = np.argsort(t)
    r = [r[i] for i in order]
    l = [l[i] for i in order]
    l = np.cumsum(l)
    t = [t[i]/3600 for i in order]
    # gaps = []
    # if folder == "ppo2_cnn_10000000.0":
    #     temp_t = np.insert(t,0,0)
    #     gaps = [t[i]-temp_t[i] for i in range(len(t))]
    #     gap = max(gaps)
    #     gap_index = gaps.index(gap)
    #     t[330:] = t[330:] - gap + np.mean(gaps[:330])

    return r,l,t,np.arange(len(l))

def plot_figure(ax, X, Y, xaxis, yaxis, names,colors=COLORS):
    i=0
    ax.clear()
    for (x,y,name) in zip(X,Y,names):
        ax.scatter(x,y,color=colors[i],alpha=0.5,s=2)
        r,std = filter_outcome(y,window=args.window)
        ax.plot(x,r,label=name,color=colors[i])
        # ax.fill_between(x,r-2*std,r+2*std,color=colors[i],alpha=0.1)
        ax.legend(loc=2, fontsize=12)
        i+=1
    ax.set_xlabel(xaxis, fontsize=20)
    ax.set_ylabel(yaxis, fontsize=20)
    ax.tick_params(axis='both', which='major', labelsize=20)

def filter_outcome(r,window):
    r=pd.Series(r)

    return r.rolling(window).mean(), r.rolling(window).std()
    # firstmean = [np.mean(r[:window]) for i in range(window)]
    # for i in range(window,len(r)):
    #     firstmean.append(np.mean(r[i-window:i]))
    # r = firstmean
    # return r

def main(folders,names,window=100):

    R = []
    STD = []
    L = []
    T = []
    N = []
    for name,folder in zip(names,folders):
        r,l,t = extract_results(folder)
        r,l,t,n = sort_lists(r,l,t,folder)
        print(name+': '+str(t[-1]-t[0]))
        R.append(r)
        L.append(l)
        T.append(t)
        N.append(n)

    if 1 in args.plots:
        plot_figure(ax_t, T,R,'elapsed time [h]','Rewards',names)
    if 2 in args.plots:  
        plot_figure(ax_ts, L,R, 'timesteps','Rewards',names)
    if 3 in args.plots:
        plot_figure(ax_n, N,R,'Number of episodes','Rewards',names)
    if 4 in args.plots:
        plot_figure(ax_tvst, L,T, 'timesteps', 'elapsed time [h]',names)
    if args.live:
        plt.pause(30)
    else:
        plt.pause(1)
        plt.show(block=True)

if __name__ == '__main__':
    args=parse_args()
    if not args.folders and args.results_path:
        print("No folders given, looking for results")
        folders = [f.path for f in os.scandir(args.results_path) if f.is_dir()]
        args.folders = [f for f in folders if os.path.isfile(f+"/0.0.monitor.csv")]
        args.names = []
        for folder in folders:
            name=folder.split("/")[-1]
            name_params=name.split("_")
            if len(name_params)==4:
                args.names.append(name_params[0]+"_"+name_params[1]+"_"+name_params[3])
            elif len(name_params)==5:
                args.names.append(name_params[0]+"_"+name_params[1]+"_"+name_params[3]+"_"+name_params[4])
            else:
                print("error: name params not recognised")
        for folder, name in zip(args.folders, args.names):
            print(folder, name)

    plt.ion()
    if 1 in args.plots:
        time_p = plt.figure()
        ax_t = time_p.add_subplot(111)
    if 2 in args.plots:
        timestep_p = plt.figure()
        ax_ts = timestep_p.add_subplot(111)
    if 3 in args.plots:
        number_p = plt.figure()
        ax_n = number_p.add_subplot(111)
    if 4 in args.plots:
        tvst = plt.figure()
        ax_tvst = tvst.add_subplot(111)

    while args.live:
        print('live')
        main(args.folders,args.names, window=args.window)
    print('offline')
    main(args.folders,args.names, window=args.window)

