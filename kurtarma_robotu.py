import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class OtonomNode(Node):
    def __init__(self):
        super().__init__('otonom_node')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.cmd = Twist()

    def scan_callback(self, msg):
        # Robotun tam önündeki mesafe (orta nokta)
        on_mesafe = msg.ranges[len(msg.ranges) // 2]
        
        if on_mesafe < 0.8:  # Engel 80cm'den yakınsa
            self.get_logger().info('Engel Tespit Edildi! Donuyorum...')
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = 0.5 # Sola dön
        else:
            self.get_logger().info('Yol Temiz, Ilerliyorum...')
            self.cmd.linear.x = 0.2 # Yavasca ilerle
            self.cmd.angular.z = 0.0
        
        self.publisher.publish(self.cmd)

def main(args=None):
    rclpy.init(args=args)
    node = OtonomNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
