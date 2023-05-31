import cv2
import base64
import asyncio
import websockets
from rclpy.node import Node
from ultralytics import YOLO
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
 
class Streaming(Node):

  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(
      Image, 
      '/camera', 
      self.listener_callback, 
      10)
    self.subscription 
    self.bridge = CvBridge()
    self.websocket_url = "ws://localhost:8000/ws"
    self.websocket = websockets.connect(self.websocket_url)

  async def send_frame_via_websocket(self, frame_base64):
    async with self.websocket as websocket:
      await websocket.send(frame_base64)

  def listener_callback(self, data):
    self.get_logger().info('Receiving video frame')
    current_frame = self.bridge.imgmsg_to_cv2(data)
    model = YOLO("./yolo/best.pt")
    result = model.predict(current_frame, conf=0.6)
    annotated = result[0].plot()
    _, frames = cv2.imencode(".jpg", annotated)
    frame_base64 = base64.b64encode(frames).decode("utf-8")
    print ("início        " + frame_base64 + "        fim")
    asyncio.get_event_loop().run_until_complete(self.send_frame_via_websocket(frame_base64))


