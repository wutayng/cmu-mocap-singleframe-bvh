#!Python 3.6
"""
Convert Carnegie Mellon Mocap file (.bvh format)
To Single frames picked out of each file (maintain .bvh format)
"""

import argparse
import os
import pickle
import linecache
import time

start_time = time.time()

parser = argparse.ArgumentParser(description="Conversion Parameters Input")
parser.add_argument("mocap_dir", help="Path To the CMU Mocap Files")
parser.add_argument("output_dir", help="Output Path")
args = parser.parse_args()

# Create total bvh video file list
file_list = [
    f
    for f in os.listdir(args.mocap_dir)
    if os.path.isfile(os.path.join(args.mocap_dir, f))
]

# Mocap File Class
class mocap:
    def __init__(self, name, header):
        self.name = name
        self.header = header
        self.frames = []


# Initialize Output Pickle
outfile = open(args.output_dir + "/cmu-bvh-frames.pickle", "wb")
# Pickle the Number of Mocap Files (Number of Objects in Output)
pickle.dump(len(file_list), outfile)

# Get Target Mocap File From Data
file_no = 0
for mocap_file in file_list:
    # Header of .bvh Mocap File
    headerstr = ""
    line_num_tracker = 0
    with open(os.path.join(args.mocap_dir, mocap_file), "r") as f:
        for line in f:
            if "Frames:" in line:
                break
            else:
                headerstr = headerstr + line
            line_num_tracker += 1
        # Write Final Two Lines of Header For Single Frame w/ T-Pose
        headerstr = headerstr + "Frames: 2\n" + "Frame Time: 1\n"
        # Write T-Pose Line to Header
        headerstr = headerstr + linecache.getline(
            os.path.join(args.mocap_dir, mocap_file), line_num_tracker + 3
        )

    # Create Object for that Mocap File
    mocap_output = mocap(os.path.basename(mocap_file)[:-4], headerstr)

    # Write All Frames to Object
    frame_no = line_num_tracker + 4
    while linecache.getline(os.path.join(args.mocap_dir, mocap_file), frame_no) != "":
        mocap_output.frames.append(
            linecache.getline(os.path.join(args.mocap_dir, mocap_file), frame_no)
        )
        frame_no += 1

    # Write Object to Pickle
    pickle.dump(mocap_output, outfile)

    # Output Stats
    print(
        "Video .bvh Files Complete: {} of {} --- Time Elapsed {} Seconds".format(
            file_no, len(file_list), round(time.time() - start_time, 2)
        )
    )
    file_no += 1

# Close Pickle Output
outfile.close()
