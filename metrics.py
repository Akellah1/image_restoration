import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import os
import pandas as pd


names_test = []
names_train = []
#caculate psnr,ssim
def calculate_psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))

def calculate_ssim(img1, img2):
    return ssim(img1, img2, channel_axis=2)

def get_image_list(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

def calculate_metrics(folder1, folder2):
    images1 = get_image_list(folder1)
    images2 = get_image_list(folder2)
    psnr_values = []
    ssim_values = []

    for img1_path, img2_path in zip(images1, images2):
        img1 = cv2.imread(img1_path)
        img2 = cv2.imread(img2_path)
        psnr_values.append(calculate_psnr(img1, img2))
        ssim_values.append(calculate_ssim(img1, img2))
        print(calculate_psnr(img1, img2))
        print(calculate_ssim(img1, img2))
        names_test.append(img1_path)
        names_train.append(img2_path)
        # print(calculate_psnr(img1, img2),calculate_ssim(img1, img2))

    return psnr_values, ssim_values, names_test, names_train

# Calculate metrics
psnr_processed, ssim_processed, test, train = calculate_metrics('ber_model', 'ber_final')

# Calculate average values
avg_psnr_processed = np.mean(psnr_processed)
avg_ssim_processed = np.mean(ssim_processed)

# Save results to a file
results = pd.DataFrame({
    'Image_test' : test,
    'Image_train' : train,
    'PSNR Processed': psnr_processed,
    'SSIM Processed': ssim_processed
})

results.loc['Average'] = [avg_psnr_processed, avg_ssim_processed, '', '']
results.to_csv('metrics_results_final_3.csv')

print('metrics_results_final_3.csv')
