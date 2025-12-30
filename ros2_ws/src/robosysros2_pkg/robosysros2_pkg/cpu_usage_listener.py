# Copyright (c) 2025 Rintarou Matsunaga
# Licensed under the BSD 3-Clause License.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class CpuUsageListener(Node):
    def __init__(self):
        super().__init__('cpu_usage_listener')
        self.subscription = self.create_subscription(
            String,
            'robosys/cpu_usage',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f'Listen: {msg.data}')

def main():
    rclpy.init()
    node = CpuUsageListener()  # or Publisher

    try:
        rclpy.spin(node)

    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        pass

    finally:
        node.destroy_node()

    return 0

if __name__ == '__main__':
    main()

