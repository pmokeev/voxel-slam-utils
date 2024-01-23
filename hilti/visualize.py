import argparse
import os
import sys
import random
import mrob, numpy as np

import open3d as o3d


def get_imu():
    # TODO: change values for specific IMU matrix
    R = mrob.geometry.quat_to_so3([0.7071068, -0.7071068, 0, 0])
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = [-0.001, -0.00855, 0.055]

    return T


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="VisualizePoses")
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--poses", type=str, required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    args = parser.parse_args()

    point_cloud = o3d.geometry.PointCloud(o3d.utility.Vector3dVector())
    point_clouds = get_sorted(args.dataset)[args.start:args.end]
    imu = get_imu()
    random.seed(42)

    for point_cloud_name in point_clouds:
        pose_name = point_cloud_name[:point_cloud_name.index(".") + 2] + ".txt"
        try:
            pose = read_pose(
                os.path.join(args.poses, pose_name)
            ) @ imu
        except:
            print(f"{pose_name} is missing, using IMU")
            pose = imu

        cloud = o3d.io.read_point_cloud(
            os.path.join(args.dataset, point_cloud_name)
        ).transform(pose)
        cloud.paint_uniform_color([random.random(), random.random(), random.random()])

        point_cloud += cloud

    o3d.visualization.draw(point_cloud)
