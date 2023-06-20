import rclpy
from subscribers.battery import Battery

class RobotController(Battery):
    def __init__(self):
        super().__init__("battery")
        self.battery = Battery(self, self.__battery_callback)

    def __battery_callback(self, data):  
        self.percentage = ((data.data - 11)/1.6) * 100
        event = {"name": "battery", "data": self.percentage}
        self.event_queue.put(event)
        self.new_scan.battery = self.percentage

def main(args=None):
    rclpy.init(args=args)
    battery_subscriber = BatterySubscriber()
    rclpy.spin(battery_subscriber)
    battery_subscriber.destroy_node()
    rclpy.shutdown()
  
if __name__ == '__main__':
  main()