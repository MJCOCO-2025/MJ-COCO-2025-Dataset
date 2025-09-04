# -*- coding: utf-8 -*-
"""
Created on Sat May 17 03:10:16 2025

@author: IAM Lab
"""
 


import os
import json
import cv2
import numpy as np
import requests
import zipfile
from collections import defaultdict
from tqdm import tqdm
import time
import gdown

# --- Paths ---

base_dir = './'
image_dir = os.path.join(base_dir, 'train2017')
ms_ann_path = os.path.join(base_dir, 'annotations/instances_train2017.json')
mj_ann_path = os.path.join(base_dir, 'annotations/MJ-COCO.json')
output_root = './result'

# --- Download COCO Dataset and Annotations ---

def download_and_prepare_coco():
    os.makedirs(base_dir, exist_ok=True)

    # Download and extract train2017 images
    if not os.path.exists(image_dir) or not os.listdir(image_dir):
        print("Downloading COCO 2017 Train Images...")
        train_images_url = "http://images.cocodataset.org/zips/train2017.zip"
        train_zip_path = os.path.join(base_dir, "train2017.zip")
        with requests.get(train_images_url, stream=True) as r:
            r.raise_for_status()
            with open(train_zip_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("Extracting train2017.zip...")
        with zipfile.ZipFile(train_zip_path, 'r') as zip_ref:
            zip_ref.extractall(base_dir)
        os.remove(train_zip_path)
        print("Train images ready.")
    else:
        print("Train images already available.")

    # Download and extract annotations
    if not os.path.exists(ms_ann_path):
        print("Downloading COCO 2017 Annotations...")
        annotations_url = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
        annotations_zip_path = os.path.join(base_dir, "annotations_trainval2017.zip")
        with requests.get(annotations_url, stream=True) as r:
            r.raise_for_status()
            with open(annotations_zip_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("Extracting annotations...")
        with zipfile.ZipFile(annotations_zip_path, 'r') as zip_ref:
            zip_ref.extractall(base_dir)
        os.remove(annotations_zip_path)
        print("Annotations ready.")
    else:
        print("COCO annotations already available.")

    # Download MJ-COCO annotation file from Google Drive if missing
    if not os.path.exists(mj_ann_path):
        print("Downloading MJ-COCO annotation from Google Drive...")
        os.makedirs("annotations", exist_ok=True)
        file_id = "1RPTBC0_H7PJjfMdBkFyTVo0m0dR7pXRc"
        url = f"https://drive.google.com/uc?id={file_id}"
        output_path = mj_ann_path
        gdown.download(url, output_path, quiet=False, fuzzy=True)
        print("MJ-COCO download completed.")
    else:
        print("MJ-COCO annotation already available.")

# --- Utility Functions ---

def compute_iou(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2
    xa, ya = max(x1, x2), max(y1, y2)
    xb, yb = min(x1 + w1, x2 + w2), min(y1 + h1, y2 + h2)
    inter = max(0, xb - xa) * max(0, yb - ya)
    union = w1 * h1 + w2 * h2 - inter
    return inter / union if union > 0 else 0

def load_annotations(path):
    with open(path, 'r') as f:
        data = json.load(f)
    images = {img['id']: img for img in data['images']}
    anns = defaultdict(list)
    for ann in data['annotations']:
        anns[ann['image_id']].append(ann)
    categories = {cat['id']: cat['name'] for cat in data['categories']}
    return images, anns, categories

def draw_bbox(img, bbox, color, class_name):
    x, y, w, h = map(int, bbox)
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    cv2.putText(img, class_name, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

def match_by_iou(ms_anns, mj_anns, threshold=0.1):
    matches = []
    used_mj = set()
    for i, a_ms in enumerate(ms_anns):
        best_j, best_iou = -1, 0
        for j, a_mj in enumerate(mj_anns):
            if j in used_mj:
                continue
            iou = compute_iou(a_ms['bbox'], a_mj['bbox'])
            if iou > best_iou:
                best_iou = iou
                best_j = j
        if best_j != -1 and best_iou > threshold:
            matches.append((i, best_j))
            used_mj.add(best_j)
    matched_ms = {i for i, _ in matches}
    matched_mj = {j for _, j in matches}
    only_ms = [i for i in range(len(ms_anns)) if i not in matched_ms]
    only_mj = [j for j in range(len(mj_anns)) if j not in matched_mj]
    return matches, only_ms, only_mj

def only_contains_class(ann_list, target_id):
    return all(a['category_id'] == target_id for a in ann_list)

# --- Main Execution ---

if __name__ == "__main__":
    start_time = time.time()
    print("Starting process...")

    # Download dataset and annotations if missing
    download_and_prepare_coco()

    # Load annotations
    ms_images, ms_anns, ms_cats = load_annotations(ms_ann_path)
    mj_images, mj_anns, mj_cats = load_annotations(mj_ann_path)

    cls2id = {v: k for k, v in ms_cats.items()}
    id2cls = {v: k for k, v in cls2id.items()}
    all_classnames = list(cls2id.keys())
    common_ids = set(ms_anns.keys()) & set(mj_anns.keys())

    for target_class in tqdm(all_classnames, desc="Processing Classes"):
        if target_class in ['banana', 'bird']:
            continue

        target_id = cls2id[target_class]
        for img_id in common_ids:
            anns_ms = ms_anns[img_id]
            anns_mj = mj_anns[img_id]

            if not only_contains_class(anns_ms, target_id):
                continue
            if not only_contains_class(anns_mj, target_id):
                continue

            file_name = ms_images[img_id]['file_name']
            image_path = os.path.join(image_dir, file_name)
            if not os.path.exists(image_path):
                continue

            img = cv2.imread(image_path)
            ann_ms = [a for a in anns_ms if a['category_id'] == target_id]
            ann_mj = [a for a in anns_mj if a['category_id'] == target_id]

            if len(ann_ms) == 0 and len(ann_mj) == 0:
                continue
            if {(a['category_id'], tuple(a['bbox'])) for a in ann_ms} == {(a['category_id'], tuple(a['bbox'])) for a in ann_mj}:
                continue

            save_dir = os.path.join(output_root, target_class, str(img_id))
            os.makedirs(save_dir, exist_ok=True)

            matches, only_ms, only_mj = match_by_iou(ann_ms, ann_mj)
            cnt = 1

            for i, j in matches:
                pair_dir = os.path.join(save_dir, f"{cnt}")
                os.makedirs(pair_dir, exist_ok=True)
                img_ms = img.copy()
                img_mj = img.copy()
                draw_bbox(img_ms, ann_ms[i]['bbox'], (0, 0, 255), target_class)
                draw_bbox(img_mj, ann_mj[j]['bbox'], (0, 255, 0), target_class)
                cv2.imwrite(os.path.join(pair_dir, "ms.jpg"), img_ms)
                cv2.imwrite(os.path.join(pair_dir, "mj.jpg"), img_mj)
                cnt += 1

            for i in only_ms:
                only_dir = os.path.join(save_dir, f"{cnt}")
                os.makedirs(only_dir, exist_ok=True)
                img_box = img.copy()
                draw_bbox(img_box, ann_ms[i]['bbox'], (0, 0, 255), target_class)
                cv2.imwrite(os.path.join(only_dir, "ms.jpg"), img_box)
                cv2.imwrite(os.path.join(only_dir, "mj.jpg"), img)
                cnt += 1

            for j in only_mj:
                only_dir = os.path.join(save_dir, f"{cnt}")
                os.makedirs(only_dir, exist_ok=True)
                img_box = img.copy()
                draw_bbox(img_box, ann_mj[j]['bbox'], (0, 255, 0), target_class)
                cv2.imwrite(os.path.join(only_dir, "mj.jpg"), img_box)
                cv2.imwrite(os.path.join(only_dir, "ms.jpg"), img)
                cnt += 1

    print("Elapsed Time: ", time.time() - start_time)
