from config.supabase_client import SupabaseClient

SCHEMA_NAME = "public"  
TABLE_NAME = "Relatorio"

class ReportService():
    def __init__(self):
        self.client = SupabaseClient()
        self.service = self.client.table(TABLE_NAME)
        
    def create(self, report):
        return self.service.insert(report.dict()).execute()
    
    def fetch(self):
        return self.service.select("*").execute()
    
    def fetch_by_id(self, id):
        return self.service.select("*").eq('id', str(id)).limit(1).execute()