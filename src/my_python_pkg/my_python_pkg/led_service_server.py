import rclpy
from rclpy.node import Node

from std_srvs.srv import SetBool
import RPi.GPIO as GPIO

class LedNode(Node):

    LED0 = 10
    LED1 = 9
    LED2 = 25

    LED_GPIO = LED0

    @property
    def log(self):
        return self.get_logger()

    def __init__(self):
        super().__init__('led_moderator')
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_GPIO, GPIO.OUT)

        self.srv = self.create_service(SetBool, 'set_led_state', self.set_led_state_callback)
        self.log.info("Service server started. Ready to get requests.")

    def set_led_state_callback(self, req, res):
        GPIO.output(self.LED_GPIO, req.data)
        res.success = True
        res.message = 'Successfully changed LED state'
        return res

    def destroy_node(self):
        GPIO.cleanup()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    node = LedNode()
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
