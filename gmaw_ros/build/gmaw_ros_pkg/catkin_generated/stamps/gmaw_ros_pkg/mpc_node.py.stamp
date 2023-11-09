#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo("Received output y: %f", data.data)

def mpc_node():
    rospy.init_node('mpc_node', anonymous=True)
    rospy.Subscriber('y', Float64, callback)
    # ---------
    pub = rospy.Publisher('u', Float64, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        u = 42.0  # Example value for 'u'
        pub.publish(u)
        rospy.loginfo("Sending control u: %f", u)
        rate.sleep()
    # ---------
    rospy.spin()

if __name__ == '__main__':
    try:
        mpc_node()
    except rospy.ROSInterruptException:
        pass
