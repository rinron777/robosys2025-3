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
    node = CpuUsageListener()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()

