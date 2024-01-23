import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="PrepareHiltiClouds")
    parser.add_argument("--dataset", type=str, required=True)
    args = parser.parse_args()

    for point_cloud_name in os.listdir(args.dataset):
        new_point_cloud_name = point_cloud_name[:point_cloud_name.index(".") + 2] + ".pcd"
        os.rename(
            os.path.join(args.dataset, point_cloud_name),
            os.path.join(args.dataset, new_point_cloud_name),
        )
