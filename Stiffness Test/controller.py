import Sofa
import os
from math import *
import time


class controller(Sofa.PythonScriptController):
        def initGraph(self, node):
            self.rootNode = node
            self.smawormNode= node.getChild('SMAWorm')
            self.Point= self.smawormNode.getChild('SMAPoint')
            self.mainNode = 2;
            self.notYetDone=True
            self.totalTime = 0
            self.file = open('position.txt', 'w')    #  position of  pedot up layer
    
        
        def onBeginAnimationStep(self,dt):
            self.totalTime+=dt
            if ( 1.1 <self.totalTime<1.12):
                d=self.Point.getObject('location').findData('position').value
                D=d[0][2]
                print 'D is ', D
                

     