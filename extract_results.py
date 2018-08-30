# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:50:06 2018

@author: feith
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from time import sleep

import argparse




def parse_args():
    parser = argparse.ArgumentParser(description='Plot results of Simulations')
    parser.add_argument('--live', default=False, action='store_true')
    parser.add_argument('--alg', default=None, nargs='*')
    parser.add_argument('--network', default=None, nargs='*')
    parser.add_argument('--env', default=None, nargs='*')
    parser.add_argument('--folder', default='', type=str)
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

    gaps = []
    if folder == "ppo2_cnn_10000000.0":
        temp_t = np.insert(t,0,0)
        gaps = [t[i]-temp_t[i] for i in range(len(t))]
        gap = max(gaps)
        gap_index = gaps.index(gap)
        t[330:] = t[330:] - gap + np.mean(gaps[:330])

    return r,l,t,np.arange(len(l))

def plot_figure(ax, X, Y, xaxis, yaxis, names):
    ax.clear()
    for (x,y,name) in zip(X,Y,names):
        ax.plot(x,y,label=name)
        ax.legend(loc=4, fontsize=20)
    ax.set_xlabel(xaxis, fontsize=20)
    ax.set_ylabel(yaxis, fontsize=20)
    ax.tick_params(axis='both', which='major', labelsize=20)

def filter_outcome(r,window=10):
    firstmean = [np.mean(r[:window]) for i in range(window)]
    for i in range(window,len(r)):
        firstmean.append(np.mean(r[i-window:i]))
    r = firstmean
    return r

def main(folders,names,window=100):

    R = []
    L = []
    T = []
    N = []
    for folder in folders:
        r,l,t = extract_results(folder)
        r,l,t,n = sort_lists(r,l,t,folder)
        r = filter_outcome(r,window=100)
        R.append(r)
        L.append(l)
        T.append(t)
        N.append(n)

    if 1 in args.plots:
        plot_figure(ax_t, T,R,'elapsed time [h]','Rewards',names)
    if 2 in args.plots:  
        plot_figure(ax_ts, L,R,'timesteps','Rewards',names)
    if 3 in args.plots:
        plot_figure(ax_n, N,R,'Number of episodes','Rewards',names)
    if 4 in args.plots:
        plot_figure(ax_tvst, L,T, 'timesteps', 'elapsed time [h]',names)
    if args.live:
        plt.pause(5)
    else:
        plt.pause(1)
        plt.show(block=True)

if __name__ == '__main__':
    args=parse_args()
    folders=[]
    names = []

    for (alg,network,env) in zip(args.alg,args.network,args.env):
        folders.append(args.folder+'/'+alg+'_'+network+'_'+env)
        names.append(alg)
   

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
        main(folders,names, window=args.window)
    print('offline')
    main(folders,names, window=args.window)

