#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import numpy as np

def callback(data):
    rospy.loginfo("Received: %f", data.data)
    y.append(data.data)

if __name__ == '__main__':
    try:
        rospy.init_node('mpc_node', anonymous=True)
        rospy.Subscriber('y', Float32, callback)
        # ---------
        pub = rospy.Publisher('u', Float32, queue_size=10)
        fs = 1
        time_step = 1 / fs
        total_steps = 100
        rate = rospy.Rate(fs)
        sim_time = 0
        sim_steps = 0
        y = []
        while not rospy.is_shutdown():
            for i in range(100000000):
                pass
            u = np.random.normal()  # Example value for 'u'
            pub.publish(u)
            rospy.loginfo("Sending: %f", u)
            rate.sleep()
            sim_steps += 1
            sim_time += time_step
        # ---------
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
