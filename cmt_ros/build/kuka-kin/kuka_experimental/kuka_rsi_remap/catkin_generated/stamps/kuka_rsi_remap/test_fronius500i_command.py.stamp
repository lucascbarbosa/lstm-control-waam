#!/usr/bin/env python3
# license removed for brevity

import rospy
import time
from kuka_rsi_msgs.msg import Fronius500iCommand

def test():

    msg = Fronius500iCommand()

    ## CAUTION: welding_start activates arc ##
    msg.welding_start = False               ##
    ## CAUTION: welding_start activates arc ##

    msg.error_quit = False

    msg.gas_test = False
    msg.wire_forward = False

    msg.working_modes = 0

    msg.wire_feed_speed_command_value = 1.5
    msg.arc_length_correction = 0.0
    msg.dynamic_correction = 0.0
    msg.wire_retract_correction = 0.0

    msg.wire_backward = False
    msg.touch_sensing = False
    msg.torch_blow_out = False
    msg.process_line_selection = 0
    msg.welding_simulation = False
    msg.synchro_pulse_on = False

    msg.header.stamp = rospy.Time.now()

    pub.publish(msg)

if __name__ == '__main__':

    pub = rospy.Publisher('powersource_command', Fronius500iCommand, queue_size=1, latch=True)
    rospy.init_node('test_fronius500i_command', anonymous=True)

    time.sleep(0.2) # without this sleep, msg is published but callback of kuka_rsi_remap is not called

    try:
        test()
    except rospy.ROSInterruptException:
        pass
