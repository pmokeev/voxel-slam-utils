# ORB-SLAM scripts

This folder contains utility scripts to interact with orb slam artifacts.
Their main goal is to obtain unified data format which uses timestamps in naming:
```bash
poses\
├── 123123.1.txt
├── 123123.2.txt
├── 123123.3.txt
...
```

Structure of folder:
```bash
orb-slam/
└── prepare_poses.py
```

--- 

#### `orb-slam/prepare_poses.py` - converts ORB-SLAM output poses to timestamps naming
```bash
orb_slam_output/
└── CameraTrajectory.txt
orb_slam_poses/
├── 123123.1.txt
├── 123123.2.txt
├── 123123.3.txt
...
```

##### How can I run it?
```bash
python3 orb-slam/prepare_poses.py \
  --poses PATH_TO_CAMERA_TRAJECTORY_FILE \
  --poses_save_path PATH_TO_SAVE_CONVERTED_POSES
```
