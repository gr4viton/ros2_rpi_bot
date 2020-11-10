from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    talker_node = Node(
        package="my_python_pkg",
        executable="but",
        name="the_dictator",
    )

    listener_node = Node(
        package="my_python_pkg",
        executable="led",
        name="a_sheep",
    )

    ld.add_action(talker_node)
    ld.add_action(listener_node)

    return ld

