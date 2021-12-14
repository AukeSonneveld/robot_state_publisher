#!/usr/bin/env python3

import rospy
from rospy.timer import sleep
import sensor_msgs
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

id = 0

if __name__ == '__main__':
    rospy.init_node("joint_state_publisher")
    pub = rospy.Publisher('different_joint_states', JointState, queue_size=10)

    while True:
        sleep(0.2)
        print("pu")
        h = Header()
        h.seq = id
        id += 1
        h.stamp = rospy.Time.now()

        js = JointState()
        js.header = h
        js.name = ["realsense_joint"]
        js.position = [0.0]
        js.velocity = [0.0]
        js.effort = [0.0]

        pub.publish(js)