import cv2
import rclpy
import base64
from rclpy.node import Node
from std_msgs.msg import String

class Camera(Node):
        
    def __init__(self, control_period=0.02):
        super().__init__('turtle_controller')
        
        self.control_timer = self.create_timer(
                timer_period_sec=1,
                callback=self.capture
        )

        self.camera = self.create_publisher(
                msg_type=String,
                topic='/camera',
                qos_profile=10
        )
    
    def capture(self):
        self.get_logger().info("Starting camera...")
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            encode_string= base64.b64encode(frame)
            string = str(encode_string)
            self.msg = String(data=string)
            self.camera.publish(self.msg)

# To see the output of this node, open a terminal and execute the following command:
# ros2 topic echo /camera