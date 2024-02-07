import mrob
import numpy as np

import argparse
import os
from typing import Dict, Tuple

from hilti.utils import write_pose

__all__ = []


def increase_timestamp(timestamp: str) -> str:
    last_digit = int(timestamp[-1])
    if last_digit == 9:
        int_timestamp = int(timestamp.split(".")[0]) + 1
        return str(int_timestamp) + ".0"

    timestamp = timestamp[:-1] + str(last_digit + 1)
    return timestamp


def decrease_timestamp(timestamp: str) -> str:
    last_digit = int(timestamp[-1])
    if last_digit == 0:
        int_timestamp = int(timestamp.split(".")[0]) - 1
        return str(int_timestamp) + ".9"

    timestamp = timestamp[:-1] + str(last_digit - 1)
    return timestamp


def get_pose(line: str) -> Tuple[str, np.ndarray]:
    timestamp, x, y, z, tx, ty, tz, tw = list(map(float, line.split(" ")))
    R = mrob.geometry.quat_to_so3([tx, ty, tz, tw])
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = [x, y, z]

    timestamp = str(timestamp)
    timestamp = timestamp[: timestamp.index(".") + 2]

    return timestamp, T


def get_poses(poses_path: str) -> Dict[str, np.ndarray]:
    poses = dict()
    with open(poses_path) as file:
        lines = file.readlines()
        for line in lines:
            if line == "":
                continue
            timestamp, pose = get_pose(line)
            poses[timestamp] = pose

    return poses


def get_closest_pose(poses: Dict[str, np.ndarray], timestamp: str) -> np.ndarray:
    left_counter, right_counter = 0, 0
    left_timestamp, right_timestamp = timestamp, timestamp
    while right_timestamp not in poses:
        if right_counter > 1000:
            break
        right_timestamp = increase_timestamp(right_timestamp)
        right_counter += 1
    while left_timestamp not in poses:
        if left_counter > 1000:
            break
        left_timestamp = decrease_timestamp(left_timestamp)
        left_counter += 1

    closest_timestamp = left_timestamp
    if right_counter < left_counter:
        closest_timestamp = right_timestamp

    return closest_timestamp


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="PrepareHiltiPoses")
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--poses", type=str, required=True)
    parser.add_argument("--poses_save_path", type=str, required=True)
    args = parser.parse_args()

    poses = get_poses(args.poses)
    for point_cloud_name in os.listdir(args.dataset):
        point_cloud_name = point_cloud_name[: point_cloud_name.index(".") + 2]

        if point_cloud_name in poses.keys():
            pose = poses[point_cloud_name]
        else:
            closest_pose = get_closest_pose(poses, point_cloud_name)
            pose = poses[closest_pose]
            print(f"Missed: {point_cloud_name} -> {closest_pose}")

        write_pose(
            os.path.join(args.poses_save_path, str(point_cloud_name) + ".txt"), pose
        )
