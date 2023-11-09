#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import numpy as np

def callback(data):
    rospy.loginfo("Received control u: %f", data.data)

def cell_node():
    rospy.init_node('cell_node', anonymous=True)
    rospy.Subscriber('u', Float64, callback)
    # ---------
    pub = rospy.Publisher('y', Float64, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        y = np.random.normal()  # You can calculate the value of 'y' here
        pub.publish(y)
        rospy.loginfo("Sending output y: %f", y)
        rate.sleep()
    # ---------
    rospy.spin()

if __name__ == '__main__':
    try:
        cell_node()
    except rospy.ROSInterruptException:
        pass
