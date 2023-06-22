import rclpy
from subscribers.battery import Battery

def main(args=None):
    rclpy.init(args=args)
    battery_subscriber = Battery()
    rclpy.spin(battery_subscriber)
    battery_subscriber.destroy_node()
    rclpy.shutdown()
  
if __name__ == '__main__':
  main()