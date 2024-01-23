import argparse
import os
from typing import List


def get_missed_timestamps(dataset_path: str, poses_path: str) -> List[str]:
    timestamps = set()
    with open(poses_path) as file:
        lines = file.readlines()
        for line in lines:
            timestamp = line.split(" ")[0]
            timestamp = timestamp[:timestamp.index(".") + 2]

            if timestamp in timestamps:
                print("There is collision in timestamps!")

            timestamps.add(timestamp)

    missed_timestamps = []
    for point_cloud_name in os.listdir(dataset_path):
        point_cloud_name = point_cloud_name[:point_cloud_name.index(".") + 2]
        if point_cloud_name not in timestamps:
            missed_timestamps.append(point_cloud_name)

    return missed_timestamps


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="MissedTimestamps")
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--poses", type=str, required=True)
    args = parser.parse_args()

    missed_timestamps = get_missed_timestamps(
        dataset_path=args.dataset,
        poses_path=args.poses,
    )

    for timestamp in missed_timestamps:
        print(f"Missed: {timestamp}")

    print(f"Total missed: {len(missed_timestamps)}")
