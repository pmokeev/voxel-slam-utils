import argparse

import mrob
import numpy as np


def get_pose(line: str) -> np.ndarray:
    x, y, z, tx, ty, tz, tw = list(map(float, line.split(" ")))
    R = mrob.geometry.quat_to_so3([tx, ty, tz, tw])
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = [x, y, z]

    return T


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="PrepareBALMPoses")
    parser.add_argument("--alidar_poses", type=str, required=True)
    parser.add_argument("--output_poses", type=str, required=True)
    parser.add_argument("--poses_save_path", type=str, required=True)
    args = parser.parse_args()

    poses = []
    with open(args.output_poses) as file:
        lines = file.readlines()
        for line in lines:
            poses.append(get_pose(line))


