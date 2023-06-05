from math import atan2
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from fastapi import FastAPI
from models import Relatorio, create_client, create_supabase_client
import httpx
from fastapi.middleware.cors import CORSMiddleware

from embedded.modules.queue import Queue
from embedded.modules.stack import Stack

app = FastAPI()


schema_name = "public"  
table_name = "Relatorio"

#supafastgrupo3

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/relatorios")
async def create_relatorio(relatorio: Relatorio):
    supabase = create_supabase_client()
    
    try:

        response = supabase.table(table_name).insert(relatorio.dict()).execute()
        print(response)
        return response
    except httpx.HTTPError as e:
        return {"message": "Erro ao criar o relatório: " + str(e)}

@app.get("/relatorios")
async def get_relatorios():
    supabase = create_supabase_client()
    
    response = supabase.table(table_name).select("*").execute()
    
    return response


@app.get("/relatorios/{id}")
async def get_relatorios(id: int):
    supabase = create_supabase_client()
     
    response = supabase.table(table_name).select("*").eq('id', str(id)).limit(1).execute()
    print(id)
    return response

@app.post("/movimento/iniciar")
async def iniciar():
    controller.iniciar_movimento()
    return {"message": "Movimento iniciado"}

@app.post("/movimento/parar")
async def parar():
    controller.parar_movimento()
    return {"message": "Movimento parado"}

class Controller(Node):
    def __init__(self, queue, stack):
        super().__init__("papy")
        self.positions = {"x": 0.0, "y":0.0, "theta":0.0}
        self.goal = {"x": 0.0, "y":0.0, "theta":0.0}
        self.queue = queue
        self.stack = stack

        self.subscription = self.create_subscription(
            Odometry, '/odom', self.callback, 10)

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.02, self.publish_movement)

    def iniciar_movimento(self):
        velocity = Twist()
        velocity.linear.x = 0.5
        velocity.angular.z = 0.0
        self.publisher.publish(velocity)

    def parar_movimento(self):
        velocity = Twist()
        velocity.linear.x = 0.0
        velocity.angular.z = 0.0
        self.publisher.publish(velocity)

# Criação da instância do Controller (precisa adicionar ainda)
queue = Queue()
stack = Stack()
controller = Controller(queue, stack)