import rclpy
from rclpy.node import Node

from std_srvs.srv import SetBool
import RPi.GPIO as GPIO

class ButtonNode(Node):
    IR_R = 18
    IR_L = 27

    BUTTON_GPIO = IR_R

    @property
    def log(self):
        return self.get_logger()

    def __init__(self):
        super().__init__('button_monitor')

        self.cli = self.create_client(SetBool, "set_led_state")


        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(
            self.BUTTON_GPIO, GPIO.BOTH,
            callback=self.button_callback,
            bouncetime=100
        )

    def button_callback(self, channel):

        power_on_led = not GPIO.input(self.BUTTON_GPIO)
        self.log.info(f"button_callback = {power_on_led}")

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.req = SetBool.Request()
        self.req.data = power_on_led

        self.cli.call_async(self.req)

        #rospy.wait_for_service('set_led_state')
        #try:
        #    set_led_state = rospy.ServiceProxy('set_led_state', SetBool)
        #    resp = set_led_state(power_on_led)
        #except rospy.ServiceException, e:
        #    self.log.warn(e)

    def destroy_node(self):
        GPIO.cleanup()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    node = ButtonNode()
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
