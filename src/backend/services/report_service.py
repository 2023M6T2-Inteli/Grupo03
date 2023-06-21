from config.supabase_client import SupabaseClient

SCHEMA_NAME = "public"  
TABLE_NAME = "Relatorio"
# URL: str = "https://qeqhovaiuqfkrjywqayz.supabase.co"
# KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFlcWhvdmFpdXFma3JqeXdxYXl6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTAxNjgwOSwiZXhwIjoyMDAwNTkyODA5fQ.0tuA_64ZpGS8olQikZBDzacoWr1Hj-srdCe46-5Mq90"  

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