# Hilti/Initial scripts

This folder contains utility scripts to interact with initial dataset artifacts.
Their main goal is to obtain unified data format which uses timestamps in naming:
```bash
clouds/
├── 123123.1.pcd
├── 123123.2.pcd
├── 123123.3.pcd
...
poses/
├── 123123.1.txt
├── 123123.2.txt
├── 123123.3.txt
...
```

Structure of folder:
```bash
hilti/initial/
├── get_missed_timestamps.py
├── prepare_clouds.py
└── prepare_poses.py
```

---

#### `hilti/initial/get_missed_timestamps.py` - for some reasons Hilti datasets doesn't have ground truth poses
for several point clouds. This scripts prints timestamps for which there is no GT poses.
```bash
initial_output/
└── poses.txt
initial_poses_converted/
├── 123123.1.txt
├── 123123.2.txt
├── 123123.3.txt
...
```

##### How can I run it?
```bash
python3 hilti/initial/get_missed_timestamps.py \
  --dataset PATH_TO_POINT_CLOUDS \
  --poses PATH_TO_POSES
```

---

#### `hilti/initial/prepare_clouds.py` - converts initial output clouds to timestamps naming
```bash
initial_output/
├── 123123.123123000.pcd
├── 123123.223123000.pcd
├── 123123.323123000.pcd
...
initial_clouds_converted/
├── 123123.1.pcd
├── 123123.2.pcd
├── 123123.3.pcd
...
```

##### How can I run it?
```bash
python3 hilti/initial/prepare_clouds.py \
  --dataset_input PATH_TO_INITIAL_POINT_CLOUDS_OUTPUT \
  --dataset_output PATH_TO_SAVE_CONVERTED_CLOUDS
```

---

#### `hilti/initial/prepare_poses.py` - produces poses files using given .txt file from Hilti website.
As it said before, for several point clouds there is no GT poses. For these timestamps GT pose
creates using the closest pose.
```bash
initial_output/
└── poses.txt
initial_poses_converted/
├── 123123.1.txt
├── 123123.2.txt
├── 123123.3.txt
...
```

##### How can I run it?
```bash
python3 hilti/initial/prepare_poses.py \
  --dataset PATH_TO_CONVERTED_POINT_CLOUDS \
  --poses PATH_TO_POSES_TXT_FILE \
  --poses_save_path PATH_TO_POSES_TO_SAVE
```

---
