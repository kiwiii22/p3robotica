import sim
import numpy as np
import time

def connect(port):
    sim.simxFinish(-1) 
    clientID=sim.simxStart('127.0.0.1',port,True,True,2000,5) 
    if clientID == 0: print("Conectado al puerto: ", port)
    else: print("La conexión ha fallado :(")
    return clientID

clientID = connect(19997)


# Obtenemos los manejadores 
ret,joint1=sim.simxGetObjectHandle(clientID,'Revolute_joint',sim.simx_opmode_blocking)
ret,joint2=sim.simxGetObjectHandle(clientID,'Revolute_joint0',sim.simx_opmode_blocking)
ret,joint3=sim.simxGetObjectHandle(clientID,'Prismatic_joint',sim.simx_opmode_blocking)

#Secuencia 1

q1 =90* np.pi/180
q2 =0* np.pi/180
q3=0.1
returnCode = sim.simxSetJointTargetPosition(clientID, joint1, q1, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint2, q2, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
time.sleep(2)

q1 =180* np.pi/180
q2 =0* np.pi/180
q3=0.1
returnCode = sim.simxSetJointTargetPosition(clientID, joint1, q1, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint2, q2, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
time.sleep(2)

q1 =200* np.pi/180
q2 =-120* np.pi/180
q3=0.1
returnCode = sim.simxSetJointTargetPosition(clientID, joint1, q1, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint2, q2, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
time.sleep(2)

q1 =70* np.pi/180
q2 =-120* np.pi/180
q3=0.1
returnCode = sim.simxSetJointTargetPosition(clientID, joint1, q1, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint2, q2, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
time.sleep(2)

q1 =-90* np.pi/180
q2 =-120* np.pi/180
q3=0.1
returnCode = sim.simxSetJointTargetPosition(clientID, joint1, q1, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint2, q2, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
time.sleep(2)

q1 =-90* np.pi/180
q2 =0* np.pi/180
q3=0.1
returnCode = sim.simxSetJointTargetPosition(clientID, joint1, q1, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint2, q2, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
time.sleep(2)

q1 =0* np.pi/180
q2 =0* np.pi/180
q3=0.1
returnCode = sim.simxSetJointTargetPosition(clientID, joint1, q1, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint2, q2, sim.simx_opmode_oneshot)
returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
time.sleep(2)