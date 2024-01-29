import numpy as np
import open3d as o3d
from colour import Color

import argparse
import os
from typing import List

from hilti.utils.utils import (get_camera_to_lidar, get_lidar_to_imu,
                               get_sorted, read_pose)


def get_trajectory(path: str, color: List) -> List:
    lidar_to_imu = get_lidar_to_imu()
    camera_to_lidar = get_camera_to_lidar()
    poses = get_sorted(path)
    meshes = []

    zero_pose = read_pose(os.path.join(path, poses[0]))

    for pose_name in poses:
        if "orb" in path:
            pose = (
                np.linalg.inv(zero_pose @ lidar_to_imu @ camera_to_lidar)
                @ read_pose(os.path.join(path, pose_name))
                @ lidar_to_imu
                @ camera_to_lidar
            )
        else:
            pose = (
                np.linalg.inv(zero_pose @ lidar_to_imu)
                @ read_pose(os.path.join(path, pose_name))
                @ lidar_to_imu
            )
        mesh = o3d.geometry.TriangleMesh.create_coordinate_frame().transform(pose)
        mesh.paint_uniform_color(color)
        meshes.append(mesh)

    return meshes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="VisualizeTrajectories")
    parser.add_argument("--poses", action="append", required=True)
    parser.add_argument("--colour", action="append", required=True)
    args = parser.parse_args()

    assert len(args.poses) == len(args.colour)

    trajectories = []

    for pose_path, color in zip(args.poses, args.colour):
        trajectories.extend(get_trajectory(pose_path, Color(color).rgb))

    o3d.visualization.draw_geometries(trajectories)
