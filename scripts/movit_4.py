from gazebo_msgs.msg import LinkStates

rospy.Subscriber("/gazebo/link_states",LinkStates,self.Palm_link_state_callback)

def Palm_link_state_callback(self,data:LinkStates):
    self.x_position = data.pose[16].position.x
    self.y_position = data.pose[16].position.y
    self.z_position = data.pose[16].position.z
    self.w_orientation = data.pose[16].orientation.w
    self.x_orientation = data.pose[16].orientation.x
    self.y_orientation = data.pose[16].orientation.y
    self.z_orientation = data.pose[16].orientation.z