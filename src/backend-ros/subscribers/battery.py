import rclpy
import asyncio
import websockets
from rclpy.node import Node
from sensor_msgs.msg import BatteryState


class Battery(Node):
    def __init__(self):
        super().__init__('battery_subscriber')
        self.subscription = self.create_subscription(
            BatteryState,
            '/battery_state', 
            self.listener_callback, 
            10)
        
    async def send_battery_via_websocket(self, relative_battery_percent):
        async with websockets.connect("ws://localhost:8000/battery") as websocket:
            await websocket.send(relative_battery_percent)

    def listener_callback(self, battery):
        relative_battery_percent = (battery.voltage - 11)/1.6
        asyncio.get_event_loop().run_until_complete(self.send_battery_via_websocket(str(relative_battery_percent)))
        print(relative_battery_percent)

def main():
    rclpy.init()
    battery = Battery()
    rclpy.spin(battery)
    rclpy.shutdown()

if __name__ == '__main__':
    main()