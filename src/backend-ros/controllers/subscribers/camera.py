import cv2
import base64
import asyncio
import websockets
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
    self.bridge = CvBridge()
    self.video_writer = None
    self.websocket_url = "ws://localhost:8000/frames"
    self.report_video_path = "./assets/routine.mp4"

  async def send_frame_via_websocket(self, frame_base64):
      async with websockets.connect(self.websocket_url) as websocket:
          await websocket.send(frame_base64)

  def video_storage(self, frame):
      if self.video_writer is None:
          height, width, _ = frame.shape
          self.video_writer = cv2.VideoWriter(
              self.report_video_path,
              cv2.VideoWriter_fourcc(*'mp4v'),
              10,
              (width, height)
          )
      self.video_writer.write(frame)
      
  def listener_callback(self, data):
    self.get_logger().info('Receiving video frame')
    current_frame = self.bridge.imgmsg_to_cv2(data)
    model = YOLO("./ai/best.pt")
    result = model.predict(current_frame, conf=0.6)
    annotated = result[0].plot()
    self.video_storage(annotated)
    _, frames = cv2.imencode(".jpg", annotated)
    frame_base64 = base64.b64encode(frames).decode("utf-8")
    asyncio.get_event_loop().run_until_complete(self.send_frame_via_websocket(frame_base64))
    self.get_logger().info(f'Receiving and sending frames: {frame_base64}')
    return frames