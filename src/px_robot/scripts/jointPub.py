import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    trajs = [
        [0, 0, 0, 0, 0], 
        [0.2,0.4,0.7,0.1,0],
         [-0.7, 0,0.2, -1.4, 0],
        [0.8, 0.9, -0.6, 0.4, 0],
        [0, 0, 1.5, 3/4, 0]
    ]
    while not rospy.is_shutdown():
        for q in trajs:
            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
            point = JointTrajectoryPoint()
            point.positions = q
            point.time_from_start = rospy.Duration(0.9)
            state.points.append(point)
            pub.publish(state)
            print('published command')
            rospy.sleep(1.2)



if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass