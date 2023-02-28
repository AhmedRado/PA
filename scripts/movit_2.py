group_name = "manipulator"
move_group = moveit_commander.MoveGroupCommander(group_name)
work_space = [-2.65, -2.65, 1.0, 2.65, 2.65, 2.65]
move_group.set_workspace(work_space)
