import Sofa
import SofaPython
from math import sin,cos, sqrt


import os
path = os.path.dirname(os.path.abspath(__file__))+'/'


PI= 3.14159265359

###### TAG: inverse or not
inverse = 1



######## geometry parameters
legLength = 10  # mm
RadiusEffector= 4 # mm
numNodePerLeg = 11;
clampingRadius= 5 #mm
clampingPosZ=-10 

numBeamPerLeg = numNodePerLeg -1;



dt=0.001
gravity = 9810
YoungModulus=1e9
density = 0.0000092 


print "**************************** README **********************************"
print "This scene makes a model of a robot created at MIT titi"
print "It assumes that the inflated cylinders are model with inflated beams"
print "**********************************************************************"

#Multiplication of two quaternions (gives the composition of the two rotation)
def rotateQuat(q1,q2):
    c0 = q1[3]*q2[3] - q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2]
    c1 = q1[3]*q2[0] + q1[0]*q2[3] + q1[1]*q2[2] - q1[2]*q2[1]
    c2 = q1[3]*q2[1] + q1[1]*q2[3] + q1[2]*q2[0] - q1[0]*q2[2]
    c3 = q1[3]*q2[2] + q1[2]*q2[3] + q1[0]*q2[1] - q1[1]*q2[0]

    q1 = [c1,c2,c3,c0]

    return q1

            
            

#Rotate a vector using a quaternion v'=qvq(-1)
def rotate(v,q):
    c0 = ((1.0 - 2.0 * (q[1] * q[1] + q[2] * q[2]))*v[0] + (2.0 * (q[0] * q[1] - q[2] * q[3])) * v[1] + (2.0 * (q[2] * q[0] + q[1] * q[3])) * v[2])
    c1 = ((2.0 * (q[0] * q[1] + q[2] * q[3]))*v[0] + (1.0 - 2.0 * (q[2] * q[2] + q[0] * q[0]))*v[1] + (2.0 * (q[1] * q[2] - q[0] * q[3]))*v[2])
    c2 = ((2.0 * (q[2] * q[0] - q[1] * q[3]))*v[0] + (2.0 * (q[1] * q[2] + q[0] * q[3]))*v[1] + (1.0 - 2.0 * (q[1] * q[1] + q[0] * q[0]))*v[2])

    v[0] = c0
    v[1] = c1
    v[2] = c2

    return v



def inverseQuat(q):
    return [ -q[0], -q[1], -q[2], q[3] ]


def inverseTransform(a_H_b):
    b_H_a=[ ]
    q = [ a_H_b[3], a_H_b[4], a_H_b[5], a_H_b[6] ] ;
    b_H_a= b_H_a +  rotate([ -a_H_b[0], -a_H_b[1],-a_H_b[2] ], q)
    b_H_a= b_H_a +  inverseQuat( q ) ;
    
    return b_H_a
 
    
def composeTransform(a_H_b, b_H_c):
    a_H_c = [ ]
    b_c_in_a = rotate([ b_H_c[0], b_H_c[1], b_H_c[2]],  inverseQuat([a_H_b[3], a_H_b[4], a_H_b[5],a_H_b[6]])  )
    a_H_c = a_H_c + [ a_H_b[0] + b_c_in_a[0],  a_H_b[1] + b_c_in_a[1], a_H_b[2] + b_c_in_a[2] ]     
    a_H_c = a_H_c + rotateQuat([a_H_b[3], a_H_b[4], a_H_b[5],a_H_b[6]] , [b_H_c[3], b_H_c[4], b_H_c[5],b_H_c[6]] )  
    
    return a_H_c
    
    

def transformTableInString(Table):
	sizeT =  len(Table);
	strOut= ' ';
	for p in range(sizeT):
		strOut = strOut+ str(Table[p])+' '

	return strOut


#Takes a n dimensional vector of vector and transform it into a simple vector 
def transformDoubleTableInSimpleTable(Table):
    size0 =  len(Table);

    # count the size
    size=0;
    for i in range(size0):
        size = size+len(Table[i]);

    TableOut=[0]*size;
    s=0;
    for i in range(size0):
        for j in range(len(Table[i])):
            TableOut[s] = Table[i][j];
            s=s+1;

    return TableOut



def createScene(rootNode):
    rootNode.createObject('RequiredPlugin', name='SoftRobots')
    rootNode.createObject('RequiredPlugin', name='BeamAdapter')
    rootNode.createObject('RequiredPlugin', name='SofaPython')
    rootNode.createObject('VisualStyle', displayFlags='showVisualModels hideBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields showInteractionForceFields hideWireframe', bbox='0 0 0 1 1 1')
    rootNode.findData('gravity').value= '0. 0 '+str(-gravity)
    rootNode.createObject('PythonScriptController', classname="controller", filename="inversecontroller.py")
  


    
    if inverse:
        rootNode.createObject('FreeMotionAnimationLoop')
        rootNode.createObject('QPInverseProblemSolver',name='solver', tolerance=[1e-10], maxIterations=[1000], epsilon='0.0001')
        #rootNode.createObject('QPInverseProblemSolver', name="QP", printLog='0')
        #rootNode.createObject('GenericConstraintSolver',name='solver', tolerance=[1e-10], maxIterations=[100])
        rootNode.createObject('BackgroundSetting', color=[0, 0.768627, 0.811765])
    else:
        rootNode.createObject('BackgroundSetting', color='0 0.168627 0.211765' , image=path+'images/P'+str(1030725)+'.JPG')#, image =path+'grille.jpeg' )
            
    
    rootNode.findData('dt').value= dt;

    #rootNode.createObject('FreeMotionAnimationLoop')
    #rootNode.createObject('GenericConstraintSolver', maxIterations='1000', tolerance='1e-15')
    #rootNode.createObject('CollisionPipeline', verbose='0')
    #rootNode.createObject('CollisionResponse', response='FrictionContact', responseParams='mu=0.5')
    #rootNode.createObject('BruteForceDetection', name='N2')
    
    alarmDistance=0.2
    #rootNode.createObject('LocalMinDistance', name="Proximity", alarmDistance=alarmDistance, contactDistance="0.1", angleCone='0.1')

    
    rootNode.createObject('OglSceneFrame', style="Arrows", alignment="TopRight")
    rootNode.createObject('SerialPortBridgeGeneric', name="serial", port="/dev/ttyACM0", baudRate="115200", size= "0", listening="true")
    
    

    
    ## Topology & Geometry of the model 
    pos = [[0 ,0, 0, 0, 0, 0, 1]];
    lines1=[ ];
    for i in range(numBeamPerLeg):
        posX = RadiusEffector + (legLength/numBeamPerLeg)*(i+1)
        pos = pos+[[posX, 0, 0,0,0,0,1]]
        lines1 = lines1 + [ i, i+1]
    
    lines2=[ ];
    for i in range(numBeamPerLeg):
        posX = RadiusEffector + (legLength/numBeamPerLeg)*(i+1)
        pos = pos+[[cos(2*PI/3)*posX, sin(2*PI/3)*posX, 0,0,0, sin(2*PI/6), cos(2*PI/6)]]
        if i==0:
            lines2 = lines2 + [ 0, numBeamPerLeg+1]
        else:
            lines2 = lines2 + [ numBeamPerLeg+i, numBeamPerLeg+i+1]
        
    lines3=[ ];
    for i in range(numBeamPerLeg):
        posX = RadiusEffector + (legLength/numBeamPerLeg)*(i+1)
        pos = pos+[[cos(4*PI/3)*posX, sin(4*PI/3)*posX, 0,0,0, sin(4*PI/6), cos(4*PI/6)]]
        if i==0:
            lines3 = lines3 + [ 0, 2*numBeamPerLeg+1]
        else:
            lines3 = lines3 + [ 2*numBeamPerLeg+i, 2*numBeamPerLeg+i+1]
            
            
    DOF0TransformNode0_beam1=[RadiusEffector, 0, 0, 0, 0, 0, 1]    
    DOF0TransformNode0_beam2=[cos(2*PI/3)*RadiusEffector, sin(2*PI/3)*RadiusEffector, 0, 0, 0, sin(2*PI/6), cos(2*PI/6)]
    DOF0TransformNode0_beam3=[cos(4*PI/3)*RadiusEffector, sin(4*PI/3)*RadiusEffector, 0, 0, 0, sin(4*PI/6), cos(4*PI/6)]
    
    DOF1TransformNode1_beam1 = [0,0,0,0,0,0,1]
    DOF1TransformNode1_beam2 = [0,0,0,0,0,0,1]
    DOF1TransformNode1_beam3 = [0,0,0,0,0,0,1]
    
    for i in range(numBeamPerLeg-1):
        DOF0TransformNode0_beam1 = DOF0TransformNode0_beam1 + [0,0,0,0,0,0,1]
        DOF0TransformNode0_beam2 = DOF0TransformNode0_beam2 + [0,0,0,0,0,0,1]
        DOF0TransformNode0_beam3 = DOF0TransformNode0_beam3 + [0,0,0,0,0,0,1]
 
        DOF1TransformNode1_beam1 = DOF1TransformNode1_beam1 + [0,0,0,0,0,0,1]
        DOF1TransformNode1_beam2 = DOF1TransformNode1_beam2 + [0,0,0,0,0,0,1]
        DOF1TransformNode1_beam3 = DOF1TransformNode1_beam3 + [0,0,0,0,0,0,1]
        
    
    clampingPos=[[ ]] 
    for i in range(3):
        
        initialH = [cos(i*2*PI/3)*clampingRadius, sin(i*2*PI/3)*clampingRadius, clampingPosZ, 0, 0, sin(i*2*PI/6), cos(i*2*PI/6)]
        rotation = [ 0, 0, 0, 0, sin(PI/2.5), 0, cos(PI/2.5)]
        #rotation = [0,0,0,0,0,0,1]
        clampingPos = clampingPos + [composeTransform(initialH, rotation) ]
    
    
    #########################################
    # Beam 
    #########################################
    
    clampingNode = rootNode.createChild('clamping')
    clampingNode.createObject('MechanicalObject', name='MO', template='Rigid', showObject='1', showObjectScale='0.4', position=clampingPos)
    
    beamNode = rootNode.createChild('beamMechanics')
    beamNode.createObject('EulerImplicitSolver', firstOrder="0", rayleighStiffness=0.0, rayleighMass='0')
    #beamNode.createObject('CGLinearSolver', name='solver')
    beamNode.createObject('SparseLDLSolver', name='solver', template='CompressedRowSparseMatrixd')
    if inverse:
        beamNode.createObject('GenericConstraintCorrection', solverName="solver")
    
    beamNode.createObject('MechanicalObject', name='MO', template='Rigid', showObject='1', showObjectScale='0.4', position=pos)



    leg1Node= beamNode.createChild('leg1')
    leg1Node.createObject('Mesh', lines=lines1)
    leg1Node.createObject('BeamInterpolation', name='leg1', dofsAndBeamsAligned='0', radius=0.003, defaultYoungModulus= YoungModulus, DOF0TransformNode0 = DOF0TransformNode0_beam1, DOF1TransformNode1 = DOF1TransformNode1_beam1)
    leg1Node.createObject('AdaptiveBeamForceFieldAndMass', massDensity=density, interpolation='@leg1')
    
    
    
    
    

    leg2Node= beamNode.createChild('leg2')
    leg2Node.createObject('Mesh', lines=lines2)
    leg2Node.createObject('BeamInterpolation', name='leg2', dofsAndBeamsAligned='0', radius=0.003 , defaultYoungModulus= YoungModulus, DOF0TransformNode0 = DOF0TransformNode0_beam2, DOF1TransformNode1 = DOF1TransformNode1_beam2)
    leg2Node.createObject('AdaptiveBeamForceFieldAndMass', massDensity=density, interpolation='@leg2')       

    

    leg3Node= beamNode.createChild('leg3')
    leg3Node.createObject('Mesh', lines=lines3)
    leg3Node.createObject('BeamInterpolation', name='leg3', dofsAndBeamsAligned='0', radius=0.003 , defaultYoungModulus= YoungModulus, DOF0TransformNode0 = DOF0TransformNode0_beam3, DOF1TransformNode1 = DOF1TransformNode1_beam3)
    leg3Node.createObject('AdaptiveBeamForceFieldAndMass', massDensity=density, interpolation='@leg3')   
    
    #beamNode.createObject('ConstantForceField', indices='2 3 4 5', force='0 0 0 0 900000 0')
    
    ##### OKAY
    
    beamNode.createObject('RestShapeSpringsForceField', points=[numBeamPerLeg, 2*numBeamPerLeg, 3*numBeamPerLeg], angularStiffness='10e100', stiffness='10e100', external_rest_shape='@../clamping/MO', external_points='0 1 2' );
   
    #constraintNode= beamNode.createChild('constraint')
    #constraintNode.createObject('FixedConstraint', indices='0')
    
    
    visualEffector = beamNode.createChild('visu')
    visualEffector.createObject('Mesh', name='mesh', position=[RadiusEffector, 0, 0,cos(2*PI/3)*RadiusEffector, sin(2*PI/3)*RadiusEffector, 0,cos(4*PI/3)*RadiusEffector, sin(4*PI/3)*RadiusEffector, 0,], triangles='0 1 2')
    visualEffector.createObject('OglModel',src='@mesh')
    visualEffector.createObject('RigidMapping', index='0')
    
    
    # there is a relation between effector goal and E
   
    
    if inverse:
        effector = beamNode.createObject('PositionEffector', name='effector', template='Rigid3d', useDirections='0 1 1 0 0 0', indices=[0], effectorGoal=[4,1,-4,0,0,0,1])
        
        actuator1 = beamNode.createObject('SlidingActuator', template='Rigid3d', direction='0 0 0 0 1 0' , indices='1 2 3 4 5 6 7 8 9 10')
        actuator2 = beamNode.createObject('SlidingActuator', template='Rigid3d', direction='0 0 0 '+str(-sin(2*PI/3))+' '+str(cos(2*PI/3))+' 0' , indices='11 12 13 14 15 16 17 18 19 20')
        actuator3 = beamNode.createObject('SlidingActuator', template='Rigid3d', direction='0 0 0 '+str(-sin(4*PI/3))+' '+str(cos(4*PI/3))+' 0' , indices='21 22 23 24 25 26 27 28 29 30')
        
    return rootNode  


    
    

        
