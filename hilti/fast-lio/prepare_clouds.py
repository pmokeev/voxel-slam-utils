import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="PrepareFastLioClouds")
    parser.add_argument("--dataset", type=str, required=True)
    args = parser.parse_args()

    with open(args.dataset) as file:
        lines = file.readlines()
        for ind, line in enumerate(lines):
            timestamp = line.split(" ")[0]
            timestamp = timestamp[:timestamp.index(".") + 2]

            os.rename(
                os.path.join(args.dataset, f"scans_{ind + 1}.pcd"),
                os.path.join(args.dataset, f"{timestamp}.pcd")
            )
