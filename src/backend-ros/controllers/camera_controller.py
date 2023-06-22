import rclpy
from subscribers.camera import Camera

def main(args=None):
    rclpy.init(args=args)
    camera_subscriber = Camera()
    rclpy.spin(camera_subscriber)
    camera_subscriber.destroy_node()
    rclpy.shutdown()
  
if __name__ == '__main__':
  main()