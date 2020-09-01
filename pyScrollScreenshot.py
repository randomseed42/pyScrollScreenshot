import os
import cv2
import numpy as np


def pyConcat(img_folder='./img', output_file='full_screenshot.png'):
    img_list = os.listdir(img_folder)
    imgs = [cv2.imread(os.path.join(img_folder, fname)) for fname in img_list]
    cut_imgs = []
    for i in range(len(img_list)-1):
        tail_cuts = []
        top_img = imgs[i]
        bottom_img = imgs[i+1]
        max_cut = max(top_img.shape[0], bottom_img.shape[0])
        for cut in range(1, max_cut):
            if np.sum(top_img[-cut:, :, :] - bottom_img[:cut, :, :]) == 0:
                tail_cuts.append(cut)
        cut_imgs.append(top_img[:-max(tail_cuts), :, :])
        print(f'image {i} cut last {max(tail_cuts)} lines')
    cut_imgs.append(imgs[-1])
    cv2.imwrite(output_file, np.concatenate(full, axis=0))
