# Phlegraean Fields Earthquakes dashboard

The Phlegrean Fields, also known as Campi Flegrei, is a large volcanic area situated near Naples, Italy. It is also extremely close to where my family lives. This interactive dashboard, built with [Dash](https://dash.plotly.com/), tracks the earthquakes in the area, scraping data from [INGV](https://www.ingv.it/), the Italian research institute monitoring the activity of the Volcano. 

## Instructions 

To run locally, clone the repository, install all the dependencies in *requirements.txt*, set the ENV variable REACT_VERSION=18.2.0 (for dash-mantine-components) and run *main.py*.

If using Mamba/Conda, to set env variables I suggest to create a separate environment and use the following commands, assuming you are in the project folder: (replace mamba with conda if using conda)

    mamba create -n phlegrean
    mamba activate phlegrean 
    mamba install --yes --file requirements.txt
    mamba env config vars set REACT_VERSION=18.2.0
    python main.py
  
You can then access the dashboard on *[localhost:8050](http://localhost:8050)* If somehow you ever want to deploy this to the internet, make sure to follow [these instructions](https://dash.plotly.com/deployment) on the Dash website to avoid potential vulnerabilities. 

## Screenshots

#### 3D map

![3D-view](https://raw.githubusercontent.com/MarcoTamb/Phlegrean-Fields/main/screenshots/3d-view.png)

#### Heatmap

![Heatmap](https://raw.githubusercontent.com/MarcoTamb/Phlegrean-Fields/main/screenshots/heatmap.png)

#### About 

![About](https://raw.githubusercontent.com/MarcoTamb/Phlegrean-Fields/main/screenshots/about.png)

## The volcano

The Phlegrean Fields caldera, spanning approximately 13 kilometers, is part of an active volcanic complex formed around 39,000 years ago following a massive eruption. The Phlegrean Fields consist of 24 craters and volcanic edifices, some of which are underwater. The most famous feature within this caldera is the Solfatara crater, which emits jets of steam and sulfurous gases, a visible reminder of the region's volatile nature. The area is characterized by its geothermal activity, hot springs, and fumaroles, making it a significant location for both scientific research and tourism. It is part of the Campanian volcanic arc, which also includes the more famous Mount Vesuvius (resposible of the eruption that destroyed Pompeii in 79 AD), about 9 km (6 miles) east of Naples. 

The last eruption happened in 1548, which deposited enough material to create a new 132m tall hill, Monte Nuovo. 

It is potentially the most dangerous volcano in Europe due to the size of past eruptions and the number of people who would be affected. 
More than half a million people live in the area of the caldera designated as "Red area", i.e. the area that would be immediately dangerous in the case of an eruption, and that would need to be evacuated beforehand. 
Further 840 thousand people live in the "Yellow area", the area that might be affected by an eruption, who may also be forced to evatuate after the eruption has started. A larger eruption than what than the current evacuation plan anticipates may impact even more people. 

## Bradyseism

Bradyseism is a geological phenomenon associated with gradual ground uplift or subsidence in volcanic areas, particularly notable in the Phlegrean Fields. This phenomenon is caused by the movement of magma and volcanic gases beneath the Earth's crust, leading to deformation of the ground surface. Bradyseism is categorized into two types: positive bradyseism, where the ground rises, and negative bradyseism, where it subsides. In the Phlegrean Fields, episodes of bradyseism have been recorded since ancient times, with significant events in the 1970s and 1980s causing the ground to rise by several meters. Monitoring bradyseism is crucial for understanding the behavior of the volcano and predicting potential eruptions.

This phenomena can persist for millennia in between eruptions, and each uplift event is normally accompanied by thousands of small to moderate earthquakes.
The word derives from the ancient Greek words βραδύς bradús, meaning "slow", and σεισμός seismós meaning "movement". 

The inflation and deflation of this caldera is especially well documented due to its seaside location and a long history of habitation and construction in the area. The town of Pozzuoli features the Roman Macellum of Pozzuoli in which three marble columns show bands of boreholes left by marine Lithophaga molluscs. These occur up to 7 metres up the columns, showing how bradyseism in the area lowered the land to at least this depth under the sea and subsequently raised it again. Furthermore, a number of archeological ruins can be found underwater near the town of Baia.
