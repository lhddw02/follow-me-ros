import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import serial

arduinoData = serial.Serial('/dev/ttyUSB0' , 9600)

class SubSerialNode(Node):

    def __init__(self):
        super().__init__('sub_node')
        
        self.subscription = self.create_subscription(
        	String,
        	'serial_communication',
        	self.command_callback,
        	10
        )
        self.subscription
        
        self.get_logger().info("Serial node initialized")
        
        
        while True:
            myCmd = input('please input command: ')
            myCmd = myCmd + '\r'
            arduinoData.write(myCmd.encode())
            self.get_logger().info("assigned : %s" % myCmd.data)
            self.get_logger().info("heard : %s" % msg.data)
        	
        
    
    def command_callback(self, msg):
    	self.get_logger().info("assigned : %s" % myCmd.data)
    	self.get_logger().info("heard : %s" % msg.data)
    



def main(args=None):
    rclpy.init(args=args)

    pub2arduino_sub_node = SubSerialNode()

    rclpy.spin(pub2arduino_sub_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pub2arduino_sub_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
