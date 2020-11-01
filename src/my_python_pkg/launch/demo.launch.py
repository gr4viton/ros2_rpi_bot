from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    talker_node = Node(
        package="demo_nodes_cpp",
        executable="talker",
        name="the_dictator",
        remappings=[
            ("chatter", "secret_chat")
        ]
    )

    listener_node = Node(
        package="demo_nodes_py",
        executable="listener",
        name="a_sheep",
        remappings=[
            ("chatter", "secret_chat")
        ]
    )

    ld.add_action(talker_node)
    ld.add_action(listener_node)

    return ld
