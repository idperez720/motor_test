#!/usr/bin/env python3

import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import String

#Define nombre de las entradas del puente H
ena = 18			
in1 = 23
in2 = 24

enb = 19
in3 = 6
in4 = 5

#configura los pines segun el microprocesador Broadcom
GPIO.setmode(GPIO.BCM)
#configura los pines como salidas
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
#Define las salidas PWM q
pwm_a = GPIO.PWM(ena,500)
pwm_b = GPIO.PWM(enb,500)
#inicializan los PWM con un duty Cicly de cero
pwm_a.start(0)
pwm_b.start(0)

#funciones de los motores
def Adelante():
    GPIO.output(in2,True)
    GPIO.output(in1,False)
    GPIO.output(in3,True)
    GPIO.output(in4,False)

def Reversa():
    GPIO.output(in2,False)
    GPIO.output(in1,True)
    GPIO.output(in3,False)
    GPIO.output(in4,True)


def callback(data):
    velocidad = int(data.data)
    rospy.loginfo(str(data.data))
    if velocidad < 0:
        velocidad = -1*velocidad
        Reversa() 
    else:
        Adelante()

    pwm_a.ChangeDutyCycle(velocidad)
    pwm_b.ChangeDutyCycle(velocidad)
   

def listener():
    rospy.init_node('motors_listener', anonymous=True)
    rospy.Subscriber('/motors_topic', String, callback)
    rospy.spin()
    GPIO.cleanup()

if __name__ == '__main__':
    listener()



