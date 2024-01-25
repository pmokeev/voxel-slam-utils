# Hilti scripts

This folder contains utility scripts to interact with Hilti dataset.
Their main goal is to obtain unified data format which uses timestamps in naming:
```bash
clouds/
├── 123123.1.pcd
├── 123123.2.pcd
├── 123123.3.pcd
...
poses\
├── 123123.1.txt
├── 123123.2.txt
├── 123123.3.txt
...
```

Structure of folder:
```bash
hilti/
├── fast-lio
│   ├── prepare_clouds.py
│   └── prepare_poses.py
├── get_missed_timestamps.py
├── prepare_clouds.py
├── prepare_poses.py
└── visualize.py
```

The purpose of each script will be explained below.

---

`hilti/fast-lio/prepare_clouds.py` - converts FAST-LIO output clouds to timestamps naming
```bash
fast_lio_output/
├── scans_0.pcd
├── scans_1.pcd
├── scans_2.pcd
...
fast_lio_converted/
├── 123123.1.pcd
├── 123123.2.pcd
├── 123123.3.pcd
...
```

How can I run it?
```bash
python3 hilti/fast-lio/prepare_clouds.py \
  --dataset_input PATH_TO_FAST_LIO_OUTPUT \
  --dataset_output PATH_TO_SAVE_CONVERTED \
  --scan_states PATH_TO_SCAN_STATES_FILE
```

---

`hilti/fast-lio/prepare_poses.py` - takes scan_states.txt as input and produces poses in
```bash
r11 r12 r13 tx
r21 r22 r23 ty
r31 r32 r33 tz
0   0   0   1
```
format

How can I run it?
```bash
python3 hilti/fast-lio/prepare_poses.py \
  --scan_states PATH_TO_SCAN_STATES_FILE \
  --poses_save_path PATH_TO_FOLDER_TO_SAVE_POSES
```

---

`hilti/get_missed_timestamps.py` - for some reasons Hilti datasets doesn't have ground truth poses
for several point clouds. This scripts prints timestamps for which there is no GT poses.

How can I run it?
```bash
python3 hilti/get_missed_timestamps.py \
  --dataset PATH_TO_POINT_CLOUDS \
  --poses PATH_TO_POSES
```

---

`hilti/prepare_clouds.py` - formats naming of point clouds and leaves only one character after
point in timestamp. Example: `123123.1234000.pcd -> 123123.1.pcd`

How can I run it?
```bash
python3 hilti/prepare_clouds.py \
  --dataset_input PATH_TO_HILTI_POINT_CLOUDS \
  --dataset_output PATH_TO_FORMATTED_POINT_CLOUDS
```

---

`hilti/prepare_poses.py` - produces poses files using given .txt file from Hilti website.
As it said before, for several point clouds there is no GT poses. For these timestamps GT pose
creates using the closest pose.

How can I run it?
```bash
python3 hilti/prepare_poses.py \
  --dataset PATH_TO_HILTI_POINT_CLOUDS \
  --poses PATH_TO_POSES \
  --poses_save_path PATH_TO_POSES_TO_SAVE
```

---

`hilti/visualize.py` - visualizes point cloud using poses and IMU matrix, which could be provided in code.

How can I run it?
```bash
python3 hilti/visualize.py \
  --dataset PATH_TO_HILTI_POINT_CLOUDS \
  --poses PATH_TO_POSES \
  --start BEGINNING_OF_VISUALISING \
  --end END_OF_VISUALISING
```
