# -*- coding: utf-8 -*-
"""
Created on Fri May 16 19:55:14 2025

@author: IAM Lab
"""

import os
import cv2
import pandas as pd
from collections import defaultdict, Counter

start_idx = int(input("Enter start annotation index (e.g., 101): ").strip())
end_idx = int(input("Enter end annotation index (e.g., 200): ").strip())

result_root = './result'
csv_save_root = './result_csv'
os.makedirs(csv_save_root, exist_ok=True)

class_stats = defaultdict(lambda: {
    'Improved': 0,
    'Worse': 0,
    'Ambiguous': 0,
    'Images Examined': 0,
    'Better Image': 0,
    'Worse Image': 0,
    'Mixed Image': 0
})

all_annotation_units = []
for class_name in sorted(os.listdir(result_root)):
    class_path = os.path.join(result_root, class_name)
    if not os.path.isdir(class_path):
        continue
    for image_id in sorted(os.listdir(class_path)):
        image_path = os.path.join(class_path, image_id)
        if not os.path.isdir(image_path):
            continue
        pair_dirs = sorted([
            d for d in os.listdir(image_path)
            if os.path.isdir(os.path.join(image_path, d)) and d.isdigit()
        ], key=lambda x: int(x))
        for pair in pair_dirs:
            all_annotation_units.append((class_name, image_id, int(pair)))

targets = all_annotation_units[start_idx - 1:end_idx]

all_rows = []
annotation_map = defaultdict(lambda: defaultdict(dict))
max_pair_index = 0

print("\nInstructions:")
print("→ 1 = Improved, 2 = Worse, 3 = Ambiguous, q = Quit\n")

for idx, (class_name, image_id, pair_index) in enumerate(targets, start=start_idx):
    pair_path = os.path.join(result_root, class_name, image_id, str(pair_index))
    ms_path = os.path.join(pair_path, 'ms.jpg')
    mj_path = os.path.join(pair_path, 'mj.jpg')

    if not (os.path.exists(ms_path) and os.path.exists(mj_path)):
        continue

    img_ms = cv2.imread(ms_path)
    img_mj = cv2.imread(mj_path)
    if img_ms is None or img_mj is None:
        continue

    combined = cv2.hconcat([img_ms, img_mj])
    window_name = f"{idx}: {class_name} | {image_id} | {pair_index}"
    cv2.imshow(window_name, combined)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(1)

    print(f"\n{idx}: Class={class_name} | Image ID={image_id} | Pair={pair_index}")
    while True:
        choice = input("Enter 1 (Improved), 2 (Worse), 3 (Ambiguous), q (Quit): ").strip()
        if choice in ['1', '2', '3', 'q']:
            break

    cv2.destroyWindow(window_name)

    if choice == 'q':
        print("Exiting.")
        break

    decision = ''
    if choice == '1':
        decision = 'Improved'
        class_stats[class_name]['Improved'] += 1
    elif choice == '2':
        decision = 'Worse'
        class_stats[class_name]['Worse'] += 1
    elif choice == '3':
        decision = 'Ambiguous'
        class_stats[class_name]['Ambiguous'] += 1

    annotation_map[class_name][image_id][pair_index] = decision
    max_pair_index = max(max_pair_index, pair_index)

for class_name in annotation_map:
    for image_id, pairs in annotation_map[class_name].items():
        row = [class_name, image_id]
        counts = {'Improved': 0, 'Worse': 0, 'Ambiguous': 0}
        for i in range(1, max_pair_index + 1):
            decision = pairs.get(i, '')
            if decision == 'Improved':
                row.append(1)
                counts['Improved'] += 1
            elif decision == 'Worse':
                row.append(2)
                counts['Worse'] += 1
            elif decision == 'Ambiguous':
                row.append(3)
                counts['Ambiguous'] += 1
            else:
                row.append('')
        row.extend([counts['Improved'], counts['Worse'], counts['Ambiguous']])
        all_rows.append(row)

if all_rows:
    columns = (
        ['class', 'image_id'] +
        [f'o{i}' for i in range(1, max_pair_index + 1)] +
        ['Sum of Improved', 'Sum of Worse', 'Sum of Ambiguous']
    )
    df = pd.DataFrame(all_rows, columns=columns)
    csv_path = os.path.join(csv_save_root, f"annotation_evaluation_{start_idx}_{end_idx}.csv")
    df.to_csv(csv_path, index=False)
    print(f"\n✅ Evaluation results saved to: {csv_path}")

for class_name in class_stats:
    stats = class_stats[class_name]
    print(f"\n[{class_name}] Summary:")
    print(f" - Improved Annotations: {stats['Improved']}")
    print(f" - Worse Annotations: {stats['Worse']}")
    print(f" - Ambiguous Annotations: {stats['Ambiguous']}")
print("-" * 50)
