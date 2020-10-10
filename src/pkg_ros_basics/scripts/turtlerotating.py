#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PI = 3.1415926535897

def pose_callback(msg):
    print(msg.x, msg.y, msg.theta)
    #pass

def move():
	rospy.init_node('turtlerotating', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.linear.x = 1		
	vel_msg.angular.z = 0.5
	rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
	velocity_publisher.publish(vel_msg)
	count = 0

	while not rospy.is_shutdown():

		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		r = 2
		distance = 2*PI*r
		speed = 1

		#Loop to move the turtle in an specified distance
		while(current_distance < distance):
		    #Publish the velocity
		    velocity_publisher.publish(vel_msg)
		    #Takes actual time to velocity calculus
		    t1=rospy.Time.now().to_sec()
		    #Calculates distancePoseStamped
		    current_distance= speed*(t1-t0)
		    #print(current_distance)

		#After the loop, stops the robot
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		#Force the robot to stop
		velocity_publisher.publish(vel_msg)
		if current_distance > distance : break


		
if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass





