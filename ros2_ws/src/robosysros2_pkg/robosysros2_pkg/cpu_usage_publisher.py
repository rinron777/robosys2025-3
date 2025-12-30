import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class CpuUsagePublisher(Node):
    def __init__(self):
        super().__init__('cpu_usage_publisher')
        self.publisher_ = self.create_publisher(
            String,
            'robosys/cpu_usage',
            10
        )
        self.prev_idle = 0
        self.prev_total = 0
        self.timer = self.create_timer(1.0, self.timer_callback)

    def read_cpu_stat(self):
        with open('/proc/stat', 'r') as f:
            values = list(map(int, f.readline().split()[1:]))
        idle = values[3]
        total = sum(values)
        return idle, total

    def timer_callback(self):
        idle, total = self.read_cpu_stat()
        if self.prev_total == 0:
            self.prev_idle = idle
            self.prev_total = total
            return

        usage = 100.0 * (1.0 - (idle - self.prev_idle) / (total - self.prev_total))
        msg = String()
        msg.data = f'CPU Usage: {usage:.2f}%'
        self.publisher_.publish(msg)

        self.prev_idle = idle
        self.prev_total = total

def main():
    rclpy.init()
    node = CpuUsagePublisher()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass
    except rclpy.executors.ExternalShutdownException:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()

        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()

