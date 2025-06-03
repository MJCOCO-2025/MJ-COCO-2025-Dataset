# MJ-COCO-2025-Dataset

## About Dataset

<p align="justify">
MJ-COCO-2025 is a modified version of the MS-COCO-2017 dataset, in which the annotation errors have been automatically corrected using model-driven methods. The name "MJ" originates from the initials of Min Je Kim, the individual who updated the dataset. "MJ" also stands for "Modification & Justification," emphasizing that the modifications were not manually edited but were systematically validated through machine learning models to increase reliability and quality. Thus, MJ-COCO-2025 reflects both a personal identity and a commitment to improving the dataset through thoughtful modification, ensuring improved accuracy, reliability and consistency. The comparative results of MS-COCO and MJ-COCO datasets are presented in Table 1 and Figure 1. The MJ-COCO-2025 dataset features the improvements, including fixes for group annotations, addition of missing annotations, removal of redundant or overlapping labels, etc. These refinements aim to improve training and evaluation performance in object detection tasks.
</p>


## Summary of Improvements:
<p align="justify">
The re-labeled MJ-COCO-2025 dataset exhibits notable improvements in annotation quality compared to the original MS-COCO-2017 dataset. As shown in Table 1, it includes substantial increases in categories such as previously missing annotations and group annotations. At the same time, the dataset has been refined by reducing annotation noise through the removal of duplicates, resolution of challenging or debatable cases, and elimination of non-existent object annotations.
</p>

<div align="center">
Table 1: Comparison of Class-wise Annotations: MS-COCO-2017 and MJ-COCO-2025.
<table style="width:100%; max-width:1200px; table-layout:fixed; border-collapse:collapse;" border="1">
  <thead>
    <tr>
      <th>Class&nbsp;Names</th><th>MS&#8209;COCO</th><th>MJ&#8209;COCO</th><th>Difference</th>
      <th>Class&nbsp;Names</th><th>MS&#8209;COCO</th><th>MJ&#8209;COCO</th><th>Difference</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Airplane</td><td>5,135</td><td>5,810</td><td>675</td><td>Kite</td><td>9,076</td><td>15,092</td><td>6,016</td></tr>
    <tr><td>Apple</td><td>5,851</td><td>19,527</td><td>13,676</td><td>Knife</td><td>7,770</td><td>6,697</td><td>-1,073</td></tr>
    <tr><td>Backpack</td><td>8,720</td><td>10,029</td><td>1,309</td><td>Laptop</td><td>4,970</td><td>5,280</td><td>310</td></tr>
    <tr><td>Banana</td><td>9,458</td><td>49,705</td><td>40,247</td><td>Microwave</td><td>1,673</td><td>1,755</td><td>82</td></tr>
    <tr><td>Baseball Bat</td><td>3,276</td><td>3,517</td><td>241</td><td>Motorcycle</td><td>8,725</td><td>10,045</td><td>1,320</td></tr>
    <tr><td>Baseball Glove</td><td>3,747</td><td>3,440</td><td>-307</td><td>Mouse</td><td>2,262</td><td>2,377</td><td>115</td></tr>
    <tr><td>Bear</td><td>1,294</td><td>1,311</td><td>17</td><td>Orange</td><td>6,399</td><td>18,416</td><td>12,017</td></tr>
    <tr><td>Bed</td><td>4,192</td><td>4,177</td><td>-15</td><td>Oven</td><td>3,334</td><td>4,310</td><td>976</td></tr>
    <tr><td>Bench</td><td>9,838</td><td>9,784</td><td>-54</td><td>Parking Meter</td><td>1,285</td><td>1,355</td><td>70</td></tr>
    <tr><td>Bicycle</td><td>7,113</td><td>7,853</td><td>740</td><td>Person</td><td>262,465</td><td>435,252</td><td>172,787</td></tr>
    <tr><td>Bird</td><td>10,806</td><td>13,346</td><td>2,540</td><td>Pizza</td><td>5,821</td><td>6,049</td><td>228</td></tr>
    <tr><td>Boat</td><td>10,759</td><td>13,386</td><td>2,627</td><td>Potted Plant</td><td>8,652</td><td>11,252</td><td>2,600</td></tr>
    <tr><td>Book</td><td>24,715</td><td>35,712</td><td>10,997</td><td>Refrigerator</td><td>2,637</td><td>2,728</td><td>91</td></tr>
    <tr><td>Bottle</td><td>24,342</td><td>32,455</td><td>8,113</td><td>Remote</td><td>5,703</td><td>5,428</td><td>-275</td></tr>
    <tr><td>Bowl</td><td>14,358</td><td>13,591</td><td>-767</td><td>Sandwich</td><td>4,373</td><td>3,925</td><td>-448</td></tr>
    <tr><td>Broccoli</td><td>7,308</td><td>14,275</td><td>6,967</td><td>Scissors</td><td>1,481</td><td>1,558</td><td>77</td></tr>
    <tr><td>Bus</td><td>6,069</td><td>7,132</td><td>1,063</td><td>Sheep</td><td>9,509</td><td>12,813</td><td>3,304</td></tr>
    <tr><td>Cake</td><td>6,353</td><td>8,968</td><td>2,615</td><td>Sink</td><td>5,610</td><td>5,969</td><td>359</td></tr>
    <tr><td>Car</td><td>43,867</td><td>51,662</td><td>7,795</td><td>Skateboard</td><td>5,543</td><td>5,761</td><td>218</td></tr>
    <tr><td>Carrot</td><td>7,852</td><td>15,411</td><td>7,559</td><td>Skis</td><td>6,646</td><td>8,945</td><td>2,299</td></tr>
    <tr><td>Cat</td><td>4,768</td><td>4,895</td><td>127</td><td>Snowboard</td><td>2,685</td><td>2,565</td><td>-120</td></tr>
    <tr><td>Cell Phone</td><td>6,434</td><td>6,642</td><td>208</td><td>Spoon</td><td>6,165</td><td>6,156</td><td>-9</td></tr>
    <tr><td>Chair</td><td>38,491</td><td>56,750</td><td>18,259</td><td>Sports Ball</td><td>6,347</td><td>6,060</td><td>-287</td></tr>
    <tr><td>Clock</td><td>6,334</td><td>7,618</td><td>1,284</td><td>Stop Sign</td><td>1,983</td><td>2,684</td><td>701</td></tr>
    <tr><td>Couch</td><td>5,779</td><td>5,598</td><td>-181</td><td>Suitcase</td><td>6,192</td><td>7,447</td><td>1,255</td></tr>
    <tr><td>Cow</td><td>8,147</td><td>8,990</td><td>843</td><td>Surfboard</td><td>6,126</td><td>6,175</td><td>49</td></tr>
    <tr><td>Cup</td><td>20,650</td><td>22,545</td><td>1,895</td><td>Teddy Bear</td><td>4,793</td><td>6,432</td><td>1,639</td></tr>
    <tr><td>Dining Table</td><td>15,714</td><td>16,569</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
  </tbody>
</table>

</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/b9a09e79-89ca-4e7f-b2e3-07c542e121e9" 
       alt="Comparative results between MS-COCO and MJ-COCO datasets" 
       width="860" height="350"/>
  <p align="center">**Figure 1:** In MS-COCO dataset, all sheep are annotated with a single label. In MJ-COCO, each sheep is annotated separately for more accurate labeling. </p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/82e9fd65-7f29-4ed3-b1f5-df39611a099f" 
       alt="Comparative results between MS-COCO and MJ-COCO datasets" 
       width="860" height="350"/>
  <p align="center">**Figure 2:** In MS-COCO dataset, some objects like a teddy bear were annotated multiple times, resulting in duplicate annotations. These errors were later corrected in the improved MJ-COCO version, which refined the labels for better accuracy.
</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/4f394cd2-969e-422b-8e5b-f2ccaab6c78a" 
       alt="Comparative results between MS-COCO and MJ-COCO datasets" 
       width="860" height="350"/>
  <p align="center">**Figure 3:** In MS-COCO dataset, there were again challenging and debatable cases where ambiguous objects were annotated as humans. These questionable annotations were later removed by MJ-COCO to improve annotation accuracy.
</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/49f6e5f1-81d1-4cd6-ba78-cd2243b10076" 
       alt="Comparative results between MS-COCO and MJ-COCO datasets" 
       width="860" height="350"/>
  <p align="center">**Figure 4:** In MS-COCO dataset, there were again challenging and debatable cases where ambiguous objects were annotated as humans. These questionable annotations were later removed by MJ-COCO to improve annotation accuracy.
</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/d6797fbc-e5be-4916-aa0a-cad6e4f30465" 
       alt="Comparative results between MS-COCO and MJ-COCO datasets" 
       width="860" height="350"/>
  <p align="center">**Figure 5:** In MS-COCO dataset, some localization errors occurred, such as annotating only the human face instead of person’s body. MJ-COCO later corrected these by re-localizing the annotations to include the complete object.
</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/5c4bdf2c-2aa4-4c3d-9a57-ea8d6eab15b2" 
       alt="Comparative results between MS-COCO and MJ-COCO datasets" 
       width="860" height="350"/>
  <p align="center">**Figure 6:** In MS-COCO dataset, some localization errors occurred, the pizza has been annotated twice with incorrect bounding boxes also. MJ-COCO later corrected these by re-localizing the annotations to include the complete object.
</p>
</div>






## Dataset Structure
• The MJ-COCO dataset utilizes images sourced from the original MS-COCO dataset, which can be downloaded from the official [MS-COCO website](https://cocodataset.org/#home). The images themselves remain unchanged to maintain consistency with the original dataset.<br>
• The re-annotated JSON file, containing updated and refined annotations, can be find [Here](https://drive.google.com/file/d/1RPTBC0_H7PJjfMdBkFyTVo0m0dR7pXRc/view?usp=sharing).<br>
• Annotation Format: JSON (standard COCO annotation format).<br>


## Citation Information
 • If you found this dataset useful, please cite our Paper.

**Pseudo-Labeling Driven Refinement of Benchmark Object Detection Datasets via Analysis of Learning Patterns**, Min Je Kim, Muhammad Munsif, Altaf Hussain, Hikmat Yar, and Sung Wook Baik, 2025, https://arxiv.org/abs/2506.00997.
## MJ-COCO-2025 Dataset Disclaimer
<p align="justify">
The MJ-COCO-2025 dataset has been re-annotated using a fully automated AI-based labeling process. While significant improvements in annotation quality and performance have been achieved, the automated nature of the process means that residual labeling errors or inaccuracies may still be present. Users are advised to carefully assess the suitability of this dataset for their specific applications and tasks, considering the automated origin of the annotations.
</p>

## Contributors
<p align="justify">The MJ-COCO-2025 dataset was re-annotated by Min Je Kim as part of his research, with support from Hikmat Yar, Altaf Hussain, Muhammad Munsif, and Sung Wook Baik.</p>
