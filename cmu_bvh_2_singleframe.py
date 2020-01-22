#!/usr/bin/env python 3.7

'''
Convert Carnegie Mellon Mocap file (.bvh format)
To single frames picked out of each file (maintain .bvh format)
**GET EVERY 5TH FRAME**
'''

import os
from os import walk

#path of CMU .bvh files
pathfrom = '/Users/warrentaylor/Desktop/bvh_motionbuilder_cmu_mocap/mocap'
#path for new single frame .bvh files (without deep directory structure)
pathto = '/Users/warrentaylor/Desktop/movement/synthetic-makehuman/bvh-poses/singleframe-bvh'

#create total filelist in no particular order
#0-2548 (2549 .bvh CMU Mocap Files)
file_list = [f for f in os.listdir(pathfrom) if os.path.isfile(os.path.join(pathfrom, f))]
#count for naming output files
file_count = 1
totalcount = 1
#deep directory count
os.mkdir(os.path.join(pathto,'files'))
level1dir = 1
os.mkdir(os.path.join(pathto,'files/', str(level1dir)))
level2dir = 1
os.mkdir(os.path.join(pathto,'files/', str(level1dir) + '/', str(level2dir)))
#loop through all Mocap Files
for i in range(0,len(file_list)):
    #create header file to append to multiple frames
    headerfile  = os.path.join(pathto,'files/','header.bvh')
    open(headerfile, 'a')
    header_linenum = 0
    motion_count = 0
    get_tpose = 0
    with open(os.path.join(pathfrom,file_list[i]), 'r') as input:
        #copy bvh hierarchy, frame_no, and frame_time to header
        #when motion section starts, copy one more line and exit out of header file
    	    #first motion line is needed for 'T-pose'
        with open(headerfile, 'w') as hf: 
            for line in input:
                header_linenum += 1
                if 'Frames:' in line:
                    hf.write('Frames: 2\n')
                elif 'Frame Time:' in line:
                    hf.write('Frame Time: 1\n')
                    get_tpose = 1
                else:
            	    hf.write(line)
                #break after getting t-pose - after 'Frame Time' above
           	    if get_tpose == 1:
           		    break
        #copy every 5th .bvh frame to the header and save file
        for line in input:
            motion_count +=1
            if motion_count % 5 == 0:
                #output file
                outfile = os.path.join(pathto,'files/', str(level1dir) + '/', str(level2dir) + '/', str(file_count) + '.bvh')
                #combine header and motion frame
                with open(outfile, 'a') as outf:
                    with open(headerfile) as hinfile:
                	    #write header to output file
                        outf.write(hinfile.read())
                        #then write motion frame
                        outf.write(line)
                    #step through filecount
                    file_count +=1
                    totalcount +=1
                    #deep directory structure
                    #2nd level reset
                    if file_count % 101 == 0:
                    	if level2dir % 100 == 0:
                    		#second level reset
                    		level1dir +=1
                    		os.mkdir(os.path.join(pathto,'files/',str(level1dir)))
                    		level2dir = 1
                    		os.mkdir(os.path.join(pathto,'files/', str(level1dir) + '/', str(level2dir)))
                    		file_count = 1
                    	else:
                    		#first level reset
                    	    level2dir +=1
                    	    os.mkdir(os.path.join(pathto,'files/', str(level1dir) + '/', str(level2dir)))
                    	    file_count = 1

    #delete header for next file
    os.remove(os.path.join(pathto,'files/','header.bvh'))

print(totalcount)

