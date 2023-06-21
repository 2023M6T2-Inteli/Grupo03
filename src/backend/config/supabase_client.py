import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Carrega variáveis do arquivo .env
load_dotenv()

def SupabaseClient():
        return create_client(supabase_url=os.getenv("SUPABASE_URL"), supabase_key=os.getenv("SUPABASE_KEY"))

SupabaseClient()