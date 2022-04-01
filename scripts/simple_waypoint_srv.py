#!/usr/bin/env python
import rospy
import time
from waypoint_navigator.srv import GoToWaypoints
from geometry_msgs.msg import Point

def call_service(waypoints):
  rospy.wait_for_service('/firefly/go_to_waypoint')
  try:
    go_to_waypoints = rospy.ServiceProxy('/firefly/go_to_waypoints', GoToWaypoints)
    go_to_waypoints.call(waypoints)
  except rospy.ServiceException as e:
    print("Service call failed: %s"%e)

if __name__ == '__main__':

  points1 = [Point(x=0, y=0, z=2.0), Point(x=-1, y=-1, z=2.0)]
  points2 = [Point(x=-2, y=-2, z=2.0), Point(x=0.0, y=0.0, z=2.0)]
  # publish estimate at 1 Hz
  # Loop to publish pose estimate. Subscriber callbacks continue in background
  called = 0
  while not rospy.is_shutdown():
      try:
        if called == 0:
          call_service(points1)
          time.sleep(2)

          call_service(points2)
          called = 1
        
      except rospy.ROSInterruptException:
          pass