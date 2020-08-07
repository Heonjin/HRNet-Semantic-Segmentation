import os
top = os.listdir('../list/cadis/.')
print(top)
here = '../list/cadis/'
f = open('splits.txt','r')
f = f.read()
loc1 = f.find('#')
loc2 = f.find('#',loc1+1)
loc3 = f.find('#',loc2+1)
split='test'#############################################
# folder = '.'
debug = False
img_paths = []
mask_paths = []
if split == 'train':
    f = f[:loc2-2].split('\n')[1:]
elif split == 'val':
    f = f[loc2:loc3-3].split('\n')[1:]
elif split == 'test':
    f = f[loc3:].split('\n')[1:]
for num in f:
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
with open(here+split+'.lst','w') as f:
    for j in range(len(img_paths)):
        f.write(img_paths[j]+' '+mask_paths[j]+'\n')