#!/usr/bin/env python3
import rospy
from visualization_msgs.msg import Marker
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Twist,Quaternion,Vector3,Pose,Point
from std_msgs.msg import Header,ColorRGBA
class TrajectoryInteractiveMarkers:
    def __init__(self):
        self.count = 0 
        rospy.Subscriber("/cmd_vel",Twist, self.event_in_cb)
        rospy.sleep(0.5)

    def event_in_cb(self,msg):
        self.waypoints = msg
        self.a = list()
        self.a.append(self.waypoints.linear.x)
        self.a.append(self.waypoints.linear.y)
        self.a.append(self.waypoints.linear.z)
        self.a.append(self.waypoints.angular.x)
        self.a.append(self.waypoints.angular.y)
        self.a.append(self.waypoints.angular.z)
        self.show_text_in_rviz()

    def show_text_in_rviz(self):
        self.marker = Marker()
        self.marker_publisher = rospy.Publisher('visualization_marker', Marker, queue_size=5)
        self.marker = Marker(
                    type=Marker.CUBE,
                    id=1,
                    lifetime=rospy.Duration(1000),
                    pose=Pose(Point(self.a[0]/10**5,self.a[1]/10**5,self.a[2]/10**5), Quaternion(0, 0, 0, 1)),
                    scale=Vector3(0.810, 0.510, 0.810),
                    header=Header(frame_id='base_link'),
                    color=ColorRGBA(0.0, 2.0, 0.0, 0.8))
        self.count+=1
        self.marker.id = self.count
        self.marker_publisher.publish(self.marker)

if __name__ == '__main__':
    rospy.init_node("trajectory_interactive_markers_node", anonymous=True)
    trajectory_interactive_markers = TrajectoryInteractiveMarkers()
    rospy.sleep(0.5)
    rospy.spin()