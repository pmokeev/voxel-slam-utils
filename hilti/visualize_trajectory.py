import open3d as o3d
from colour import Color

import argparse
import os
from typing import List

from visualize import get_imu, get_sorted, read_pose


def get_trajectory(path: str, color: List) -> List:
    imu = get_imu()
    poses = get_sorted(path)
    meshes = []

    for pose_name in poses:
        pose = read_pose(os.path.join(path, pose_name)) @ imu
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

    for poses_path, colour in zip(args.poses, args.colour):
        trajectories.extend(get_trajectory(poses_path, Color(colour).rgb))

    o3d.visualization.draw_geometries(trajectories)
