import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import serial

UWBData = serial.Serial('/dev/ttyUSB0' , 230400)
arduinoData = serial.Serial('/dev/ttyUSB1' , 9600)

class uwbSerialNode(Node):

    def __init__(self):
        super().__init__('uwb_ser_node')
        
        self.subscription = self.create_subscription(
        	String,
        	'serial_communication',
        	self.command_callback,
        	10
        )
        self.subscription
        
        self.get_logger().info("Serial node initialized")
        
        while True:
            uwb_bytes = UWBData.read(37)
            while (uwb_bytes[:4] != b'\xff\xff\xff\xff'):
                uwb_bytes = UWBData.read(37)
                self.get_logger().info("waiting UWB start bytes...")
            
            while (uwb_bytes[:4] == b'\xff\xff\xff\xff'):
                dist_byte = uwb_bytes[20:24]
                dist = int.from_bytes(dist_byte, byteorder='big', signed=False)
                angle_byte = uwb_bytes[24:26]
                angle = int.from_bytes(angle_byte, byteorder='big', signed=True)
                elev_byte = uwb_bytes[26:28]
                elev = int.from_bytes(elev_byte, byteorder='big', signed=True)
                self.get_logger().info(f"read dist: {dist} , angle: {angle}, elev; {elev}")
                uwb_bytes = UWBData.read(37)
        
    def command_callback(self,msg):
        self.get_logger().info("hear : %s" % msg.data)
    

def main(args=None):
    rclpy.init(args=args)

    uwb_serial_node = uwbSerialNode()

    rclpy.spin(uwb_serial_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    uwb_serial_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
