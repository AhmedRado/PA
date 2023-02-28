from math import pi

def go_to_start_state(self):
    move_group = self.move_group
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = 0  
    joint_goal[1] = -pi/2
    joint_goal[2] = pi/2
    joint_goal[3] = 0
    joint_goal[4] = 0
    joint_goal[5] = 0 
    move_group.set_max_acceleration_scaling_factor(1)
    move_group.set_max_velocity_scaling_factor(1)
    move_group.go(joint_goal, wait=True)
    move_group.stop()