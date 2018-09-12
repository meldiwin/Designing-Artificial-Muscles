import Sofa
import os
import sys



def transformTableInString(Table):
	sizeT =  len(Table);
	strOut= ' ';
	for p in range(sizeT):
		strOut = strOut+ str(Table[p])+' '
	return strOut



class controller(Sofa.PythonScriptController):


    def initGraph(self, node):
        #self.rootNode = node
        #self.smawormNode= node.getChild('SMAWorm')
        self.forceSensorNode = node
        self.MechaObject = node.getObject('FS_MO')
        self.mapping = node.getChild('ForceSensorPoint1').getObject('map')
        #self.Point=self.smawormNode.getChild('SMAPoint')
        self.totalTime = 0
        
        ''' sensor setup coordinates '''
        ''' At the simulation there is relationship between the sensor resolution and the expected displacement of the actuator only at simulation'''
        
        ''' offset for adjusting the position of the sensor to make sure it has a good contact with the actuator'''
        
        self.velocity= -1; #mm/s  as it compression 
        
        '''The protection of the sensor by adding the limit, this limit it could be optimized'''
        
        
        self.limit_up=  0.7 # (maximum position of the sensor in z)
        self.limit_down=-0.01 # (minimum position of the sensor in z)

        
          

    def applyTranslationOnZ(self,offsetZ, limit_down, limit_up):
        '''rigid position of the sensor quaternion '''
        pos = [0.0]*7

        # copy the actual position of the sensor
        for j in range (0,7):
            pos[j] =  self.MechaObject.position[0][j]
            

            
        # apply the translation in Z
        pos[2] = pos[2]+ offsetZ
        
        
        # if the limits are reached modify the position
        
        if pos[2]>limit_up:
            pos[2]=limit_up
            
        if pos[2]<limit_down:
            pos[2]=limit_down
            
        #print pos
    
        # the position is sent back to SOFA      
        self.MechaObject.findData('position').value= transformTableInString(pos)
        self.MechaObject.findData('free_position').value= transformTableInString(pos)
        self.mapping.init()
        


    def onBeginAnimationStep(self,dt):
        self.totalTime+=dt
        
        offsetZ = self.velocity*dt
        
        self.applyTranslationOnZ(offsetZ, self.limit_down, self.limit_up)
        
        
        
