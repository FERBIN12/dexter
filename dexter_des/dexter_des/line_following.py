from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image #thats how ros2 receives image information
from geometry_msgs.msg import Twist

import cv2

class line_follower(Node):

    def __init__(self):
        super().__init__('line_follower_node')
        self.camera_sub = self.create_subscription(Image,'/camera/image_raw',self.camera_cb,10)
        self.bridge=CvBridge() # enables connection between ros2 and cv2
        self.vel_msg = Twist()
        self.cmd_vel_pub = self.create_publisher(Twist,'/cmd_vel',10)


    def camera_cb(self, data):
        frame = self.bridge.imgmsg_to_cv2(data,'bgr8')
        frame = frame[290:479,130:400]  # we shorten the frame for better detection
        edged = cv2.Canny(frame,60,100)  # canny is a edge detector

        white_index =[]  #empty list for storing the edge lines
        mid_point_lines = 0
        for index,values in enumerate(edged[:][90]):
            if values == 255:
                white_index.append(index)
        print(white_index)

        if len(white_index) == 2:
            cv2.circle(img=edged,center= (white_index[0],90),radius=2,color=(255,0,0),thickness=1)
            cv2.circle(img=edged,center=(white_index[1],90),radius=2,color=(255,0,0),thickness=1)
            # then we take the midpoints of both the edge lines and and divide by 2 to get the mid point which is then used to 
            # follow the line
            mid_point_lines = int((white_index[0] + white_index[1]) / 2)  # this is the midpoint of both lines 
            cv2.circle(img=edged,center=(mid_point_lines,90),radius=3,color=(255,0,0),thickness=2)
            
        midpoint_robot = [133,90]  ## will give the midpoint of the rover wrt to that frame
        cv2.circle(img=edged,center=(midpoint_robot[0],midpoint_robot[1]),radius=3,color=(255,0,0),thickness=2)
        error = midpoint_robot[0] - mid_point_lines
        print(error)

        # adding the conditions based on our error values

        if error < 0:
            self.vel_msg.angular.z = -0.5
        else:
            self.vel_msg.angular.z = 0.5
        
        self.vel_msg.linear.x = 0.5
        self.cmd_vel_pub.publish(self.vel_msg)

        cv2.imshow('Frame',frame)
        cv2.imshow('Canny edge',edged)
        cv2.waitKey(1)

  
def main(args=None):
    rclpy.init(args=args)

    line_follower_sub = line_follower()

    rclpy.spin(line_follower_sub)
    line_follower_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()