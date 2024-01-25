import argparse
import os

from visualize import get_imu, read_pose, get_sorted
import open3d as o3d

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="VisualizeGroundTruthTrajectory")
    parser.add_argument("--poses", type=str, required=True)
    args = parser.parse_args()

    imu = get_imu()
    poses = get_sorted(args.poses)
    meshes = []

    for ind, pose_name in enumerate(poses):
        pose = read_pose(os.path.join(args.poses, pose_name)) @ imu
        mesh = o3d.geometry.TriangleMesh.create_coordinate_frame().transform(pose)
        meshes.append(mesh)

    o3d.visualization.draw(meshes)
