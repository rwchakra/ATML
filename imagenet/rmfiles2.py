# code to remove corrupted files in the imagenet dataset downloaded using 'download_9class_imagenet.py'

import os
import glob
from PIL import Image 

wnids = ['n01641577', 'n01644373', 'n01644900', 'n01664065', 'n01665541',
	'n01667114', 'n01667778', 'n01669191', 'n01819313', 'n01820546',
	'n01833805', 'n01843383', 'n01847000', 'n01978287', 'n01978455',
	'n01980166', 'n01981276', 'n02085620', 'n02099601', 'n02106550',
	'n02106662', 'n02110958', 'n02123045', 'n02123159', 'n02123394',
	'n02123597', 'n02124075', 'n02174001', 'n02177972', 'n02190166',
	'n02206856', 'n02219486', 'n02486410', 'n02487347', 'n02488291',
	'n02488702', 'n02492035', 'n02607072', 'n02640242', 'n02641379',
	'n02643566', 'n02655020']

# change the location according to the dataset train and validation directories.
locs = ["/home/stud101/atml/rebias/imagenet9class/train/", "/home/stud101/atml/rebias/imagenet9class/val/"]

count_arr = []
fail_arr = []
for wnid in wnids:
	for loc in locs:
		os.chdir(loc+wnid)
		count = 0 
		fail = 0
		for file in glob.glob("*"):
			count += 1
			try:
				im = Image.open(file)
				#print('ok')
				im.close()
			except:
				#print('not ok')
				fail += 1
				os.remove(file)
				continue
		count_arr.append(count)
		fail_arr.append(fail)

print(count_arr, len(count_arr))
print(fail_arr, len(fail_arr))
