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
        name="enlightened_sheep",
    )

    listener_node2 = Node(
        package="my_python_pkg",
        executable="mot",
        name="motorized_sheep",
    )

    ld.add_action(talker_node)
    # ld.add_action(listener_node)
    ld.add_action(listener_node2)

    return ld


