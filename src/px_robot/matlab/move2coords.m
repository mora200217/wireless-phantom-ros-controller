function [] = move2coords(coords, dura)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
    % config_ros("http://192.168.10.14:11311"); 
    pub = rospublisher("/joint_trajectory", "trajectory_msgs/JointTrajectory");
    msg = rosmessage("trajectory_msgs/JointTrajectory"); 
    
    time_now = rostime("now", "DataFormat", "object"); 
    
    msg.Header.Stamp = time_now;
    msg.JointNames = {'joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5'}; 
    
    pt = rosmessage("trajectory_msgs/JointTrajectoryPoint");
    
    pt.Positions = coords; 
    pt.TimeFromStart = rosduration(dura); 
    
    msg.Points = pt; 
    disp(pub)
    disp(coords)
    pub.send(msg); 
    

end