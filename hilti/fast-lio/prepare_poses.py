import argparse
import os
from typing import Tuple
import mrob

import numpy as np


def get_pose(line: str) -> Tuple[str, np.ndarray]:
    timestamp, x, y, z, tx, ty, tz, tw = list(map(float, line.split(" ")[:8]))

    R = mrob.geometry.quat_to_so3([tx, ty, tz, tw])
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = [x, y, z]

    timestamp = str(timestamp)
    timestamp = timestamp[:timestamp.index(".") + 2]

    return timestamp, T


def write_pose(path: str, pose: np.ndarray):
    with open(path, "w+") as file:
        for ind, pose_line in enumerate(pose):
            file.write(" ".join(str(x) for x in pose_line))

            if ind != pose.shape[0]:
                file.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="PrepareFastLioPoses")
    parser.add_argument("--scan_states", type=str, required=True)
    parser.add_argument("--poses_save_path", type=str, required=True)
    args = parser.parse_args()

    with open(args.scan_states) as file:
        lines = file.readlines()
        for line in lines:
            timestamp, pose = get_pose(line)
            write_pose(
                os.path.join(args.poses_save_path, f"{timestamp}.txt"),
                pose,
            )
