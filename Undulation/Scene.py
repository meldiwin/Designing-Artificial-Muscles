import Sofa
from math import sin,cos

#path = os.path.dirname(os.path.abspath(__file__))+'/'


def createScene(rootNode):
    
                rootNode.createObject('RequiredPlugin', name='SoftRobots')
                rootNode.createObject('RequiredPlugin', name='SofaPython')
                rootNode.createObject('RequiredPlugin', name='BeamAdapter')
                rootNode.createObject('VisualStyle', displayFlags='showVisualModels showBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields showInteractionForceFields hideWireframe')
            
                rootNode.findData('dt').value= 0.01
                rootNode.findData('gravity').value= '0 0 -9.81'
                
                rootNode.createObject('FreeMotionAnimationLoop');
                #rootNode.createObject('GenericConstraintSolver', tolerance='1e-15', maxIterations='1e4');
                rootNode.createObject('LCPConstraintSolver',  tolerance='1e-15', maxIt='1e4')
                rootNode.createObject('CollisionPipeline', verbose="0")
                rootNode.createObject('BruteForceDetection', name="N2")
                rootNode.createObject('CollisionResponse', response="FrictionContact")
                rootNode.createObject('LocalMinDistance', name="Proximity", alarmDistance="2", contactDistance="0.5")
            
                rootNode.createObject('BackgroundSetting', color='0 0.168627 0.211765')
                rootNode.createObject('OglSceneFrame', style="Arrows", alignment="TopRight")
                
                rootNode.createObject('PythonScriptController', classname="controller", filename="test.py")
                
                #rootNode.createObject('PythonScriptController', classname="controller", filename="InterpolationController.py")
                
                smawormNode = rootNode.createChild('SMAWorm')
                
                smawormNode.createObject('EulerImplicit')
                smawormNode.createObject('PCGLinearSolver', preconditioners='linearSolver')
                smawormNode.createObject('BTDLinearSolver', name='linearSolver')
                smawormNode.createObject('GenericConstraintCorrection', solverName='linearSolver')
                
                smawormNode.createObject('Mesh', edges='0 1  1  2  2 3  3 4   4 5')
                
                smawormNode.createObject('MechanicalObject', template='Rigid', position='0 0 0 0 0 0 1   10 0 0 0 0 0 1   20 0 0 0 0 0 1   30 0 0 0 0 0 1   40 0 0 0 0 0 1   50 0 0 0 0 0 1  ')
                
                smawormNode.createObject('BeamInterpolation', name='Interpol', crossSectionShape='rectangular', lengthY='1', lengthZ='0.1', defaultYoungModulus='2e8') 
                
                smawormNode.createObject('AdaptiveBeamForceFieldAndMass', name='ff', interpolation='@Interpol', massDensity='0.01')
                
                smawormNode.createObject('ConstantForceField',name='SMAForce', forces='0 0 0 0 0 0    0 0 0 0 0 0   0 0 0 0 0 0   0 0 0 0 0 0    0 0 0 0 0 0   0 0 0 0 0 0 ' )
                #smawormNode.createObject('FixedConstraint', indices='5')
                
                smawormNode.createObject('UniformMass', totalmass='10')
                
                
                
            
                visualNode=smawormNode.createChild('Visual0')
                visualNode.createObject('MeshObjLoader', filename='mesh/cube.obj', name='loader' ) 
                visualNode.createObject('Mesh', src='@loader')
                visualNode.createObject('MechanicalObject', template='Vec3d', name='mm0', scale="1")
                visualNode.createObject('Triangle')
                visualNode.createObject('Line')
                visualNode.createObject('Point')
                #visualNode.createObject('OglModel')
                visualNode.createObject('RigidMapping', index='0')
                visualNode.createObject('UniformMass', totalmass='0.7')
            
                
                visualNode=smawormNode.createChild('Visual1')
                visualNode.createObject('MeshObjLoader', filename='mesh/cube.obj', name='loader' ) 
                visualNode.createObject('Mesh', src='@loader')
                visualNode.createObject('MechanicalObject', template='Vec3d', name='mm1', scale="1")
                visualNode.createObject('Triangle')
                visualNode.createObject('Line')
                visualNode.createObject('Point')
                #visualNode.createObject('OglModel')
                visualNode.createObject('RigidMapping', index='1')
                visualNode.createObject('UniformMass', totalmass='0.1')
                               
                
                visualNode=smawormNode.createChild('Visual2')
                visualNode.createObject('MeshObjLoader', filename='mesh/cube.obj', name='loader' ) 
                visualNode.createObject('Mesh', src='@loader')
                visualNode.createObject('MechanicalObject', template='Vec3d', name='mm2', scale="1")
                visualNode.createObject('Triangle')
                visualNode.createObject('Line')
                visualNode.createObject('Point')
                #visualNode.createObject('OglModel')
                visualNode.createObject('RigidMapping', index='2')
                visualNode.createObject('UniformMass', totalmass='0.2')
                
                
                visualNode=smawormNode.createChild('Visual3')
                visualNode.createObject('MeshObjLoader', filename='mesh/cube.obj', name='loader' ) 
                visualNode.createObject('Mesh', src='@loader')
                visualNode.createObject('MechanicalObject', template='Vec3d', name='mm3', scale="1")
                visualNode.createObject('Triangle')
                visualNode.createObject('Line')
                visualNode.createObject('Point')
                #visualNode.createObject('OglModel')
                visualNode.createObject('RigidMapping', index='3')
                visualNode.createObject('UniformMass', totalmass='0.3')
                               
                
                visualNode=smawormNode.createChild('Visual4')
                visualNode.createObject('MeshObjLoader', filename='mesh/cube.obj', name='loader' ) 
                visualNode.createObject('Mesh', src='@loader')
                visualNode.createObject('MechanicalObject', template='Vec3d', name='mm4', scale="1")
                visualNode.createObject('Triangle')
                visualNode.createObject('Line')
                visualNode.createObject('Point')
                #visualNode.createObject('OglModel')
                visualNode.createObject('RigidMapping', index='4')
                visualNode.createObject('UniformMass', totalmass='0.2')
                

                visualNode=smawormNode.createChild('Visual5')
                visualNode.createObject('MeshObjLoader', filename='mesh/cube.obj', name='loader' ) 
                visualNode.createObject('Mesh', src='@loader')
                visualNode.createObject('MechanicalObject', template='Vec3d', name='mm5', scale="1")
                visualNode.createObject('Triangle')
                visualNode.createObject('Line')
                visualNode.createObject('Point')
                #visualNode.createObject('OglModel')
                visualNode.createObject('RigidMapping', index='5')
                visualNode.createObject('UniformMass', totalmass='0.5')

            
                groundNode = rootNode.createChild('Ground')
                groundNode.createObject('RegularGrid', min="-10 -30 -2", max="100 30 -2",  n="2 2 0", name="mesh")
                groundNode.createObject('MechanicalObject', template='Vec3d', name='mm_ground')
                groundNode.createObject('Triangle')
                groundNode.createObject('Line')
                groundNode.createObject('Point')
   
                
                   

                return rootNode



 
