## Code for downloading the 9-class ImageNet dataset for running ImageNet tests of Rebias:https://github.com/clovaai/rebias.git
## It can be used for downloading any subset of Imagenet, by adding it to the wnids list below

## READ ME
# 1. This is the code for downloading the latest imagenet dataset using the imagenet/wordnet API
# 2. It downloads imagenet images tagged with specific wnids. The wnids in the list 'wnids' is taken from the code
# 3. Create an 'imagenet_9class' folder, inside it create two folders called 'train' and 'val'. Make sure you create these folders before you # run this code. Change the base path variable accroding to the location of your 'imagenet_9class' folder. Make sure this code is placed right# outside the 'imagenet_9class' folder
# 4. for running open a terminal and go to the directory where this code is - outside the 'imagenet_9class' folder
# 5. and use python3. you may need to do a pip3 install requests

##This code was written using the following links as references:
# 1. https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
# 2. https://github.com/itf/imagenet-download/blob/master/imagenetDownloader.py

import os
import sys
import requests
import shutil
import numpy as np
from socket import timeout as TimeoutError

base_path = '/home/stud101/atml/rebias/imagenet9class' 

wnids = ['n01641577', 'n01644373', 'n01644900', 'n01664065', 'n01665541',
        'n01667114', 'n01667778', 'n01669191', 'n01819313', 'n01820546',
        'n01833805', 'n01843383', 'n01847000', 'n01978287', 'n01978455',
        'n01980166', 'n01981276', 'n02085620', 'n02099601', 'n02106550',
        'n02106662', 'n02110958', 'n02123045', 'n02123159', 'n02123394',
        'n02123597', 'n02124075', 'n02174001', 'n02177972', 'n02190166',
        'n02206856', 'n02219486', 'n02486410', 'n02487347', 'n02488291',
        'n02488702', 'n02492035', 'n02607072', 'n02640242', 'n02641379',
        'n02643566', 'n02655020']

accepted_formats = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG'] # formats like gif are not accepted
TIMEOUT = 5 # timeout for image URL loading, after which it stops trying and moves on 

def download_images(wnid, path, r): # r is a list of urls
        j = 0
        failed = 0
        for url_img in r:
            #print(url_img)
            if url_img[:4] == 'http':
                try:
                    r2 = requests.get(url_img, stream=True, timeout=TIMEOUT)
                    if r2.status_code == 200:
                        image_format = str(url_img[url_img.rfind('.'):])
                        if image_format in accepted_formats:
                            j += 1
                            image_name = os.path.join(path, wnid+'_'+str(j)+image_format)
                            with open(image_name, 'wb') as f:
                                r2.raw.decode_content = True
                                shutil.copyfileobj(r2.raw, f)
                        else:
                            #print('rejected format : {} | wnid {}'.format(image_format, url_img))
                            failed += 1
                    else:
                        #print('failed to download 1 : {} | wnid : {}'.format(url_img, wnid))
                        failed += 1
                except KeyboardInterrupt:
                    # quit
                    sys.exit()
                except TimeoutError:
                    #print('TimeOut ERROR | ', url_img)
                    failed += 1
                    continue
                except:
                    #print('failed to download 2 : {} | wnid : {}'.format(url_img, wnid))
                    failed += 1
                    continue
        
        return j, failed

for i, wnid in enumerate(wnids):
    url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid='+wnid
    # url = url_list + wnid + url_key


    print('{}/{} | prepairing to download wnid {}...'.format(i, len(wnids), wnid))

    train_path = os.path.join(base_path, 'train', wnid)
    val_path = os.path.join(base_path, 'val', wnid)

    if not os.path.exists(train_path):
        os.mkdir(train_path)
    if not os.path.exists(val_path):
        os.mkdir(val_path)

    response = requests.get(url, stream=True)
    r = response.text.splitlines()[:-1] #last line is empty

    print('wnid {} has {} image links - (some may fail, ~80/20 split)'.format(wnid, len(r)))
    r_val = np.random.choice(np.array(r), size=int(len(r)*0.2), replace=False).tolist()
    r_train = np.array(set(r) - set(r_val)).tolist()

    train_status_j, train_status_failed = download_images(wnid, train_path, r_train)
    val_status_j, val_status_failed = download_images(wnid, val_path, r_val)

    print("wnid: {} ; train data successes-{} ; train data fails-{} ; val data successes-{} ; val data fails {}".
        format(wnid, train_status_j, train_status_failed, val_status_j, val_status_failed))


