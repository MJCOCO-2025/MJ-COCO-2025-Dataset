# MJ-COCO-2025-Dataset

## About Dataset

<p align="justify">
MJ-COCO-2025 is a modified version of the MS-COCO-2017 dataset, in which the annotation errors have been automatically corrected using model-driven methods. The name "MJ" originates from the initials of Min Je Kim, the individual who updated the dataset. "MJ" also stands for "Modification & Justification," emphasizing that the modifications were not manually edited but were systematically validated through machine learning models to increase reliability and quality. Thus, MJ-COCO-2025 reflects both a personal identity and a commitment to improving the dataset through thoughtful modification, ensuring improved accuracy, reliability and consistency. The comparative results of MS-COCO and MJ-COCO datasets are presented in Table 1 and Figure 1. The MJ-COCO-2025 dataset features the improvements, including fixes for group annotations, addition of missing annotations, removal of redundant or overlapping labels, etc. These refinements aim to improve training and evaluation performance in object detection tasks.
</p>


## Summary of Improvements:
<p align="justify">
The re-labeled MJ-COCO-2025 dataset demonstrates substantial improvements in annotation quality, with significant increases in several categories and minor corrections in a few due to previous over-annotations or misclassifications, as shown in Table 1 when compared to the original MS-COCO-2017 dataset.
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
  <img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F26520677%2F6af38e16f7a313e3ad560dc88525f87c%2FPicture14.svg?generation=1745669512762612&alt=media" 
       alt="Comparative results between MS-COCO and MJ-COCO datasets" 
       width="860" height="790"/>
  <p align="center">Figure 1: Visual comparison of MS-COCO-2017 and MJ-COCO-2025 datasets</p>
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
