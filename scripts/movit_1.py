import rospy
import moveit_commander

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("move_group", anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()