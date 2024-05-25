import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Adjust based on the actual message type
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import pickle
import socket

class ProcessedPublisher(Node):
    def __init__(self):
        super().__init__('processed_publisher')
        self.subscription = self.create_subscription(Twist, '/cmd_vel',
            self.listener_callbace, 10)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('localhost', 50000))

    def listener_callbace(self, msg):
        self.get_logger().info(f"Received: {msg}")
        try:
            serialized_msg = pickle.dumps(msg)
            self.sock.sendall(serialized_msg)
        except BrokenPipeError:
            print("Connection broken, attempting to reconnect...")
            self.sock.close()
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('localhost', 50000))
            self.sock.sendall(serialized_msg)
        except Exception as e:
            print(f"An error occurred: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = ProcessedPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()