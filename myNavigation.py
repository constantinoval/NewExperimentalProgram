import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
from qtpy.QtCore import Qt, QObject
from qtpy.QtCore import Signal as pyqtSignal
import numpy as np

class myCurve(object):
    __points=None
    codes=None
    l=None
    lastindex=0
    __ax = None

    def __init__(self,ax):
        self.__ax=ax
        self.__points=[]
    
    def rebuild_line(self):
        if not self.__points: return
        xs,ys=list(zip(*self.__points))
        if self.l: self.l.remove()
        self.l = plt.Line2D(xs,ys,marker=".",color="black", lw=0.5)
        self.__ax.add_line(self.l)

    def clear(self):
        if not self.l: return
        self.__points=[]
        self.l.remove()
        self.l=None
        self.__lastindex=0
        self.__ax.figure.canvas.draw()
        
    def getpoints(self):
        return self.__points
    def setpoints(self,pnts):
        if not pnts: return        
        self.__points=pnts
        self.rebuild_line()
    points=property(getpoints, setpoints)
       
    def add_point(self,point):
        if self.__points and point[0]<self.__points[-1][0]:
            xs,ys = list(zip(*self.__points))
            for i,xx in enumerate(xs):
                if xx>point[0]: break
            self.__points.insert(i,point)
            self.lastindex=i
        else:
            self.__points.append(point)
            self.lastindex=len(self.__points)-1
        self.rebuild_line()
        
    def change_point(self,point):
        self.__points[self.lastindex]=point
        self.rebuild_line()
    
class MyNavigation(QObject):
    mpl_mv=pyqtSignal(float, float, name='mpl_move')
    def __init__(self, ax, mplwidget=None):
        super(MyNavigation,self).__init__()
        self.mplwidget=mplwidget
        self.ax = ax
        self.figure = ax.figure
        self.canvas = ax.figure.canvas
        self.zoomer = None
        self.mode = "zoom"
        self.drag = False
        self.interval = None
        self.distance = None
        self.curve = myCurve(self.ax)
        self.canvas.mpl_connect("button_press_event",self.on_press)
        self.canvas.mpl_connect("button_release_event",self.on_release)
        self.canvas.mpl_connect("motion_notify_event",self.on_move)
        self.canvas.mpl_connect("scroll_event",self.on_scroll)
        self.canvas.mpl_connect("axes_leave_event",self.on_leave_axes)
                
    def on_leave_axes(self, event):
        if event.inaxes==self.ax and self.mplwidget:
            self.mplwidget.setCursor(Qt.ArrowCursor)
    
    def on_press(self,event):
        if event.inaxes!=self.ax: return
        self.startx, self.starty = event.xdata, event.ydata

        if event.button==1 and self.mode == "interval":
            self.remove_interval()
            self.bg = self.canvas.copy_from_bbox(self.ax.bbox)
            self.interval=self.ax.axvspan(self.startx,self.startx,fc="gray", alpha=0.2)
            self.interval.set_animated(True)
            self.drag = True
            print('Mode=interval')

        if event.button==1 and self.mode == "distance":
            self.bg = self.canvas.copy_from_bbox(self.ax.bbox)
            self.distance, = self.ax.plot([self.startx, self.startx], [self.starty, self.starty], "black", ls="-.")
            self.txt = self.ax.text(self.startx,self.starty,"(%8.3e,%8.3e)\n%8.3e" % (0,0,0), ha='center')
            self.txt.set_animated(True)
            self.distance.set_animated(True)
            self.canvas.restore_region(self.bg)
            self.ax.draw_artist(self.txt)
            self.canvas.blit(self.ax.bbox)
            self.drag = True
                                   
        if event.button==1 and self.mode == "curve":
            self.curve.add_point((event.xdata,event.ydata))
            self.curve.l.set_animated(True)
            self.canvas.draw()
            self.bg = self.canvas.copy_from_bbox(self.ax.bbox)
            self.drag = True
            self.canvas.restore_region(self.bg)
            self.ax.draw_artist(self.curve.l)
            self.canvas.blit(self.ax.bbox)                            
  

    def on_move(self,event):
        if event.inaxes!=self.ax: return
        self.curx, self.cury = event.xdata, event.ydata
        if self.mplwidget:
            self.mpl_mv.emit(self.curx, self.cury)
        if self.mode=="interval" and self.drag:
            xy=self.interval.get_xy()
            xy[2,0]=event.xdata
            xy[3,0]=event.xdata
            self.interval.set_xy(xy)
            self.interval.set_xy(xy)
            self.canvas.restore_region(self.bg)
            self.ax.draw_artist(self.interval)
            self.canvas.blit(self.ax.bbox)
        if self.mode=="distance" and self.drag:
            self.distance.set_xdata([self.startx,self.curx])
            self.distance.set_ydata([self.starty,self.cury])
            self.txt.set_x(0.5*(self.startx+self.curx))
            self.txt.set_y(0.5*(self.starty+self.cury))
            dx=abs(self.startx-self.curx)
            dy=abs(self.starty-self.cury)
            self.txt.set_text("(%8.3e,%8.3e)\n%8.3e" % (dx,dy,np.sqrt(dx*dx+dy*dy)))
            self.canvas.restore_region(self.bg)
            self.ax.draw_artist(self.distance)
            self.ax.draw_artist(self.txt)
            self.canvas.blit(self.ax.bbox)
   
        if self.mode=="curve" and self.drag:
            self.curve.change_point((self.curx, self.cury))
            self.canvas.restore_region(self.bg)
            self.ax.draw_artist(self.curve.l)
            self.canvas.blit(self.ax.bbox)                            

    def on_release(self,event):
        if event.inaxes==self.ax:
            self.curx, self.cury = event.xdata, event.ydata
        if event.button==3 and event.inaxes==self.ax:
            self.ax.autoscale()
            self.canvas.draw()
        if self.mode == "interval" and self.drag and event.inaxes==self.ax:
            self.interval.set_animated(False)
            x1,x2=self.get_interval()
            if x1==x2: self.remove_interval()
            self.canvas.draw()
            self.drag = False

        if self.mode == "curve" and self.drag and event.inaxes==self.ax:
            self.curve.change_point((self.curx, self.cury))
            self.curve.l.set_animated(False)
            self.canvas.draw()
            self.drag = False
        if self.mode == "distance" and self.drag and event.inaxes==self.ax:
            self.distance.remove()
            self.txt.remove()
            del self.txt
            del self.distance
            self.canvas.draw()
            self.drag = False

    def on_scroll(self, event):
        scale = -1
        if event.button=="up": scale = 1
        b = self.ax.get_xbound()
        self.ax.set_xlim(b[0]-scale*0.1*(b[1]-b[0]), b[1]+scale*0.1*(b[1]-b[0]))
        b = self.ax.get_ybound()
        self.ax.set_ylim(b[0]-scale*0.1*(b[1]-b[0]), b[1]+scale*0.1*(b[1]-b[0]))
        self.canvas.draw()

    def get_interval(self):
        if self.interval:
            x1=self.interval.xy[0,0]
            x2=self.interval.xy[2,0]
            if x2<x1: x1,x2=x2,x1
            return (x1, x2)
        else: return None

    def remove_interval(self):
        if self.interval:
            self.interval.remove()
            self.canvas.draw()
            del self.interval
            self.interval=None

if __name__=="__main__":
    f = plt.figure()
    ax=f.add_subplot(111)
    nav = MyNavigation(ax)
    nav.mode="interval"
    ax.plot([0,0.1,0.2,0.3,0.4,0.5,0.6],[0,0.3,0.2,0.6,0.4,-0.5,-0.3])
    plt.show()

