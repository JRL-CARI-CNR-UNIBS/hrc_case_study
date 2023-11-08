#!/usr/bin/env python3

import rospy
import geometry_msgs.msg
import tf
import numpy as np


def main():
    rospy.init_node('listener_example')

    listener = tf.TransformListener()
    rospy.sleep(1)
    frame_to_get = "/sfera_link"

    try:
        (trans, rot) = listener.lookupTransform('/camera_link',
                                                frame_to_get,
                                                rospy.Time(0))
        rospy.loginfo(f"Translation: {trans}")
        rospy.loginfo(f"Rotation: {rot}")

    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        rospy.loginfo(f"Frame: {frame_to_get}, non presente")

    trans_camera_obj = tf.transformations.translation_matrix(trans)
    rot_camera_obj = tf.transformations.quaternion_matrix(rot)

    print(f"Matrice translazione:\n {trans_camera_obj}")
    print(f"Matrice rotazione:\n {rot_camera_obj}")

    M_camera_obj = np.dot(trans_camera_obj, rot_camera_obj)

    print(f"M_camera_obj:\n {M_camera_obj}")

    rospy.sleep(1)
    try:
        (trans_cam, rot_cam) = listener.lookupTransform('/base_link',
                                                '/camera_link',
                                                rospy.Time(0))
        rospy.loginfo(f"Translation: {trans_cam}")
        rospy.loginfo(f"Rotation: {rot_cam}")
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        rospy.loginfo(f"Frame: camera_link, non presente")
        return 0

    trans_camera = tf.transformations.translation_matrix(trans_cam)
    rot_camera = tf.transformations.quaternion_matrix(rot_cam)

    print(f"Matrice translazione:\n {trans_camera}")
    print(f"Matrice rotazione:\n {rot_camera}")

    M_robot_camera = np.dot(trans_camera, rot_camera)
    print(f"M_robot_camera:\n {M_robot_camera}")

    M_robot_obj = np.dot(M_robot_camera, M_camera_obj)
    print(f"M_robot_obj:\n {M_robot_obj}")
    print(f"Object position (robot):\n {M_robot_obj[0:3,-1]}")

    quat_robot_obj= tf.transformations.quaternion_from_matrix(M_robot_obj)
    print(f"Quaternion (robot):\n {quat_robot_obj}")


if __name__ == '__main__':
    main()