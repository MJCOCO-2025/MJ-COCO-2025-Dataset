# MJ-COCO-2025-Dataset

# MJ-COCO-2025-Dataset

## About Dataset

<p align="justify">
MJ-COCO-2025 is a modified version of the MS-COCO-2017 dataset, in which the annotation errors have been automatically corrected using model-driven methods. The name "MJ" originates from the initials of Min Je Kim, the individual who updated the dataset. "MJ" also stands for "Modification & Justification," emphasizing that the modifications were not manually edited but were systematically validated through machine learning models to increase reliability and quality. Thus, MJ-COCO-2025 reflects both a personal identity and a commitment to improving the dataset through thoughtful modification, ensuring improved accuracy, reliability and consistency. The comparative results of MS-COCO and MJ-COCO datasets are presented in Table 1 and Figure 1. The MJ-COCO-2025 dataset features the improvements, including fixes for group annotations, addition of missing annotations, removal of redundant or overlapping labels, etc. These refinements aim to improve training and evaluation performance in object detection tasks.
</p>


## Summary of Improvements:
<p align="justify">
The re-labeled MJ-COCO-2025 dataset demonstrates substantial improvements in annotation quality, with significant increases in several categories and minor corrections in a few due to previous over-annotations or misclassifications, as shown in Table 1 when compared to the original MS-COCO-2017 dataset.
</p>

Table 1: Comparison of Class-wise Annotations: MS-COCO-2017 and MJ-COCO-2025.
| Class Names     | MS-COCO | MJ-COCO | Difference | Class Names    | MS-COCO | MJ-COCO | Difference |
|:----------------|:--------|:--------|:-----------|:---------------|:--------|:--------|:-----------|
| Airplane        | 5,135   | 5,810   | 675        | Kite           | 9,076   | 15,092  | 6,016      |
| Apple           | 5,851   | 19,527  | 13,676     | Knife          | 7,770   | 6,697   | -1,073     |
| Backpack        | 8,720   | 10,029  | 1,309      | Laptop         | 4,970   | 5,280   | 310        |
| Banana          | 9,458   | 49,705  | 40,247     | Microwave      | 1,673   | 1,755   | 82         |
| Baseball Bat    | 3,276   | 3,517   | 241        | Motorcycle     | 8,725   | 10,045  | 1,320      |
| Baseball Glove  | 3,747   | 3,440   | -307       | Mouse          | 2,262   | 2,377   | 115        |
| Bear            | 1,294   | 1,311   | 17         | Orange         | 6,399   | 18,416  | 12,017     |
| Bed             | 4,192   | 4,177   | -15        | Oven           | 3,334   | 4,310   | 976        |
| Bench           | 9,838   | 9,784   | -54        | Parking Meter  | 1,285   | 1,355   | 70         |
| Bicycle         | 7,113   | 7,853   | 740        | Person         | 262,465 | 435,252 | 172,787    |
| Bird            | 10,806  | 13,346  | 2,540      | Pizza          | 5,821   | 6,049   | 228        |
| Boat            | 10,759  | 13,386  | 2,627      | Potted Plant   | 8,652   | 11,252  | 2,600      |
| Book            | 24,715  | 35,712  | 10,997     | Refrigerator   | 2,637   | 2,728   | 91         |
| Bottle          | 24,342  | 32,455  | 8,113      | Remote         | 5,703   | 5,428   | -275       |
| Bowl            | 14,358  | 13,591  | -767       | Sandwich       | 4,373   | 3,925   | -448       |
| Broccoli        | 7,308   | 14,275  | 6,967      | Scissors       | 1,481   | 1,558   | 77         |
| Bus             | 6,069   | 7,132   | 1,063      | Sheep          | 9,509   | 12,813  | 3,304      |
| Cake            | 6,353   | 8,968   | 2,615      | Sink           | 5,610   | 5,969   | 359        |
| Car             | 43,867  | 51,662  | 7,795      | Skateboard     | 5,543   | 5,761   | 218        |
| Carrot          | 7,852   | 15,411  | 7,559      | Skis           | 6,646   | 8,945   | 2,299      |
| Cat             | 4,768   | 4,895   | 127        | Snowboard      | 2,685   | 2,565   | -120       |
| Cell Phone      | 6,434   | 6,642   | 208        | Spoon          | 6,165   | 6,156   | -9         |
| Chair           | 38,491  | 56,750  | 18,259     | Sports Ball    | 6,347   | 6,060   | -287       |
| Clock           | 6,334   | 7,618   | 1,284      | Stop Sign      | 1,983   | 2,684   | 701        |
| Couch           | 5,779   | 5,598   | -181       | Suitcase       | 6,192   | 7,447   | 1,255      |
| Cow             | 8,147   | 8,990   | 843        | Surfboard      | 6,126   | 6,175   | 49         |
| Cup             | 20,650  | 22,545  | 1,895      | Teddy Bear     | 4,793   | 6,432   | 1,639      |
| Dining Table    | 15,714  | 16,569  |   -        |    -           |   -     |   -     |   -        |



<div align="left">
  <img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F26520677%2F6af38e16f7a313e3ad560dc88525f87c%2FPicture14.svg?generation=1745669512762612&alt=media" 
       alt="Comparative results between MS-COCO and MJ-COCO datasets" 
       width="860" height="860"/>
  <p align="center">Figure 1: Comparative results between MS-COCO and MJ-COCO datasets</p>
</div>

## Dataset Structure
• The MJ-COCO dataset utilizes images sourced from the original MS-COCO dataset, which can be downloaded from the official MS-COCO website. The images themselves remain unchanged to maintain consistency with the original dataset.<br>
• The re-annotated JSON file, containing updated and refined annotations, can be find [Here](https://drive.google.com/file/d/1RPTBC0_H7PJjfMdBkFyTVo0m0dR7pXRc/view?usp=sharing).<br>
• Annotation Format: JSON (standard COCO annotation format).<br>


## Citation Information
 • If you found this dataset useful, please cite this repository.

## MJ-COCO-2025 Dataset Disclaimer
<p align="justify">
The MJ-COCO-2025 dataset has been re-annotated using a fully automated AI-based labeling process. While significant improvements in annotation quality and performance have been achieved, the automated nature of the process means that residual labeling errors or inaccuracies may still be present. Users are advised to carefully assess the suitability of this dataset for their specific applications and tasks, considering the automated origin of the annotations.
</p>

## Contributors
<p align="justify">The MJ-COCO-2025 dataset was re-annotated by Min Je Kim as part of his research, with support from Hikmat Yar, Altaf Hussain, Muhammad Munsif, and Sung Wook Baik.</p>
