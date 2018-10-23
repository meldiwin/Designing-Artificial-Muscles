import Sofa
import os
from time import gmtime, strftime


class controller(Sofa.PythonScriptController):


    def initGraph(self, node):

            self.rootNode = node
            self.smawormNode= node.getChild('SMAWorm')
            self.mainNode = 2;

            
  
    def onKeyPressed(self,c):
        
        forces=self.smawormNode.getObject('SMAForce').findData('forces').value
        
        
        
        if (ord(c)==20): #right arrow => increase mainNode
            self.mainNode =  self.mainNode +1;
            if (self.mainNode > 4):
                self.mainNode=4;
            
            
        if (ord(c)==18): #left arrow => decrease mainNode
            self.mainNode =  self.mainNode -1;     
            if (self.mainNode < 1):
                self.mainNode=1;
                
        for i in range(0,6):
            forces[i] = [0, 0, 0,0,0,0];
                
    
    
        forces[self.mainNode]=[0, 0, 0,0,0,0];
        forces[self.mainNode-1]=[0,100,0,0,20,0];
        forces[self.mainNode+1]=[0,-100,0,0,-20,0];
        
        
        #forces[self.mainNode]=[0, 0, 0, 0, 0, 0];
        #forces[self.mainNode-1]=[0.000005,0.000007, 0.00004,- 0.000005, -0.000007, 0.00006];
        #forces[self.mainNode+1]=[0.000005, 0.000007, -0.00001, 0.00002, 0.000025, 0.00003];
        
        

        self.smawormNode.getObject('SMAForce').findData('forces').value = forces;
        
        
        
        # 0 0 0 0 0 0    0 0 -20 0 -200 0   0 0 40 0 0 0   0 0 -20 0 200 0    0 0 0 0 0 0   0 0 0 0 0 0
        
        print forces
        
        print ord(c)
        
       
  

       
       
    #def swap0(S1, S2):
     #   assert type(S1) == list and type(S2) == list
        
      #  tmp = S1[:]
       # S1 = S2[:]
        #S2= tmp
        #return
 
        #S1 = [1]
        #S2= [2]
        #swap0(S1, S2)
        
        
       
   #    swap forces values 
    

    '0 0 0 0 0 0    0 0 -20 0 -200 0   0 0 40 0 0 0   0 0 -20 0 200 0    0 0 0 0 0 0   0 0 0 0 0 0 ' 
        
        #forces[self.mainNode]=[0, 0, 0, 0, 0, 0];
        #forces[self.mainNode-1]=[5,7, 40,- 5, -7, 60];
        #forces[self.mainNode+1]=[5, 7, -10, 20, 25, 30];
        

        #self.smawormNode.getObject('SMAForce').findData('forces').value = forces;
                
                
                 # called on each animation step
             #print 'onBeginAnimatinStep (python) dt=%f total time=%f'%(dt,self.total_time)
           
                
  
	
	#print str(pos[indexFirstNode][0])
	#print str(pos[indexFirstNode][1])
	#print str(pos[indexFirstNode][2])
                
                
                
                
                
                
                
                


   # def onKeyPressed(self,c):
       
        
        
        
    #    if (ord(c)==20): #right arrow => increase mainNode
     #       self.mainNode =  self.mainNode +1;
      #      if (self.mainNode > 4):
       #         self.mainNode=4;
            
            
        #if (ord(c)==18): #left arrow => decrease mainNode
         #   self.mainNode =  self.mainNode -1;     
          #  if (self.mainNode < 1):
           #     self.mainNode=1;
                
        #for i in range(0,6):
         #   forces[i] = [0, 0, 0, 0, 0, 0];
                
    
        
        #forces[self.mainNode]=[0, 0, 0, 0, 0, 0];
        #forces[self.mainNode-1]=[5,7, 40,- 5, -7, 60];
        #forces[self.mainNode+1]=[5, 7, -10, 20, 25, 30];
        

        #self.smawormNode.getObject('SMAForce').findData('forces').value = forces;
        
        
        
        # 0 0 0 0 0 0    0 0 -20 0 -200 0   0 0 40 0 0 0   0 0 -20 0 200 0    0 0 0 0 0 0   0 0 0 0 0 0
        
        
        #print ord(c)


#       goalPositionRigid1 = self.goalNode.getObject('goalMOFiltered1').findData('position').value[0]
#
#           ##Update middle cable limits for grasping event
#           if (ord(c) == 21):
#               theta = 0.1
#               q=[0., 0., sin(theta/2.),cos(theta/2.)]
#               goalPositionRigid1 = rotateQuat(goalPositionRigid1,q)
#               print "Quat"
#               print goalPositionRigid1
#               goalPositionRigid1 = normalizeQuat(goalPositionRigid1)



#            self.goalNode.getObject('goalMOFiltered1').findData('position').value = goalPositionRigid1
