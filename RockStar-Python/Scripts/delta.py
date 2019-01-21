import sys
import os
#sys.path.insert(0,'../')

#from readgadget import *
#from pygadgetreader import *
#from pylab import *
import numpy as np

import h5py


delta = 0
for n_s in range(2):
    snaps=['chi','phi','psiN','T00']
    for snap in snaps:
        f = h5py.File('./output/lcdm_snap00'+str(n_s)+'_'+snap+'.h5', "r")
        s = np.array(list(f['data']))
        f = h5py.File('./back/output/lcdm_snap00'+str(n_s)+'_'+snap+'.h5', "r")
        s0 = np.array(list(f['data']))
        delta += np.sum(s[:,:,:]-s0[:,:,:])
        del f


    snaps=['B','p']
    for snap in snaps:
        f = h5py.File('./output/lcdm_snap00'+str(n_s)+'_'+snap+'.h5', "r")
        s = np.array(list(f['data']))
        f = h5py.File('./back/output/lcdm_snap00'+str(n_s)+'_'+snap+'.h5', "r")
        s0 = np.array(list(f['data']))
        for i in range(3):
            delta += np.sum(s[:,:,:,i]-s0[:,:,:,i])

        del f

    snaps=['hij','Tij']
    for snap in snaps:
        f = h5py.File('./output/lcdm_snap00'+str(n_s)+'_'+snap+'.h5', "r")
        s = np.array(list(f['data']))
        f = h5py.File('./back/output/lcdm_snap00'+str(n_s)+'_'+snap+'.h5', "r")
        s0 = np.array(list(f['data']))
        for i in range(6):
            delta += np.sum(s[:,:,:,i]-s0[:,:,:,i])

        del f
print delta
