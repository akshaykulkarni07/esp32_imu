import rospy
import os
import sys
import csv
from geometry_msgs.msg import Quaternion

def callback(data) :
    x_acc = data.x
    y_acc = data.y
    z_acc = data.z
    # getting time in ms, so divide by 1000
    timestamp = data.w / 1000
    data_out = [timestamp, x_acc, y_acc, z_acc]
    # print(timestamp, x_acc, y_acc, z_acc)
    with open(path, 'a') as wf :
        wrf = csv.writer(wf)
        wrf.writerow(data_out)

def save_readings() :
    # initialize node
    rospy.init_node('get_imu_readings', anonymous = True)

    # create subscriber object
    rospy.Subscriber('imu_data', Quaternion, callback)

    rospy.spin()

if __name__ == '__main__' :
    path = '../data/example_data.csv'
    save_readings()
