import open3d as o3d

import argparse
import os
import random

from hilti.utils.utils import get_lidar_to_imu, get_sorted, read_pose

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="VisualizePoses")
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--poses", type=str, required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    args = parser.parse_args()

    point_cloud = o3d.geometry.PointCloud(o3d.utility.Vector3dVector())
    point_clouds = get_sorted(args.dataset)[args.start : args.end]
    lidar_to_imu = get_lidar_to_imu()
    random.seed(42)

    for point_cloud_name in point_clouds:
        pose_name = point_cloud_name[: point_cloud_name.index(".") + 2] + ".txt"
        try:
            pose = read_pose(os.path.join(args.poses, pose_name)) @ lidar_to_imu
        except Exception as e:
            print(f"{pose_name} is missing due to {e}, using lidar-to-imu")
            pose = lidar_to_imu

        cloud = o3d.io.read_point_cloud(
            os.path.join(args.dataset, point_cloud_name)
        ).transform(pose)
        cloud.paint_uniform_color([random.random(), random.random(), random.random()])

        point_cloud += cloud

    o3d.visualization.draw(point_cloud)
