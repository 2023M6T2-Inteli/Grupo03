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
from sensor_msgs.msg import LaserScan
from pynput import keyboard

import sys
import termios
import tty

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Define a function to create a graph of nodes and edges with weights based on distance between nodes
def Graph():
    nodes = []
    WE = []
    G = nx.Graph()

    # Define a class for nodes with a name and x and y coordinates
    class Position_Node():
        def __init__(self, name, x, y):
            self.name = name
            self.x = x
            self.y = y
            nodes.append(self)

        def __repr__(self):
            return f"node{self.name}"

    # Define a function to create an edge between two nodes with a weight based on the distance between them
    def Weighed_Edge(p1, p2):
        weitgh = sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y))
        weitghEdge = (p1, p2, weitgh)
        WE.append(weitghEdge)

    # Prompt the user to input the coordinates of nodes and add them to the graph
    i = 1
    vn = []
    while True:
        x = float(input(f"Digite a coordenada x do nó {i}: "))
        y = float(input(f"Digite a coordenada y do nó {i}: "))
        node = Position_Node(i,x,y)
        vn.append((node.x,node.y))
        i += 1
        end = input("Voce quer adicionar algum nó? (y/n) ")
        if end == 'n' or end == 'N':
            break
    print(vn)

    print(nodes)
    G.add_nodes_from(nodes)

    # Prompt the user to input edges between nodes and add them to the graph with weights based on distance between nodes
    while True:
        end = input("Voce quer adicionar alguma aresta? (y/n)")
        if end == "n" or end == "N":
            break

        p1 = nodes[int(input(f"{vn} De que ponto voce quer adicionar a aresta? Digite a posição do ponto na lista. Considere que o primeiro ponto é o 0. "))]
        p2 = nodes[int(input(f"{vn} Com qual ponto voce quer conectar o ponto {p1}? Digite a posição do ponto na lista. Considere que o primeiro ponto é o 0. "))]
        Weighed_Edge(p1, p2)

    G.add_weighted_edges_from(WE)
    return (G, vn, nodes)

# Define a function to find the best path through all nodes in the graph using the traveling salesman problem algorithm from the networkx library
def best_path_all_nodes(graph, source):

    print(source)

    cycle = approx.traveling_salesman_problem(graph)

    path = [source]

    for i in range (len(cycle)-cycle.index(source)):
        path.append(cycle[cycle.index(source)+i])

    for i in range (cycle.index(source)+1):
        path.append(cycle[i])

    repeated = []
    for i in range (1,len(path)):
        if path[i-1] == path[i]:
            repeated.append(i-1)
    for i in repeated:
        path.pop(i)
    
    print(f"path:{path}")
    return path

# Define a class for controlling a turtle robot using rclpy to create a node that publishes Twist messages to the cmd_vel topic and subscribes to Odometry messages from the /odom topic
class TurtleController(Node):
    currentPose = []
    frontDist = []
    angleSet = False
    manual = False
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
        self.lidar_subscription = self.create_subscription(
            msg_type=LaserScan,
            topic = 'scan',
            callback = self.lidar_callback,
            qos_profile = 10
        )

        self.timer_ = self.create_timer(0.1, self.move_turtle)
        self.twist_msg_ = Twist()

    # Define a function to move the turtle robot along the path by publishing Twist messages to the cmd_vel topic based on the current position
    def move_turtle(self):
        if self.manual == True:
            comand = getch()
            if comand == "w":
                self.twist_msg_.linear.x -= 0.1
            if comand == "s":
                self.twist_msg_.linear.x = 0.0
                self.twist_msg_.angular.z = 0.0
            if comand == "x":
                self.twist_msg_.linear.x += 0.1
            if comand == "a":
                self.twist_msg_.angular.z += 0.1
            if comand == "d":
                self.twist_msg_.angular.z -= 0.1
            if comand == "k":
                self.manual = False
            self.publisher_.publish(self.twist_msg_)
            return
        print(f"fd = {self.frontDist}")
        if len(self.currentPose) == 0:
            return
        nextPose = self.path[0]
        print(f"np: {nextPose.x},{nextPose.y}")
        self.pose_subscription.callback
        print(f"cp: {self.currentPose}")
        dx = self.currentPose[0]-nextPose.x
        dy = self.currentPose[1]-nextPose.y
        ang = atan2(dy,dx)-self.currentPose[2]
        direction = ang/abs(ang)
        print(f"ang: {ang}")
        if self.angleSet == False:
            if (abs(dx)<0.1 and abs(dy)<0.1):
                self.path.pop(0)
                self.angleSet = False
            if ang > 0.01 or ang < -0.01:
                self.twist_msg_.linear.x = 0.0
                self.twist_msg_.angular.z = 0.1
            else:
                self.twist_msg_.angular.z = 0.0
                self.angleSet = True
                print("Angulo ajustado!")

        if self.angleSet:
            for i in self.frontDist:
                if i < 0.3:
                    self.twist_msg_.linear.x = 0.0
                    print(f"Encontrei um obstaculo {self.frontDist}")
                    self.publisher_.publish(self.twist_msg_)
                    self.angleSet = False
                    self.manual = True
                    return
            
            if (abs(dx)>0.1 or abs(dy)>0.1):
                self.twist_msg_.linear.x = -0.1

            else:
                self.twist_msg_.linear.x = 0.0
                self.path.pop(0)
                self.angleSet = False

        self.publisher_.publish(self.twist_msg_)

    # Define a callback function to update the current position of the turtle robot based on Odometry messages from the /odom topic
    def pose_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        ang = msg.pose.pose.orientation
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
        #self.get_logger().info(f"x={x}, y={y}, theta={theta}")
        self.currentPose = [x,y,theta]

    def lidar_callback(self, msg):
        front = (msg.angle_max)/(2*msg.angle_increment)
        self.frontDist = msg.ranges[int(front-17):int(front+17)]
        

# Define the main function to create a graph of nodes and edges, find the best path through all nodes, and control a turtle robot to move along the path using rclpy
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
