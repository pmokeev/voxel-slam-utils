import argparse
import os
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="PrepareFastLioClouds")
    parser.add_argument("--dataset_input", type=str, required=True)
    parser.add_argument("--dataset_output", type=str, required=True)
    parser.add_argument("--scan_states", type=str, required=True)
    args = parser.parse_args()

    with open(args.scan_states) as file:
        lines = file.readlines()
        for ind, line in enumerate(lines):
            timestamp = line.split(" ")[0]
            timestamp = timestamp[: timestamp.index(".") + 2]

            shutil.copy(
                os.path.join(args.dataset_input, f"scans_{ind + 1}.pcd"),
                os.path.join(args.dataset_output, f"{timestamp}.pcd"),
            )
