import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState
 
class Battery(Node):
    def __init__(self):
        super().__init__('batterysubscriber')
        self.subscription = self.create_subscription(
            BatteryState,
            '/battery_state', 
            self.listener_callback, 
            10)

    def listener_callback(self, battery):
        relative_battery_percent = (battery.voltage - 11)/1.6
        return relative_battery_percent
        # O tópico está funcionando, falta apenas fazer a requisição post para o banco de dados.

def main():
    rclpy.init()
    battery = Battery()
    rclpy.spin(battery)
    rclpy.shutdown()

if __name__ == '__main__':
    main()