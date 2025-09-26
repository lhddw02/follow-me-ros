import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import serial

UWBData = serial.Serial('/dev/ttyUSB0' , 230400)
arduinoData = serial.Serial('/dev/ttyUSB1' , 9600)

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
            arduinoData.write(myCmd.encode())
            self.get_logger().info("assigned : %s" % myCmd.data)
            self.get_logger().info("heard : %s" % msg.data)
        	
        
    
    def command_callback(self, msg):
    	self.get_logger().info("assigned : %s" % myCmd.data)
    	self.get_logger().info("heard : %s" % msg.data)
    	
	def parseUWBdata(self,):
	    #uwb_bytes = UWBData.readline()
	    #uwb_str = uwb_bytes.decode('utf-8').strip()
	    #uwb_str = UWBData.readline()
	    
	    uwb_bytes = UWBData.read(17)
	    while (uwb_bytes[:4] != b'\xff\xff\xff\xff');
	        uwb_bytes = UWBData.read(17)
	        self.get_logger().info("waiting UWB start bytes...")
	    
	    dist_byte = uwb_bytes[20:24]
	    dist = int.from_bytes(dist_byte, byteorder='big', signed=False)
	    angle_byte = uwb_bytes[24:26]
	    angle = int.from_bytes(angle_byte, byteorder='big', signed=True)
	    elev_byte = uwb_bytes[26:28]
	    elev = int.from_bytes(elev_byte, byteorder='big', signed=True)
	        
	    uwb_str = uwb_bytes.decode('utf-8').strip()
    
    



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
