# Hilti scripts

This folder contains utility scripts to interact with Hilti dataset.
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
hilti/
├── fast-lio - Represents scripts to interfact with FAST-LIO artifacts
├── initial - Represents scripts to interfact with initial dataset artifacts
├── orb-slam - Represents scripts to interfact with ORB-SLAM artifacts
├── utils - Represents utility scripts to interfact with !!! 2022 DATASET !!!
├── visualize.py
└── visualize_trajectories.py
```

---

#### `hilti/visualize.py` - visualizes point cloud using poses

> [!WARNING]
> This script uses lidar-to-imu matrix from 2022 dataset. You have to specify it in hilti/utils/utils.py

##### How can I run it?
```bash
python3 hilti/visualize.py \
  --dataset PATH_TO_HILTI_POINT_CLOUDS \
  --poses PATH_TO_POSES \
  --start BEGINNING_OF_VISUALISING \
  --end END_OF_VISUALISING
```

---

#### `hilti/visualize_trajectories.py` - visualizes trajectories using poses and TriangleMesh object

> [!WARNING]
> This script uses lidar-to-imu, camera-to-lidar matrix from 2022 dataset. You have to specify it in hilti/utils/utils.py

##### How can I run it?
```bash
python3 hilti/visualize_trajectories.py \
  --poses PATH_TO_POSES \
  --colour NAME_OF_COLOUR_TO_VISUALISE_PREVIOUS_POSES (for example "green") \
  --poses ANOTHER_PATH_TO_POSES \
  --colour ANOTHER_NAME_OF_COLOUR_TO_VISUALISE_PREVIOUS_POSES (for example "blue") \
```
