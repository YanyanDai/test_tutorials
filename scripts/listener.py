#!/usr/bin/env python
import rospy
from std_msgs.msg import String



    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    
    
    

    # spin() simply keeps python from exiting until this node is stopped


if __name__ == '__main__':
    listener()
