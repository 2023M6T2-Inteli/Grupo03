import cv2 
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Camera(Node):
  def __init__(self):
    super().__init__('image_publisher')
    self.publisher_ = self.create_publisher(Image, '/camera', 10)
    timer_period = 0.001
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.cap = cv2.VideoCapture(0)
    self.bridge = CvBridge()
   
  def timer_callback(self):
    ret, frame = self.cap.read()
    if ret == True:
      self.publisher_.publish(self.bridge.cv2_to_imgmsg(frame))
    self.get_logger().info('Publishing video frame')
