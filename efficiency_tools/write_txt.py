import os
## singel
img_folder = ''
root_name = ''
list_folder = ''
os.makedirs(list_folder, exist_ok=True)
img_list = os.listdir(img_folder)
test_num = int(0.2*len(img_list))
train_list = img_list[0:-test_num]
test_list = img_list[-test_num:]


with open(list_folder+'train.txt', 'w') as f:
    for l1 in train_list:
        if l1.split('.')[-1] != 'png':
            continue
        f.write('%s%s '%(root_name,l1))
with open(list_folder+'test.txt', 'w') as f:
    for l1 in test_list:
        if l1.split('.')[-1] != 'png':
            continue
        f.write('%s%s '%(root_name,l1))


