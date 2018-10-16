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



def gather_data(results_path,window=10):
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

        return r,l,t,np.arange(len(l))

    def filter_outcome(r,window):
    	r=pd.Series(r)

    	return r.rolling(window).mean(), r.rolling(window).std()
        # firstmean = [np.mean(r[:window]) for i in range(window)]
        # for i in range(window,len(r)):
        #     firstmean.append(np.mean(r[i-window:i]))
        # r = firstmean
        # return r

    def main(folders,names,window=10):

        R = []
        STD = []
        L = []
        T = []
        N = []
        data = {}

        for name,folder in zip(names,folders):
            r,l,t = extract_results(folder)
            r,l,t,n = sort_lists(r,l,t,folder)
            print(name+': '+str(t[-1]-t[0]))
            rfilter,std = filter_outcome(r,window)
            R.append(r)
            L.append(l)
            T.append(t)
            N.append(n)
            STD.append(std)
            data[name]=[r,l,t,n,rfilter,std]

        return data

    print("looking for results in "+results_path)
    folders = [f[0] for f in os.walk(results_path)]
    folders = [f for f in folders if os.path.isfile(f+"/0.0.monitor.csv")]
    names = []
    print("check")
    for folder in folders:
        name=folder.split("/")[-1]
        name_params=name.split("_")
        if len(name_params)==4:
            names.append(name_params[0]+"_"+name_params[1]+"_"+name_params[3])
        elif len(name_params)==5:
            names.append(name_params[0]+"_"+name_params[1]+"_"+name_params[3]+"_"+name_params[4])
        else:
            print("error: name params not recognised")
        print(names[-1], folder)
    print len(names)
    # return main(folders, names, window=window)

