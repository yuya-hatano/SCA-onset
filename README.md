# SCA-onset
- This application displays the results of using the random survival forest (RSF) to predict the probability that a non-affected person with the pathological alleles of SCA3 and DRPLA at a given age will remain unaffected in subsequent years. 
- This application is based on data from 292 SCA3 and 203 DRPLA cases. A 100 % asymptomatic probability does not mean that 100 % of the patients will not develop the disease.
- described in detail in:<br>
Yuya Hatano,  Tomohiko Ishihara, Sachiko Hirokawa,  Osamu Onodera. Machine Learning Approach for the Prediction of Age-Specific Probability of SCA3 and DRPLA by Survival Curve Analysis Neurol Genet Jun 2023, 9 (3) e200075; DOI: 10.1212/NXG.0000000000200075 <br> https://ng.neurology.org/content/9/3/e200075
## Install
- If you are a Windows 64 bit user, download all files and run SCAonsetv1.0.exe.
- If not, run SCAonsetv1.0.py in Python 3.11. SCAonsetv1.0.py requires pandas, matplotlib and numpy to be installed.
## Usage
- After running SCAonsetv1.0.exe, select SCA3 or DRPLA for disease. In addition, enter the current age of the unaffected carrier, the number of repeats, and the age at which you want to know the asymptomatic probability.
- A new window will appear. The graph in the center shows the asymptomatic probability (Y-axis) at a certain age (X-axis) for that unaffected carrier. "Asymptomatic probability at age X : Y" at the top shows the asymptomatic probability at the age you want to know, which you entered in the previous Window.　The age at which you want to know the probability can be moved by using the slider below.
## License
- © 2023 Yuya Hatano
- hatanoyuya@gmail.com
## Note
- If you intend to utilize this application for writing papers or presenting at acamedic conferences, please kindly notify us (ishihara@bri.niigata-u.ac.jp).
