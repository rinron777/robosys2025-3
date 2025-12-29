#!/bin/bash
set -e

# ROS2 環境
source /opt/ros/humble/setup.bash

# ワークスペースへ移動（CI対応）
cd "$(dirname "$0")/../.."

# ビルド
colcon build --symlink-install

# 反映
source install/setup.bash

# listener 起動
timeout 5 ros2 run robosysros2_pkg cpu_usage_listener > /tmp/listener.log &
sleep 2

# publisher 起動
timeout 5 ros2 run robosysros2_pkg cpu_usage_publisher > /tmp/publisher.log &
sleep 3

# listener が受信しているか確認
grep "CPU Usage" /tmp/listener.log

