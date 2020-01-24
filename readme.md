## Create Single Frame .bvh Motion Capture Files

## Reformatting from CMU Mocap Data 
http://mocap.cs.cmu.edu/  
Initial Marker Placement Guide  
http://mocap.cs.cmu.edu/markerPlacementGuide.pdf

## To Run

Download CMU Mocap Data ('bvh_motionbuilder_cmu_mocap')  
https://sites.google.com/a/cgspeed.com/cgspeed/motion-capture/cmu-bvh-conversion  

Clone Repo

run.py
```
python3 run.py /path/to/mocap /path/to/output
```
#### Estimated Output Size 3.3 GB


## To Read Output Pickle
```python
mocap_object_list = []
with open(/path/to/cmu-bvh-frames.pickle", "rb") as f:
    for _ in range(pickle.load(f)):
        mocap_object_list.append(pickle.load(f))
```
Individual Mocap Objects Containing 1 CMU Mocap Video File
```python
mocap_object = mocap_object_list[i]
```
Header of .bvh File (Including T-Pose)
```python
header = mocap_object.header
```
Get Random Frame
```python
import random
frame_no = rand.randint(0,len(mocap_object.frames))
frame = object.frames[frame_no]
```
Create Singleframe .bvh file
```python
outfile = open(/path/to/bvhname.bvh", "w")
outfile.write(object.header + object.frames[i])
outfile.close()
```
