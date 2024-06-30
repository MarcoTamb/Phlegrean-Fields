from dash import register_page, html, dcc

register_page(__name__, path='/about')

markdown_text_1='''## Campi Flegrei 

Campi Flegrei, also known as Phlegrean Fields, are a large caldera near Naples, Italy.  It is one of the most dangerous volcanoes in the world. This interactive dashboard, built with [Dash](https://dash.plotly.com/), tracks the earthquakes in the Campi Flegrei area.  It gets data from [INGV](https://www.ingv.it/), the Italian research institute monitoring the activity of the Volcano.

#### The volcano

Campi Flegrei, also known as Phlegrean Fields, is a large volcanic area situated near Naples, Italy. This caldera, spanning approximately 13 kilometers, is part of an active volcanic complex formed around 39,000 years ago following a massive eruption. The Phlegrean Fields consist of 24 craters and volcanic edifices, some of which are underwater. The most famous feature within this caldera is the Solfatara crater, which emits jets of steam and sulfurous gases, a visible reminder of the region's volatile nature. The area is characterized by its geothermal activity, hot springs, and fumaroles, making it a significant location for both scientific research and tourism. It is part of the Campanian volcanic arc, which also includes the more famous Mount Vesuvius (resposible of the eruption that destroyed Pompeii in 79 AD), about 9 km (6 miles) east of Naples. The last eruption happened in 1548, which deposited enough material to create a new 132m tall hill, Monte Nuovo. '''



markdown_text_2 = '''It is potentially the most dangerous volcano in Europe due to the size of past eruptions and the number of people who would be affected. 
More than half a million people live in the area of the caldera designated as "Red area", i.e. the area that would be immediately dangerous in the case of an eruption, and that would need to be evacuated beforehand. 
Further 840 thousand people live in the "Yellow area", the area that might be affected by an eruption, who may also be forced to evatuate after the eruption has started. A larger eruption than what than the current evacuation plan anticipates may impact even more people. 

#### Bradyseism

Bradyseism is a geological phenomenon associated with gradual ground uplift or subsidence in volcanic areas, particularly notable in the Phlegrean Fields. This phenomenon is caused by the movement of magma and volcanic gases beneath the Earth's crust, leading to deformation of the ground surface. Bradyseism is categorized into two types: positive bradyseism, where the ground rises, and negative bradyseism, where it subsides. In the Phlegrean Fields, episodes of bradyseism have been recorded since ancient times, with significant events in the 1970s and 1980s causing the ground to rise by several meters. Monitoring bradyseism is crucial for understanding the behavior of the volcano and predicting potential eruptions.

This phenomena can persist for millennia in between eruptions, and each uplift event is normally accompanied by thousands of small to moderate earthquakes.
The word derives from the ancient Greek words βραδύς bradús, meaning "slow", and σεισμός seismós meaning "movement". '''

markdown_text_3 = '''The inflation and deflation of this caldera is especially well documented due to its seaside location and a long history of habitation and construction in the area. The town of Pozzuoli features the Roman Macellum of Pozzuoli in which three marble columns show bands of boreholes left by marine molluscs. These occur up to 7 metres up the columns, showing how bradyseism in the area lowered the land to at least this depth under the sea and subsequently raised it again. Furthermore, a number of archeological ruins can be found underwater near the town of Baia.

This dashboard tracks the earthquakes in the area, scraping data from INGV, the Italian research institute monitoring the activity of the Volcano. 
'''
layout=[
    html.Div(
        dcc.Markdown(markdown_text_1),
        className='about',
    ), 
    html.Img(src='assets/map.png', className='image_centered'),
    html.Div(
        dcc.Markdown(markdown_text_2),
        className='about',
    ), 
    html.Img(src='https://upload.wikimedia.org/wikipedia/commons/5/52/Serapeum_%28Pozzuoli%29_-2.jpg', className='image_centered'),
    html.Div(
        dcc.Markdown(markdown_text_3),
        className='about',
    )
]