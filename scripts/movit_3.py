import geometry_msgs.msg

planning_frame = move_group.get_planning_frame()
print("============ Planning frame: %s" % planning_frame)

eef_link = move_group.get_end_effector_link()
print("============ End effector link: %s" % eef_link)

group_names = robot.get_group_names()
print("============ Available Planning Groups:", group_names)

print("============ Printing robot state")
print(robot.get_current_state())
print("")
self.pub = rospy.Publisher("goal_position",geometry_msgs.msg.Pose,queue_size=1)