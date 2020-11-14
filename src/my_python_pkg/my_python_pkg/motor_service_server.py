import rclpy
from rclpy.node import Node

from std_srvs.srv import SetBool
import RPi.GPIO as GPIO

from enum import Enum

class MotorActionItem:
    name = None
    ins = None

    def __init__(self, name, enabled, in_states):
        self.name = name
        self.ins = [bool(state) for state in in_states]
        self.enabled = [bool(enabled), bool(enabled)]


class MotorAction(Enum):
    forward = MotorActionItem("forward", 1, [1, 0, 1, 0])
    back = MotorActionItem("back", 1, [0, 1, 0, 1])
    left = MotorActionItem("left", 1, [1, 0, 0, 1])
    right = MotorActionItem("right", 1, [0, 1, 1, 0])
    stop = MotorActionItem("stop", 0, [0, 0, 0, 0])

    @property
    def pin_values(self):
        vals = list(self.value.enabled)
        vals.extend(self.value.ins)
        return vals


class MotorControl:

    ENA = 13    # L298 EN_A
    ENB = 20    # L298 EN_B
    IN1 = 19    # 1
    IN2 = 16    # 2
    IN3 = 21    # 3
    IN4 = 26    # 4
    def __init__(self):
        self.init_pins()
        # GPIO.setwarnings(False)

    def init_pins(self):
        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    @property
    def pins(self):
        return [self.ENA, self.ENB, self.IN1, self.IN2, self.IN3, self.IN4]

    def set_action(self, action):
        for pin, value in zip(self.pins, action.pin_values):
            GPIO.output(pin, value)


class MotorsNode(Node):
    action = MotorAction.stop
    motors = None

    @property
    def log(self):
        return self.get_logger()

    def __init__(self):
        super().__init__("motor_moderator")
        GPIO.setmode(GPIO.BCM)
        self.motors = MotorControl()

        self.srv = self.create_service(
            SetBool, "set_led_state", self.set_action_callback
        )
        self.log.info("Service server started. Ready to get requests.")

    def set_action_callback(self, req, res):
        action = MotorAction.forward if bool(req.data) else MotorAction.back
        self.motors.set_action(action)
        res.success = True
        res.message = f"Successfully set motor {action.name}"
        self.log.info(res.message)
        return res

    def destroy_node(self):
        GPIO.cleanup()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    node = MotorsNode()
    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
