#!/bin/bash

source /opt/ros/humble/setup.bash

cd "$(dirname "$0")/../.."

colcon build --symlink-install
source install/setup.bash

timeout 5 ros2 run robosysros2_pkg cpu_usage_listener > /tmp/listener.log &
sleep 2

timeout 5 ros2 run robosysros2_pkg cpu_usage_publisher > /tmp/publisher.log &
sleep 3

grep "CPU Usage" /tmp/listener.log || exit 1

