import Sofa
from math import sin,cos

#path = os.path.dirname(os.path.abspath(__file__))+'/'

#One of the problem is the dimensions


'''  Blocked force test for electronic conducting polymer, In this test we will create compression between the actuator and force sensor '''    

def createScene(rootNode):
    #for dt in range(0,5):
    
                rootNode.createObject('RequiredPlugin', name='SoftRobots')
                rootNode.createObject('RequiredPlugin', name='BeamAdapter')
                rootNode.createObject('RequiredPlugin', name='SofaPython')
                rootNode.createObject('VisualStyle', displayFlags='showVisualModels showBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields showInteractionForceFields hideWireframe')
                rootNode.findData('dt').value= 0.01
                rootNode.findData('gravity').value= '0 0 0'  # the gravity in mm  -9810  
                rootNode.createObject('BackgroundSetting', color='1 1 1')
                rootNode.createObject('OglSceneFrame', style="Arrows", alignment="TopRight")
                rootNode.createObject('FreeMotionAnimationLoop' )
                rootNode.createObject('GenericConstraintSolver', tolerance="1e-5", maxIterations="100")
                rootNode.createObject('PythonScriptController', classname="controller", filename="o.py")
                rootNode.createObject('CollisionPipeline', verbose="0", draw="0")
                rootNode.createObject('BruteForceDetection', name="N2")
                rootNode.createObject('NewProximityIntersection', name="Proximity", alarmDistance="0.00001", contactDistance="0.000005")
                rootNode.createObject('CollisionResponse', name="Response", response="default")

        
                
                
                
              
    
    
                ''' Beam FEM Model '''
                smawormNode = rootNode.createChild('SMAWorm')
                smawormNode.createObject('EulerImplicit')
                smawormNode.createObject('SparseLDLSolver', name='direct_solver')
                smawormNode.createObject('GenericConstraintCorrection', solverName='direct_solver')
                
                

                
                length = 10.716
                nbEdges =50
                edgesList = ""
                for i in range(0,nbEdges):
                    edgesList += str(i)+ " " + str(i+1) + " "
                    
                
                positionsList = ""
                for i in range(0,nbEdges+1):
                    dx = length/(nbEdges+1)
                    positionsList += str(dx*i)+ " 0 0 0 0 0 1 "
                
                smawormNode.createObject('Mesh', edges=edgesList)  ## the measurement at each edge will be different interms of position and force applied  and stiffness as well
                smawormNode.createObject('MechanicalObject', template='Rigid', position=positionsList, name='Frame')  
                smawormNode.createObject('BeamInterpolation')  # thickness 0.2 mm
                smawormNode.createObject('RestShapeSpringsForceField', name="MeasurementFF", points="0" , stiffness="100000e20",  recompute_indices="1", angularStiffness="100000e20" , drawSpring="1" , springColor="1 0 0 1")
        
                
                '''Electronic Conducting Polymer Layers'''

                speNode = smawormNode.createChild('SPE')  
                speNode.createObject('Mesh', edges=edgesList)
                speNode.createObject('BeamInterpolation', name='Interpol', crossSectionShape='rectangular', lengthY='2.167', lengthZ='0.2', defaultYoungModulus='0.8e6')  # thickness 0.2 mm
                speNode.createObject('AdaptiveBeamForceFieldAndMass',  name="BeamForceField", computeMass="1", massDensity="0.0016") #
                


                DOF0TransformNode = ""
                for i in range(0,nbEdges+1):
                    DOF0TransformNode += " 0 0 0.1 0 0 0 1 "
                cp_upNode = smawormNode.createChild('CP_up') 
                cp_upNode.createObject('Mesh', edges=edgesList)
                cp_upNode.createObject('BeamInterpolation', name='Interpol', crossSectionShape='rectangular', lengthY='2.167', lengthZ='0.025', defaultYoungModulus='0.6259e9', dofsAndBeamsAligned='0', DOF0TransformNode0=DOF0TransformNode, DOF1TransformNode1=DOF0TransformNode)
                cp_upNode.createObject('AdaptiveBeamForceFieldAndMass',  name="BeamForceField", computeMass="1", massDensity="0.0016")
                
                
                DOF0TransformNode = ""
                for i in range(0,nbEdges+1):
                    DOF0TransformNode += " 0 0 -0.1 0 0 0 1 "
                cp_downNode=smawormNode.createChild('CP_down')
                cp_downNode.createObject('Mesh', edges=edgesList)
                cp_downNode.createObject('BeamInterpolation', name='Interpol', crossSectionShape='rectangular', lengthY='2.167', lengthZ='0.025', defaultYoungModulus='0.6259e9', dofsAndBeamsAligned='0', DOF0TransformNode0=DOF0TransformNode, DOF1TransformNode1=DOF0TransformNode)
                cp_downNode.createObject('AdaptiveBeamForceFieldAndMass',  name="BeamForceField", computeMass="1", massDensity="0.0016")
                
        
                ''' Visualization of the Electronic conducting polymer '''
                
                visuNode = smawormNode.createChild('visualization')
                visuNode.createObject('RegularGridTopology', name='topology', n="10 4 2" , min="0 -0.3 -0.05", max="10.716 0.5 0.05")
                visuNode.createObject('MechanicalObject', name='test', src='@topology')
                visuNode.createObject('AdaptiveBeamMapping', interpolation="@../SPE/Interpol", input="@../Frame", output="@test")
                
                oglNode = visuNode.createChild('ogl')
                oglNode.createObject('OglModel', name='visualModel', color='0 1 0 1')
                oglNode.createObject('IdentityMapping')
                
                
                 
                visuNode2 = smawormNode.createChild('visualization2')
                visuNode2.createObject('RegularGridTopology', name='topology', n="10 4 2" , min="0 -0.3 -0.05", max="10.716 0.5 0.05")
                visuNode2.createObject('MechanicalObject', name='test', src='@topology')
                visuNode2.createObject('AdaptiveBeamMapping', interpolation="@../CP_up/Interpol", input="@../Frame", output="@test")
                
                oglNode2 = visuNode2.createChild('ogl')
                oglNode2.createObject('OglModel', name='visualModel', color='1 0 0 1')
                oglNode2.createObject('IdentityMapping')               
        
                
                visuNode3 = smawormNode.createChild('visualization3')
                visuNode3.createObject('RegularGridTopology', name='topology', n="10 4 2" , min="0 -0.3 -0.05", max="10.716 0.5 0.05")
                visuNode3.createObject('MechanicalObject', name='test', src='@topology')
                visuNode3.createObject('AdaptiveBeamMapping', interpolation="@../CP_down/Interpol", input="@../Frame", output="@test")
                
                oglNode3 = visuNode3.createChild('ogl')
                oglNode3.createObject('OglModel', name='visualModel', color='1 0 0 1')
                oglNode3.createObject('IdentityMapping')       
                
                
            
            
            
            
                ''' Mapped measured point to the electronic conducting polymer actuator '''
                
                
                Point= smawormNode.createChild('SMAPoint')
                Point.createObject('MechanicalObject', position='5 0 0', name='location')
                Point.createObject('AdaptiveBeamMapping', name="222000000")
                
                
                ''' Force sensor for measurement'''
                
                forceSensor=rootNode.createChild('ForceSensor')
                forceSensor.createObject('MechanicalObject', name='FS_MO', template='Rigid', position='5 0 0 0 0 0 1')
                forceSensor.createObject('UniformMass', totalMass='0') # for visual
                forceSensor.createObject('PythonScriptController', classname="controller", filename="controlForceSensor.py")
       
                '''first possibility penalty'''
                # smawormNode.createObject('RestShapeSpringsForceField', name="SensorPush", points="34" , stiffness="1e20", angularStiffness="0", external_rest_shape='@../ForceSensor/FS_MO', external_points='0', drawSpring='1', recompute_indices='false')
                
                '''second possibility constraints'''
                
                '''Sliding Points'''
                forceSensorPoint1=forceSensor.createChild('ForceSensorPoint1')
                forceSensorPoint1.createObject('MechanicalObject', name='point_MO', position='0 0 0' ) 
                forceSensorPoint1.createObject('RigidMapping', name='map')
                
                
                '''  Beam Points '''
                beamPoints2=smawormNode.createChild('beamPoint2')
                beamPoints2.createObject('Mesh')
                beamPoints2.createObject('MechanicalObject', name='point_MO',position='4.5 0  0 0 0 0 6 0 0')
                beamPoints2.createObject('AdaptiveBeamMapping')  
                
                
                # 3DOF constraint => only for small indentation...
                # rootNode.createObject('BilateralInteractionConstraint', template='Vec3', object1='@./ForceSensor/ForceSensorPoint1/point_MO', object2='@./SMAWorm/beamPoints2/point_MO', first_point='0', second_point='1')
                # 2 DOF constraint => better: no constraint alongx
                rootNode.createObject('SlidingConstraint',object1='@ForceSensor/ForceSensorPoint1/point_MO', object2='@SMAWorm/beamPoint2/point_MO', sliding_point='0', axis_1='0', axis_2='2')
                
                
                
                # there must be a compression between the force sensor and the actuator, so we will apply voltage in the negative direction and compression the force, the constrain here is  the compression between sensor and actuator.
                
                

                return rootNode



 
