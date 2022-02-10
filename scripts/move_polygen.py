#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import radians

class MovePolygen():
    def __init__(self):
	rospy.init_node('GoForward',anonymous=False)
	#stop AIBot
	rospy.loginfo("To stop AIBot CTRL + c")

	#what function to call when you ctrol +c
	rospy.on_shutdown(self.shutdown)	
	
	#Create a publisher which can "talk" to AIBot and tell it to move
	self.cmd_vel = rospy.Publisher('aibot/cmd_vel', Twist, queue_size=10)
	#AIBot will stop if we do not keep telling it to move. 5Hz
	r = rospy.Rate(5);
	
        # Create two different Twist() variables. One for moving forward. One for turning 30 degree
        #move forward at 0.5m/s
	move_cmd = Twist()
        move_cmd.linear.x = 0.5
        move_cmd.angular.z = 0

        #turn at 30degree
        turn_cmd = Twist()
        turn_cmd.linear.x = 0.5
        turn_cmd.angular.z = radians(30)

        # Go forward for 2 seconds (10*5 Hz) then turn for 2 second
        while not rospy.is_shutdown():
            # go forward
            
            for i in range(0,10):
                rospy.loginfo("Going Straight")
                #publish the velocity
		self.cmd_vel.publish(move_cmd)
		#wait for 0.2 second(5Hz) and publish again
		r.sleep()
            for i in range(0,10):
                rospy.loginfo("Turning")
                #publish the velocity
		self.cmd_vel.publish(turn_cmd)
		#wait for 0.2 second (5Hz) and publish again
		r.sleep()

    def shutdown(self):
        #stop aibot
        rospy.loginfo("Stop AIBot")
	#a default twist has linear.x of 0 and angular.z of 0. So it will stop AIBot
	self.cmd_vel.publish(Twist())
	rospy.sleep(1)

if __name__ == '__main__':	
	try:	
	    MovePolygen()
	except:
	    rospy.loginfo("node terminated.")
