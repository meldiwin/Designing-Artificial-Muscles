import Sofa
from math import sin,cos

#path = os.path.dirname(os.path.abspath(__file__))+'/'

#One of the problem is the dimensions


##############################  stiffness Test #############################################    

def createScene(rootNode):
    
                rootNode.createObject('RequiredPlugin', name='SoftRobots')
                rootNode.createObject('RequiredPlugin', name='BeamAdapter')
                rootNode.createObject('RequiredPlugin', name='SofaPython')
                rootNode.createObject('VisualStyle', displayFlags='showVisualModels showBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields showInteractionForceFields hideWireframe')
                rootNode.findData('dt').value= dt =0.0001
                rootNode.findData('gravity').value= '0 9.8 0' 
                rootNode.createObject('BackgroundSetting', color='0 0.168627 0.211765')
                rootNode.createObject('OglSceneFrame', style="Arrows", alignment="TopRight")
                rootNode.createObject('PythonScriptController', classname="controller", filename="sim_diffu.py")
                
                smawormNode = rootNode.createChild('SMAWorm')
                smawormNode.createObject('EulerImplicit')
                smawormNode.createObject('SparseLDLSolver')
                
                
                length = 10.716
                nbEdges =10
                edgesList = ""
                for i in range(0,nbEdges):
                    edgesList += str(i)+ " " + str(i+1) + " "
                    
                
                positionsList = ""
                for i in range(0,nbEdges+1):
                    dx = length/(nbEdges+1)
                    positionsList += str(dx*i)+ " 0 0 0 0 0 1 "
                
                smawormNode.createObject('Mesh', edges=edgesList)  
                smawormNode.createObject('MechanicalObject', template='Rigid', position=positionsList, name='Frame') 
                smawormNode.createObject('BeamInterpolation')  
                
                smawormNode.createObject('ConstantForceField',name='SMAForce', points= "0 1 2 3 4 5 6 7 8 9", forces='0 0 0 0 0 0   0 0 0 0 0 0    0 0 0 0 0 0    0 0 0 0 0 0     0 0 0 0 0 0     0 0 0 0 0 0     0 0 0 0 0 0     0 0 0 0 0 0    0 0 0 0 0 0    0 0 0 0 0 0    ', arrowSizeCoef="0.001")
                smawormNode.createObject('RestShapeSpringsForceField', name="MeasurementFF", points="9" , stiffness="100000e100",  recompute_indices="1", angularStiffness="100000e100" , drawSpring="1" , springColor="1 0 0 1")
                
                
                            
                ################################## It doesnot make a big change in the system as it is dielectric layer and there is no big change in the displacement behavior, the displacement still in the same range

                speNode = smawormNode.createChild('SPE')  
                speNode.createObject('Mesh', edges=edgesList)
                speNode.createObject('BeamInterpolation', name='Interpol', crossSectionShape='rectangular', lengthY='2.167', lengthZ='0.2', defaultYoungModulus='0.8e6')   #### the change of SPE layer young Modulus it doesnot make a difference as it is dielectric  material.  
                speNode.createObject('AdaptiveBeamForceFieldAndMass',  name="BeamForceField", computeMass="1", massDensity="0.0016") 
                


                DOF0TransformNode = ""
                for i in range(0,nbEdges+1):
                    DOF0TransformNode += " 0 0 0.1 0 0 0 1 "
                cp_upNode = smawormNode.createChild('CP_up') 
                cp_upNode.createObject('Mesh', edges=edgesList)
                cp_upNode.createObject('BeamInterpolation', name='Interpol', crossSectionShape='rectangular', lengthY='2.167', lengthZ='0.025', defaultYoungModulus='1.2e10', dofsAndBeamsAligned='0', DOF0TransformNode0=DOF0TransformNode, DOF1TransformNode1=DOF0TransformNode)
                cp_upNode.createObject('AdaptiveBeamForceFieldAndMass',  name="BeamForceField", computeMass="1", massDensity="0.0016")
                
                
                DOF0TransformNode = ""
                for i in range(0,nbEdges+1):
                    DOF0TransformNode += " 0 0 -0.1 0 0 0 1 "
                cp_downNode=smawormNode.createChild('CP_down')
                cp_downNode.createObject('Mesh', edges=edgesList)
                cp_downNode.createObject('BeamInterpolation', name='Interpol', crossSectionShape='rectangular', lengthY='2.167', lengthZ='0.025', defaultYoungModulus='1.2e10', dofsAndBeamsAligned='0', DOF0TransformNode0=DOF0TransformNode, DOF1TransformNode1=DOF0TransformNode)
                cp_downNode.createObject('AdaptiveBeamForceFieldAndMass',  name="BeamForceField", computeMass="1", massDensity="0.0016")
                
                                
                
               
                #Mapping
                Point= smawormNode.createChild('SMAPoint')
                Point.createObject('MechanicalObject', position='5.2 0 0', name='location')
                Point.createObject('ConstantForceField',name='SMAForce', points= "0", forces='0 0 600', arrowSizeCoef="0.001")
                Point.createObject('AdaptiveBeamMapping', name="222000000")
                
                
                
                visuNode = smawormNode.createChild('visualization')
                visuNode.createObject('RegularGridTopology', name='topology', n="10 4 2" , min="0 -0.3 -0.05", max="10.716  0.5 0.05")
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

                return rootNode



 