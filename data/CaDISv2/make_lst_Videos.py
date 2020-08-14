import os
top = os.listdir('../list/cadis/.')
print(top)
here = '../list/cadis/'
for i in range(2):
    if i == 0:
        f = open('splits.txt','r')
    else:
        f = open('splits2.txt','r')
    f = f.read()
    loc1 = f.find('#')
    loc2 = f.find('#',loc1+1)
    loc3 = f.find('#',loc2+1)
    splits=['train','val','test']
    for split in splits:
        img_paths = []
        mask_paths = []
        if split == 'train':
            g = f[:loc2-2].split('\n')[1:]
        elif split == 'val':
            g = f[loc2:loc3-3].split('\n')[1:]
        elif split == 'test':
            g = f[loc3:].split('\n')[1:]
        for num in g:
            Each = num
            if num[:3] !='Vid':
                continue
            img_path = os.path.join(Each,'Images')
            lab_path = os.path.join(Each,'Labels')
            if os.path.isfile(img_path):
                continue
            for img in os.listdir(img_path):
                img_paths += os.path.join(img_path, img),
            for lab in os.listdir(lab_path):
                mask_paths += os.path.join(lab_path, lab),
        print(here+split+'.lst')
        # print(img_paths)
        if i ==0:
            with open(here+split+'val.lst','w') as h:
                for j in range(len(img_paths)):
                    h.write(img_paths[j]+' '+mask_paths[j]+'\n')
        else:
            with open(here+split+'_debug.lst','w') as h:
                for j in range(len(img_paths)):
                    h.write(img_paths[j]+' '+mask_paths[j]+'\n')
