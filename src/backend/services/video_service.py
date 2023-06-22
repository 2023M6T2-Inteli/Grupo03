import datetime
from dotenv import load_dotenv
from config.supabase_client import SupabaseClient

class VideoService():
    def __init__(self):
        self.client = SupabaseClient()
        self.local_path = "backend-ros/assets/routine.mp4"

    def set_output_filename(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.output = f"routine_{timestamp}.mp4"
        return self.output

    def upload(self):
        self.client.storage.from_(f"{self.client.bucket_name}").upload(f"{self.set_output_filename()}", f"../{self.local_path}")