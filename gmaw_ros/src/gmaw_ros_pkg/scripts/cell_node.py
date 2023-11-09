#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import numpy as np

def callback(data):
    rospy.loginfo("Received: %f", data.data)

def cell_node():
    rospy.init_node('cell_node', anonymous=True)
    rospy.Subscriber('u', Float32, callback)
    # ---------
    pub = rospy.Publisher('y', Float32, queue_size=10)
    fs = 1
    rate = rospy.Rate(fs)

    while not rospy.is_shutdown():
        y = np.random.normal()  # You can calculate the value of 'y' here
        pub.publish(y)
        rospy.loginfo("Sending: %f", y)
        rate.sleep()
    # ---------
    rospy.spin()

if __name__ == '__main__':
    try:
        cell_node()
    except rospy.ROSInterruptException:
        pass
