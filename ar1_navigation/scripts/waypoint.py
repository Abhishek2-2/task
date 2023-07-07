#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    
    lst = []

    n = int(input("Enter number of pose : "))

    # iterating till the range
    for i in range(0, n):
        ele = float(input())
        # adding the element
        lst.append(ele)

    print(lst)

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    for a in range(0,n,4):
        goal.target_pose.pose.position.x = lst[a]
        goal.target_pose.pose.position.y = lst[a+1]
        goal.target_pose.pose.orientation.z = lst[a+2]
        goal.target_pose.pose.orientation.w = lst[a+3]
        client.send_goal(goal)
        wait = client.wait_for_result()
        rospy.sleep(2)
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")