#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('/motors_topic', String, queue_size=10)
    rospy.init_node('motors_talker', anonymous=True)
    rate = rospy.Rate(10) #10Hz
    velocidad = input('Ingresar Velocidad')
    while not rospy.is_shutdown():
        rospy.loginfo('Velocidad ingresada: ' + velocidad)
        pub.publish(velocidad)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass