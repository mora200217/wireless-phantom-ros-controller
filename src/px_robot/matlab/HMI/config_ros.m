function [] = config_ros(ROS_MASTER_URI)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
 
rosshutdown();
 rosinit(ROS_MASTER_URI); 
end