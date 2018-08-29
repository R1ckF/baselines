# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:50:06 2018

@author: feith
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from time import sleep

folders = ["a2c_cnn_10000000.0","ppo2_cnn_10000000.0", "acktr_cnn_10000000.0", "trpo_mpi_cnn_10000000.0"]
names = ["A2C CNN", "PPO CNN", "ACKTR CNN","TRPO_MPI"]


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
        ax.legend(loc=4)
    ax.set_xlabel(xaxis)
    ax.set_ylabel(yaxis)


def filter_outcome(r,window=10):
    r[window:] = [np.mean(r[i-window:i]) for i in range(window,len(r))]
    return r

def main(folders,names):

    R = []
    L = []
    T = []
    N = []
    for folder in folders:
        r,l,t = extract_results(folder)
        r,l,t,n = sort_lists(r,l,t,folder)
        r = filter_outcome(r,window=10)
        R.append(r)
        L.append(l)
        T.append(t)
        N.append(n)

    plot_figure(ax_t, T,R,'elapsed time [h]','Rewards',names)
    plot_figure(ax_ts, L,R,'timesteps','Rewards',names)
    plot_figure(ax_n, N,R,'Number of episodes','Rewards',names)
    plot_figure(ax_tvst, L,T, 'timesteps', 'elapsed time [h]',names)
    plt.pause(30)


if __name__ == '__main__':
    plt.ion()
    time_p = plt.figure()
    ax_t = time_p.add_subplot(111)
    timestep_p = plt.figure()
    ax_ts = timestep_p.add_subplot(111)
    number_p = plt.figure()
    ax_n = number_p.add_subplot(111)
    tvst = plt.figure()
    ax_tvst = tvst.add_subplot(111)
    while True:

        main(folders,names)



#    for (r,t,name) in zip(R,T,names):
#        plt.plot(t,r,label = name)
#
#    plt.xlabel('t [h]')
#    plt.ylabel('Rewards')
#    plt.legend(loc=4)
#    plt.show()
#
#    for (r,l,name) in zip(R,L,names):
#        plt.plot(l,r,label = name)
#    plt.xlabel('timesteps')
#    plt.ylabel('Rewards')
#    plt.legend(loc=4)
#    plt.show()
#
#    for (r,l,name) in zip(R,L,names):
#        plt.plot(np.arange(len(l)),r,label = name)
#    plt.xlabel('Number of episodes')
#    plt.ylabel('Rewards')
#    plt.legend(loc=4)
#    plt.show()
