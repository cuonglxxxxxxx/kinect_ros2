import os

import launch_ros
from launch_ros.actions.node import Node
from launch import LaunchDescription

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="kinect_ros2",
                executable="kinect_ros2_node",
                name="kinect_ros2",
                namespace="kinect",
            ),
        ]
    )
