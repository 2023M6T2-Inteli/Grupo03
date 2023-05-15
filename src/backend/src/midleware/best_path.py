#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from collections import deque
import networkx as nx
from networkx.algorithms import approximation as approx
import time
from math import *

def Graph():
    nodes = []
    WE = []
    G = nx.Graph()

    class Position_Node():
        def __init__(self, name, x, y):
            self.name = name
            self.x = x
            self.y = y
            nodes.append(self)

        def __repr__(self):
            return f"node{self.name}"

    def Weighed_Edge(p1, p2):
        weitgh = sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y))
        weitghEdge = (p1, p2, weitgh)
        WE.append(weitghEdge)
    
    #seting nodes
    i = 1
    vn = []
    while True:
        x = float(input(f"Digite a coordenada x do nó {i}: "))
        y = float(input(f"Digite a coordenada y do nó {i}: "))
        node  = Position_Node(i,x,y)
        vn.append((node.x,node.y))
        i += 1
        end = input("Voce quer adicionar algum nó? (y/n) ")
        if end == 'n' or end == 'N':
            break
        print(vn)

    print(nodes)
    G.add_nodes_from(nodes)

    while True:
        end = input("Voce quer adicionar alguma aresta? (y/n)")
        if end == "n" or end == "N":
            break
        
        p1 = nodes[int(input(f"{vn} De que ponto voce quer adicionar a aresta? Digite a posição do ponto na lista. Considere que o primeiro ponto é o 0.  "))]
        p2 = nodes[int(input(f"{vn} Com qual ponto voce quer conectar o ponto {p1}? Digite a posição do ponto na lista. Considere que o primeiro ponto é o 0.  "))]
        Weighed_Edge(p1, p2)
    
    G.add_weighted_edges_from(WE)
    return (G, vn, nodes)


    


# Função para encontrar o melhor caminho passando por todos os nós
def best_path_all_nodes(graph, source):

    print(source)
    # Encontrar um ciclo hamiltoniano aproximado usando o algoritmo Christofides
    cycle = approx.traveling_salesman_problem(graph)

    # Construir o caminho começando no nó de origem
    path = [source]

    # Adicionar os nós do ciclo após o nó de origem na ordem em que aparecem no ciclo
    for i in range (len(cycle)-cycle.index(source)):
        path.append(cycle[cycle.index(source)+i])

    # Adicionar os nós do ciclo antes do nó de origem na ordem em que aparecem no ciclo
    for i in range (cycle.index(source)+1):
        path.append(cycle[i])

    # Remover qualquer nó duplicado no caminho
    repeated = []
    for i in range (1,len(path)):
        if path[i-1] == path[i]:
            repeated.append(i-1)
    for i in repeated:
        path.pop(i)


    # Retornar o caminho
    return path

class TurtleController(Node):
    currentPose = []
    angleSet = False
    def __init__(self,path):
        self.path = path
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(
            msg_type=Twist, 
            topic='cmd_vel',
            qos_profile=10
        )
        self.pose_subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.pose_callback,
            qos_profile=10
        )
        self.timer_ = self.create_timer(0.1, self.move_turtle)
        self.twist_msg_ = Twist()
        

    def move_turtle(self):
        nextPose = self.path[0]
        print(nextPose)
        self.pose_subscription.callback
        print(self.currentPose)
        dx = self.currentPose[0]-nextPose.x
        dy = self.currentPose[1]-nextPose.y
        ang = atan2(dy,dx)-self.currentPose[2]
        direction = ang/abs(ang)
        print(ang)
        if self.angleSet == False:
            if abs(dx)<0.1 or abs(dy)<0.1:
                self.path.pop(0)
                return
            if abs(ang) > 0.01:
                self.twist_msg_.linear.x = 0.0
                self.twist_msg_.angular.z = 0.1*direction
            else:
                self.twist_msg_.angular.z = 0.0
                self.angleSet = True

        if self.angleSet:
            if abs(dx)>0.1 or abs(dy)>0.1:
                self.twist_msg_.linear.x = -0.1
            else:
                self.twist_msg_.linear.x = 0.0
                self.path.pop(0)
                self.angleSet = False
        
        self.publisher_.publish(self.twist_msg_)
    
    def pose_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        ang = msg.pose.pose.orientation
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
        self.get_logger().info(f"x={x}, y={y}, theta={theta}")
        self.currentPose = [x,y,theta]
        
        


def main(args=None):
    G = Graph()
    graph = G[0]
    nodes = G[2]
    p0 = int(input(f"{G[1]} De que ponto voce quer começar o percurso? Digite a posição do ponto na lista. Considere que o primeiro ponto é o 0"))
    path = best_path_all_nodes(graph, nodes[p0])
    rclpy.init()
    turtle_controller = TurtleController(path)
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()