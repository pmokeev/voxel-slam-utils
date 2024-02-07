import os

import mrob
import numpy as np

__all__ = [
    "get_lidar_to_imu",
    "get_camera_to_lidar",
    "get_sorted",
    "read_pose",
    "write_pose",
]


def get_lidar_to_imu():
    # TODO: change values for specific LIDAR-TO-IMU matrix (this one for Hilti2022)
    R = mrob.geometry.quat_to_so3([0.7071068, -0.7071068, 0, 0])
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = [-0.001, -0.00855, 0.055]

    return T


def get_camera_to_lidar():
    # TODO: change values for specific CAMERA-TO-LIDAR matrix (this one for Hilti2022)
    return np.array(
        [
            [0.00670802, 0.00242564, 0.99997456, 0.05126355],
            [0.99992642, 0.0100912, -0.00673218, 0.04539012],
            [-0.01010727, 0.99994614, -0.00235777, -0.01321491],
            [0, 0, 0, 1],
        ]
    )


def get_sorted(directory):
    with os.scandir(directory) as entries:
        sorted_entries = sorted(entries, key=lambda entry: entry.name)
        sorted_items = [entry.name for entry in sorted_entries]
    return sorted_items


def read_pose(path: str) -> np.ndarray:
    pose = np.eye(4)
    with open(path) as file:
        lines = file.readlines()
        for ind, line in enumerate(lines):
            pose[ind] = list(map(float, line.replace("\n", "").split(" ")))

    return pose


def write_pose(path: str, pose: np.ndarray):
    np.savetxt(path, pose)
