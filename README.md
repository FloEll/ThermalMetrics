# ThermalMetrics
This QGIS3 plugin helps to calculate basic metrics and indices (Shannon and Simpson Diversity Index) from thermal images. 
I created a small tutorial for this plugin: https://ecothermographylab.com/thermal-metrics/

# ThermalMetrics plugin for QGIS3
This plugin helps to calculate several metrics and indices such as the Shannon Diversity Index and the Simpson Diversity Index from thermal images. It is especially useful for land, landscape and canopy surface temperature maps and images. However, it is still an experimental plugin and especially the patch detection functions still take quite long to calculate. It is a good idea to just grab a coffee (or any other hot beverage) and just wait until it is done calculating. It might sometimes look like QGIS crashed while it is calculating the patches, just wait, it will be fine. In a worst case it took ~7 min so far, depending on your raster size, it should take around 1-2 minutes usually.

If you have any problems using the plugin, if you found a bug or if you just want to say "Hi!", please contact me via info@ecothermographylab.com

# Index:
1. How to run ThermalMetrics
2. How to cite the use of ThermalMetrics
3. More information

# 1. How to run ThermalMetrics:
I created a small tutorial for this plugin: https://ecothermographylab.com/thermal-metrics/

To run the plugin please open the tab ThermalMetrics in the plugin user interface

## 1.1 Minimum requirements:
### 1.1.1 Select an input raster:
Your input raster should be a one-band .tif file with a single temperature value per pixel in Kelvin or degree Celsius. If the values are in degree Celsius they are automatically converted to Kelvin and vice versa. Please try to use a .tif file that has been georeferenced before. Without a georeferenciation, the area calculated in m² or km² will not be realistic.

Example data is provided for download from this source:
https://github.com/FloEll/QWaterModel/tree/master/Data_Examples

### 1.1.2 Select an output file:
Define a location where to store the output .csv file. This file contains model input and output data as averages, minimal and maximal values. 

### 1.1.3 Manually input NaN values: 
Define the NaN (empty) values of the input raster manually. This is usually not necessary because I suppose your NaN values are sth. like None or 0. If this is the case, just leave the NaN value window as it is, the NaN values will be recognized.  However, if your file contains the NaN values not as None, np.nan or 0 but as e.g. -273.15 or -9999.99 or anything else, please specify this in the window. You can't however define your NaN values as a string or text.  

## 1.2 The simple metrics section
Actually you could give your data a test run now already. Just click on OK below, if your data will work with this plugin, you will already get a .csv files with the first metrics as an output.

The simple metrics section is activated by default. However, you can of course untick it. All these values will be saved in your output file.

The options you can choose from here are: 
- image and map metrics:
    - total number of pixels in the image/map
    - total number of non-NaN pixels
    - % of non_NaN pixels
    - X and Y shape of image
- geographic metrics:
    -  Area covered by whole image (m²)
    - Area covered by non-NaN pixels (m²)
    - Area covered by whole image (km²)
    - Area covered by non-NaN pixels (km²)
- statistical standard metrics:
    - Min, max and mean temperature (in K and °C)
    - Standard deviation of temperature
    - Variance of temperature

## 1.3 The histogram and distribution metrics section
This section is also activated by default, but you can also untick and deactivate it. In this section a histogram from all your non-NaN data is created. By default the historgam bins are created automatically. However if you decide you just want e.g. 5 bins, you can fill the small bin definition window with a 5. Typing "auto" in it again will result in an automatic bin selection again. 
This section calculates and saves the following values to the .csv:
- Histogram 
- Histogram number of pixels in bins
- Skewness
- Kurtosis
- Fisher-Pearson Coefficient of Skewness (FPCS)

## 1.4 The patch richness and distribution section
This section is deactivated by default. Please click the check box to run it. 
This section will produce output for the .csv statistics file you specified above. It will also generate a second .csv file with the patch parameters (in the style of a pandas dataframe -> you can easily import that in pandas again) for each individual patch. It will also create a raster with the patch classes and load this into QGIS automatically.

After clicking the checkbox, the output raster path window is automatically filled. This feature was just implemented for convenience and the raster file is saved in the same location as the .csv file. Optionally you can also select another location using the menu next to it. 
Next, you can define the number of patch classes. This is by default set to auto, just type in any full number. This doesn't define the number of patches, but how they are selected by their values. If you type in a 5, then there will be 5 patch classes (but usually many more patches per class). 
The patch construction parameters are how the individual patches are constructed. They are by default all set to 3, because that resulted to be a good compromise for my test rasters. Generally pick higher numbers (try 8 or 20) if your patches are supposed to be bigger (e.g. if you want a wheat field to be one entire patch and the road and hedge next to it to also be single patches for themselves). If you are interested in selecting the single plants in your wheat field, then you should pick a lower value. 1 is the minimum though. 

You can also choose 3 different values, e.g. dilation = 4, closing = 3, erosion = 15 if that works better for you. I plan to also provide an automated selection feature here in the future. Therefore it would be great if you could communicate me your experiences via: info@ecothermographylab.com

## 1.5 The Indices section
This section is for calculating indices based on the patches above. You'll therefore have to run the patch section to be able to run the indices. 
The Indices are deactivated by default. 
- Shannon Diversity Index:
This is a pretty common index in ecology, my implementation of this index and the similar indices below are based on these two sources:
-> http://www.tiem.utk.edu/~gross/bioed/bealsmodules/shannonDI.html
-> https://www.statology.org/shannon-diversity-index/
- Shannon Equitability Index
- Simpson Diversity Index:
This is a pretty common index in ecology, my implementation of this index and the similar indices below are based on these two sources:
-> http://www.tiem.utk.edu/~gross/bioed/bealsmodules/simpsonDI.html
-> https://www.omnicalculator.com/statistics/simpsons-diversity-index#what-is-simpson's-index
- Gini-Simpson Diversity Index
- Simpson Reciprocal Index

# 2. How to cite the ThermalMetrics plugin
If you are using this plugin for a scientific publication please don't forget to cite it:
Ellsäßer, F. (2021) QGIS3 ThermalMetrics Plugin version 0.1 URL: https://plugins.qgis.org/plugins/thermalmetrics/

If you have any suggestions of how to make this plugin better, or did you find a bug? Then just contact me via: info@ecothermographylab.com


Happy patch diversity modelling :) 

# 3. More Information
This plugin is the last plugin that I wanted to create for a small toolbox to be used with thermal images/maps in ecology research. So far it is mostly used for educational purposes. 

You might also try:
QWaterModel for water and energy balance modelling and evapotranspiration assessment 
-> https://plugins.qgis.org/plugins/qwatermodel/
CWSI to calculate the crop water stress index
-> https://plugins.qgis.org/plugins/cwsi/
The Ecoystem Respiration Tool  to calculate ecosystem and plant respiration
-> https://plugins.qgis.org/plugins/ecores/

I'll create some nice tutorials for all of these soon. 

QGIS3 Python Plugins repository: https://plugins.qgis.org/plugins/thermalmetrics/
Code repository: https://github.com/FloEll/ThermalMetrics
Bug Tracker: https://github.com/FloEll/ThermalMetrics/issues
