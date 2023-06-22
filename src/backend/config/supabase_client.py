import os
from dotenv import load_dotenv
from supabase import Client

load_dotenv()

class SupabaseClient(Client):
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        self.bucket_name = os.getenv("SUPABASE_BUCKET_NAME")
        super().__init__(supabase_url=self.url, supabase_key=self.key)

SupabaseClient()