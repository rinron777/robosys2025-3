import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/tiba07/robosys2025-3/ros2_ws/install/robosysros2_pkg'
