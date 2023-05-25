import cv2
import rclpy
import base64
from rclpy.node import Node
from ultralytics import YOLO
from std_msgs.msg import String

class Streaming(Node):
        
    def __init__(self, control_period=0.02):
        super().__init__('turtle_controller')

        self.streaming = self.create_subscription(String, '/camera', self.callback, 10)

    def callback(self, msg):
        print(msg)
        # decode = base64.b64decode(str(msg))
        # model = YOLO("./yolo/best.pt")
        # result = model.predict(decode, conf=0.4)
        # annotated = result[0].plot()
        # print(annotated)
        
if __name__ == '__main__':
    rclpy.init()
    streaming = Streaming()
    rclpy.spin(streaming)
    rclpy.shutdown()
