import rclpy
from rclpy.node import Node

class MyPythonNode(Node):
    def __init__(self):
        super().__init__("my_node_name")

        self.declare_parameter('my_str')
        self.declare_parameter('my_int')
        self.declare_parameter('my_double_array')

        self.declare_parameters(
            namespace='',
            parameters=[
                ('my_str2', None),
                ('my_int2', None),
                ('my_double_array2', None)
            ]
        )

        self.get_logger().info("This node just says 'Hello'")

def main(args=None):
    rclpy.init(args=args)

    node = MyPythonNode()
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()
