#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from gazebo_msgs.msg import LinkStates
from math import pi

class move_robot_as_wrist():
    def __init__(self):
        ## First initialize `moveit_commander`_ and a `rospy`_ node:
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node("move_group", anonymous=True)

        ## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
        ## kinematic model and the robot's current joint states
        robot = moveit_commander.RobotCommander()

        ## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
        ## for getting, setting, and updating the robot's internal understanding of the
        ## surrounding world:
        scene = moveit_commander.PlanningSceneInterface()

        ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
        ## to a planning group (group of joints). 
        ## This interface can be used to plan and execute motions:
        group_name = "manipulator"
        move_group = moveit_commander.MoveGroupCommander(group_name)
        work_space = [-2.65, -2.65, 1.0, 2.65, 2.65, 2.65]
        move_group.set_workspace(work_space)

        ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
        ## trajectories in Rviz:
        display_trajectory_publisher = rospy.Publisher(
            "/move_group/display_planned_path",
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=20,
        )
            ## Getting Basic Information
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^
        # We can get the name of the reference frame for this robot:
        planning_frame = move_group.get_planning_frame()
        print("============ Planning frame: %s" % planning_frame)

        # We can also print the name of the end-effector link for this group:
        eef_link = move_group.get_end_effector_link()
        print("============ End effector link: %s" % eef_link)

        # We can get a list of all the groups in the robot:
        group_names = robot.get_group_names()
        print("============ Available Planning Groups:", group_names)

        # Sometimes for debugging it is useful to print the entire state of the
        # robot:
        print("============ Printing robot state")
        print(robot.get_current_state())
        print("")
        self.pub = rospy.Publisher("goal_position",geometry_msgs.msg.Pose,queue_size=1)
        sub = rospy.Subscriber("/gazebo/link_states",LinkStates,self.Palm_link_state_callback)
        

        # Misc variables
        self.box_name = ""
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names
        self.x_position = 0
        self.y_position = 0
        self.z_position = 0
        self.w_orientation = 0
        self.x_orientation = 0
        self.y_orientation = 0
        self.z_orientation = 0

    def Palm_link_state_callback(self,data:LinkStates):
        self.x_position = data.pose[16].position.x
        self.y_position = data.pose[16].position.y
        self.z_position = data.pose[16].position.z
        self.w_orientation = data.pose[16].orientation.w
        self.x_orientation = data.pose[16].orientation.x
        self.y_orientation = data.pose[16].orientation.y
        self.z_orientation = data.pose[16].orientation.z
        # self.go_to_hand_pose()
        print("x")
        print(data.pose[16].position.z)

    def go_to_start_state(self):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        move_group = self.move_group

        ## BEGIN_SUB_TUTORIAL plan_to_joint_state
        ##
        ## Planning to a Joint Goal
        ## ^^^^^^^^^^^^^^^^^^^^^^^^
        ## The Panda's zero configuration is at a `singularity <https://www.quora.com/Robotics-What-is-meant-by-kinematic-singularity>`_, so the first
        ## thing we want to do is move it to a slightly better configuration.
        ## We use the constant `tau = 2*pi <https://en.wikipedia.org/wiki/Turn_(angle)#Tau_proposals>`_ for convenience:
        # We get the joint values from the group and change some of the values:
        joint_goal = move_group.get_current_joint_values()
        # joint_goal[0] = 0
        # joint_goal[1] = -tau / 8
        # joint_goal[2] = 0
        # joint_goal[3] = -tau / 4
        # joint_goal[4] = 0
        # joint_goal[5] = tau / 6  # 1/6 of a turn
        # joint_goal[6] = 0

        joint_goal[0] = 0  
        joint_goal[1] = -pi/2
        joint_goal[2] = pi/2
        joint_goal[3] = 0
        joint_goal[4] = 0
        joint_goal[5] = 0  # 1/6 of a turn
        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        move_group.set_max_acceleration_scaling_factor(0.4)
        move_group.set_max_velocity_scaling_factor(0.4)
        move_group.go(joint_goal, wait=True)

        # Calling ``stop()`` ensures that there is no residual movement
        move_group.stop()


    def go_to_hand_pose(self):
        move_group = self.move_group
        
        ## Planning to a Pose Goal
        ## ^^^^^^^^^^^^^^^^^^^^^^^
        ## We can plan a motion for this group to a desired pose for the
        ## end-effector:
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.orientation.w = 0
        pose_goal.orientation.x = 0
        pose_goal.orientation.y = 0
        pose_goal.orientation.z = 0
        pose_goal.position.x = self.x_position + 0.2
        pose_goal.position.y = self.y_position + 2.470692004698213
        pose_goal.position.z = self.z_position
        self.pub.publish(pose_goal)
        move_group.set_pose_target(pose_goal)
        # move_group.set_max_acceleration_scaling_factor(0.4)
        # move_group.set_max_velocity_scaling_factor(0.4)

        ## Now, we call the planner to compute the plan and execute it.
        # `go()` returns a boolean indicating whether the planning and execution was successful.
        move_group.set_start_state_to_current_state()
        success = move_group.go(wait=True)
        if(success):
            print("motion succeded")
        else:
            print("motion failed")
        # Calling `stop()` ensures that there is no residual movement
        move_group.stop()
        # It is always good to clear your targets after planning with poses.
        # Note: there is no equivalent function for clear_joint_value_targets().
        move_group.clear_pose_targets()







def main():
    move = move_robot_as_wrist()
    rate = rospy.Rate(50)
    move.go_to_start_state()
    while not rospy.is_shutdown():
        move.go_to_hand_pose()
        rate.sleep






if __name__ == "__main__":
    main()