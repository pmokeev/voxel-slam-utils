import numpy as np
import open3d as o3d
from colour import Color

import argparse
import os
from typing import List

from hilti.utils import (get_camera_to_lidar, get_lidar_to_imu, get_sorted,
                         read_pose)


def get_normalized_poses(path: str) -> List:
    lidar_to_imu = get_lidar_to_imu()
    camera_to_lidar = get_camera_to_lidar()
    poses = [read_pose(os.path.join(path, pose_name)) for pose_name in get_sorted(path)]

    if "orb" in path:
        poses = [
            np.linalg.inv(poses[0] @ lidar_to_imu @ camera_to_lidar)
            @ pose
            @ lidar_to_imu
            @ camera_to_lidar
            for pose in poses
        ]
    else:
        poses = [
            np.linalg.inv(poses[0] @ lidar_to_imu) @ pose @ lidar_to_imu
            for pose in poses
        ]

    return poses


def get_trajectory(poses: List[np.ndarray], color: List) -> List:
    meshes = [
        o3d.geometry.TriangleMesh.create_coordinate_frame().transform(pose)
        for pose in poses
    ]
    meshes = [mesh.paint_uniform_color(color) for mesh in meshes]

    return meshes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="VisualizeTrajectories")
    parser.add_argument("--poses", action="append", required=True)
    parser.add_argument("--colour", action="append", required=True)
    args = parser.parse_args()

    assert len(args.poses) == len(args.colour)

    trajectories = []

    for pose_path, color in zip(args.poses, args.colour):
        trajectories.extend(
            get_trajectory(get_normalized_poses(pose_path), Color(color).rgb)
        )

    o3d.visualization.draw_geometries(trajectories)
