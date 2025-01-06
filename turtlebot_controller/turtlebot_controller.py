import rclpy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rclpy.node import Node
import time

class Turtle(Node):
	def __init__(self):
		super().__init__('turtlebot_controller')
		self.publisher_ = self.create_publisher(Twist, 'cmd_vel',10)
		self.subscriber_ = self.create_subscription(Odometry,'odom', self.odom_callback,10)
		self.turtle_vel = Twist()
		self.current_position = None
		
	def controll_turtle (self,x,y,z):
		try:
			self.turtle_vel.linear.x = x
			self.turtle_vel.linear.y = y
			self.turtle_vel.angular.z = z
			self.publisher_.publish(self.turtle_vel)
			
		except Exception as e:
			self.get_logger().info(f'Error...\n')
	
	
	def odom_callback (self,msg):
		try:
			self.current_position=msg.pose.pose.position
			self.get_logger().info (f'Actual position: x = {self.current_position.x}, y= {self.current_position.y}')
		except Exception as e:
			self.get_logger().info(f'Error...\n')
		
	def user_input(self):
		try:
			x = float(input("Choose linear velocity x: "))
			y = float(input("Choose linear velocity y: "))
			z = float(input("Choose angular velocity z: "))
			return x,y,z
		except ValueError:
			print("Non valid input. Please, try again...\n")
			return None, None, None
	
	def run(self):
		while rclpy.ok():
			x,y,z = self.user_input()
			if x is not None and y is not None and z is not None:
				self.controll_turtle(x,y,z)
				time.sleep(1)
				self.controll_turtle(0.0, 0.0,0.0)
				if self.current_position:
					rclpy.spin_once(self)
				else:
					print("Turtle is not moving!\n\n")

def main (args=None):
	rclpy.init(args=args)
	turtle = Turtle ()
	try:
		turtle.run()
	except Exception as e:
		print(f"Error: {e}")
	except KeyboardInterrupt:
		print("Interruption of the program...")
	finally:
		turtle.destroy_node()

if __name__=='__main__':
	main()
