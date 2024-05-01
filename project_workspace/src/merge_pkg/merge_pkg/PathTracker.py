# !usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped

class PathTracker(Node):
    def __init__(self):
        super().__init__('path_tracker')
        self.subscription = self.create_subscription(
            Path,
            '/pose',
            self.pose_callback,
            10)
        self.publisher = self.create_publisher(Path, '/path', 10)
        self.path = Path()

    def pose_callback(self, msg):
        pose_stamped = PoseStamped()
        pose_stamped.header = msg.header
        pose_stamped.pose = msg.pose.pose

        self.path.poses.append(pose_stamped)
        self.path.header.stamp = self.get_clock().now().to_msg()
        self.path.header.frame_id = 'map'

        self.publisher.publish(self.path)

def main(args=None):
    rclpy.init(args=args)
    path_tracker = PathTracker()
    rclpy.spin(path_tracker)
    path_tracker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()