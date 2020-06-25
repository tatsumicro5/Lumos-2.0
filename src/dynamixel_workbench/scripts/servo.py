#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# created by: tatsumi
# update    : 2020.06.25
#

# Built-in/Generic Imports
import json
import threading
import time
import random

# Libs
import rospy

# Own Modules

# ROS Messages/Services
from dynamixel_workbench_msgs.srv import DynamixelCommand


# this class has servo methods.
class Servo:

    # Initialize
    def __init__(self):
        self.service = '/dynamixel_workbench/dynamixel_command'
        self.method = rospy.ServiceProxy(self.service, DynamixelCommand)
    
    
    # ROS Service Client
    def command(self, command="", id=0, addr_name="", value=0):
        rospy.wait_for_service(self.service)
        try:
            res = self.method(command, id, addr_name, value)
            return res.comm_result
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
    
    
    # Move Servo
    def move(self, id, value):
        return command(id=id, value=value)


# Usage Sample
if __name__ == '__main__':
    # initialize Servo class.
    servo = Servo()
    
    # move servo id:1
    servo.move(1, 200)
    
