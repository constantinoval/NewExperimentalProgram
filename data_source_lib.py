import zipfile as zp
import os
import numpy as np

def lvmopen(fname):
    if fname[-3:].upper()=="LVM":
        fin=open(fname,"r")
    if fname[-3:].upper()=="LVZ":
        fz=zp.ZipFile(fname)
        fin=fz.open(fz.namelist()[0])
    x  = []
    y1 = []
    y2 = []
    while 1:
        l=fin.readline()
        if "Delta_X" in l:
            dx=float(l.split()[1])
            break  
    while 1:
        if "X_Value" in fin.readline(): break
    i=0
    for l in fin:
        if len(l.split())<2: break
        x.append(dx*i)
        y1.append(float(l.split()[-2]))
        y2.append(float(l.split()[-1]))
        i=i+1
    fin.close()
    if 'fz' in locals(): fz.close()
    return (x,y1,y2)
    
def save_as_lvz(fname, del_old=True):
    if fname[-3:].upper()!="LVM":
        return
    fz=zp.ZipFile(fname[:-3]+"lvz", mode="w",compression=zp.ZIP_DEFLATED)
    fz.write(fname)
    fz.close()
    if del_old:
        os.remove(fname)

def save_as_npz(fname, del_old=True):
    x,y1,y2=lvmopen(fname)
    save_npz(fname[:-3]+'npz',x,y1,y2)
    if del_old:
        os.remove(fname)

def save_npz(fname,x,y1,y2):
    np.savez_compressed(fname,dt=x[1]-x[0],y1=y1,y2=y2)

def load_npz(fname):
    data=np.load(fname)
    x=np.arange(0,len(data['y1']))*data['dt']
    return (x, data['y1'],data['y2'])
