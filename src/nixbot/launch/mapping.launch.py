import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
import xml.parsers.expat
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro


<launch>
  <node pkg="gmapping" type="slam_gmapping" name="slam_gmapping">
    <param name="base_frame" value="base_link"/>
    <param name="odom_frame" value="odom"/>
    <param name="map_frame" value="map"/>
    <param name="map_update_interval" value="5.0"/>
    <param name="maxUrange" value="10.0"/>
    <param name="maxRange" value="12.0"/>
    <param name="sigma" value="0.05"/>
    <param name="kernelSize" value="1"/>
    <param name="lstep" value="0.05"/>
    <param name="astep" value="0.05"/>
    <param name="iterations" value="5"/>
    <param name="lsigma" value="0.075"/>
    <param name="ogain" value="3.0"/>
    <param name="lskip" value="0"/>
    <param name="minimumScore" value="50.0"/>
    <param name="srr" value="0.1"/>
    <param name="srt" value="0.2"/>
    <param name="str" value="0.1"/>
    <param name="stt" value="0.2"/>
    <param name="linearUpdate" value="0.2"/>
    <param name="angularUpdate" value="0.1"/>
    <param name="temporalUpdate" value="-1.0"/>
    <param name="resampleThreshold" value="0.5"/>
    <param name="particles" value="30"/>
    <param name="xmin" value="-50.0"/>
    <param name="ymin" value="-50.0"/>
    <param name="xmax" value="50.0"/>
    <param name="ymax" value="50.0"/>
    <param name="delta" value="0.05"/>
    <param name="llsamplerange" value="0.01"/>
    <param name="llsamplestep" value="0.01"/>
    <param name="lasamplerange" value="0.005"/>
    <param name="lasamplestep" value="0.005"/>
  </node>

  <!-- Display for Laser Scan -->
  <node name="laser_scan_display" pkg="rviz" type="rviz" args="-d $(find rviz)/config/laser_scan.rviz" />

  <!-- Display for Map -->
  <node name="map_display" pkg="rviz" type="rviz" args="-d $(find rviz)/config/navigation.rviz" />
</launch>