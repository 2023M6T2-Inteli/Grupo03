import cv2
import base64
import asyncio
from rclpy.node import Node
from ultralytics import YOLO
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
 
class Camera(Node):

  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(
      Image, 
      '/camera', 
      self.listener_callback, 
      10)
    self.subscription 
    self.bridge = CvBridge()

  def listener_callback(self, data):
    self.get_logger().info('Receiving video frame')
    current_frame = self.bridge.imgmsg_to_cv2(data)
    model = YOLO("./ai/best.pt")
    result = model.predict(current_frame, conf=0.6)
    annotated = result[0].plot()
    _, frames = cv2.imencode(".jpg", annotated)
    frame_base64 = base64.b64encode(frames).decode("utf-8")

