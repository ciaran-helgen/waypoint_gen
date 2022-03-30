#!/usr/bin/env python
import rospy
import time
from waypoint_navigator.srv import GoToWaypoint
from geometry_msgs.msg import Point

def call_service(waypoint):
  rospy.wait_for_service('/firefly/go_to_waypoint')
  try:
    go_to_waypoint = rospy.ServiceProxy('/firefly/go_to_waypoint', GoToWaypoint)
    go_to_waypoint.call(waypoint)
  except rospy.ServiceException as e:
    print("Service call failed: %s"%e)

if __name__ == '__main__':

  point = Point(x=0.0, y=0.0, z=1.0)
  points = [Point(x=0.0, y=0.0, z=1.0), Point(x=1, y=0.0, z=1.0), Point(x=1, y=1, z=1.0), Point(x=0, y=1, z=1.0)]
  # publish estimate at 1 Hz
  # Loop to publish pose estimate. Subscriber callbacks continue in background
  while not rospy.is_shutdown():
      try:
        for point in points:
          call_service(point)
          time.sleep(6)
      except rospy.ROSInterruptException:
          pass