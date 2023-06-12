cmake_minimum_required(VERSION 3.0.2)
project(hrc_case_study_descriptions)
find_package(catkin REQUIRED COMPONENTS
ur_description
realsense2_description
robotiq_2f_85_gripper_visualization
)
catkin_package(
)

include_directories(
)
