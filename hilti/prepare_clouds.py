import argparse
import os
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="PrepareHiltiClouds")
    parser.add_argument("--dataset_input", type=str, required=True)
    parser.add_argument("--dataset_output", type=str, required=True)
    args = parser.parse_args()

    for point_cloud_name in os.listdir(args.dataset_input):
        new_point_cloud_name = (
            point_cloud_name[: point_cloud_name.index(".") + 2] + ".pcd"
        )
        shutil.copy(
            os.path.join(args.dataset_input, point_cloud_name),
            os.path.join(args.dataset_output, new_point_cloud_name),
        )
