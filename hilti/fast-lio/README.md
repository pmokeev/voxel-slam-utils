# Hilti/FAST-LIO scripts

This folder contains utility scripts to interact with FAST-LIO artifacts.
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
hilti/fast-lio/
├── prepare_clouds.py
└── prepare_poses.py
```

--- 

#### `hilti/fast-lio/prepare_clouds.py` - converts FAST-LIO output clouds to timestamps naming
```bash
fast_lio_output/
├── scans_0.pcd
├── scans_1.pcd
├── scans_2.pcd
...
fast_lio_clouds_converted/
├── 123123.1.pcd
├── 123123.2.pcd
├── 123123.3.pcd
...
```

##### How can I run it?
```bash
python3 hilti/fast-lio/prepare_clouds.py \
  --dataset_input PATH_TO_FAST_LIO_OUTPUT \
  --dataset_output PATH_TO_SAVE_CONVERTED_CLOUDS \
  --scan_states PATH_TO_SCAN_STATE_TXT_FILE
```

---

#### `hilti/fast-lio/prepare_poses.py` - converts FAST-LIO output poses to timestamps naming
```bash
fast_lio_output/
├── scan_states.txt
fast_lio_poses/
├── 123123.1.txt
├── 123123.2.txt
├── 123123.3.txt
...
```

##### How can I run it?
```bash
python3 hilti/fast-lio/prepare_poses.py \
  --scan_states PATH_TO_SCAN_STATE_TXT_FILE \
  --poses_save_path PATH_TO_SAVE_CONVERTED_POSES
```
