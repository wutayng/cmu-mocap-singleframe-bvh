# Create Single Frame .bvh Motion Capture Files

# Reformatting from CMU Mocap Data http://mocap.cs.cmu.edu/ - Initial Marker Placement Guide http://mocap.cs.cmu.edu/markerPlacementGuide.pdf

# Every 5th frame in each video .bvh file reformatted into individual file, starting w/5

## Each output .bvh file has two frames: 1 = t-pose, 2 = chosen frame

# Steps

1. Download CMU Mocap Data ('bvh_motionbuilder_cmu_mocap') - from https://sites.google.com/a/cgspeed.com/cgspeed/motion-capture/cmu-bvh-conversion
2. Edit cmu_bvh_2_singleframe.py 'pathfrom' (mocap folder dir) and 'pathto' (output files dir)
3. Run cmu_bvh_2_singleframe.py

# Files Created

## Total File Count: 851,350

## 4.49 GB

## Directory Structure

Top Level: singleframe-bvh
Level 1: max100 Directories
Level 2: max100 Directories
Level 3: max100 .bvh Files
