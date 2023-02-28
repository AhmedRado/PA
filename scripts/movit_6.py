def go_to_hand_pose(self):
    move_group = self.move_group
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position.x = self.x_position + 0.2
    pose_goal.position.y = self.y_position + 2.470692004698213
    pose_goal.position.z = self.z_position
    self.pub.publish(pose_goal)
    move_group.set_pose_target(pose_goal)
    move_group.set_start_state_to_current_state()
    success = move_group.go(wait=True)
    if(success):
        print("motion succeded")
    else:
        print("motion failed")
    move_group.stop()
    move_group.clear_pose_targets()