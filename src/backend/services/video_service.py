from config.supabase_client import SupabaseClient

class VideoService():
    def __init__(self):
        self.client = SupabaseClient()
        self.local_path = "backend-ros/assets/routine.mp4"

    def upload(self, id):
        self.client.storage.from_(f"{self.client.bucket_name}").upload(f"routine_{id}.mp4", f"../{self.local_path}")

    def fetch_by_id(self, id):
        return self.client.storage.from_(f"{self.client.bucket_name}").get_public_url(f"routine_{id}.mp4")