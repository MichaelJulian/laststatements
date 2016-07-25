import pandas as pd
from bokeh.sampledata import us_counties
from bokeh.plotting import *
from collections import Counter

us_counties = us_counties.data.copy()
prisoners = pd.read_csv('prisoners.csv')
tx_fips = pd.read_csv('texas_fips.csv', header=None)

fips = tx_fips[1]
tx_counties = [us_counties[(48,i)] for i in fips]

tx_x = [county['lons'] for county in tx_counties]
tx_y = [county['lats'] for county in tx_counties]

county_counts = Counter(prisoners['County'])

p = figure(title="County Rates", toolbar_location="left",
plot_width=1100, plot_height=700)

p.patches(tx_x, tx_y, fill_alpha=0.0,
line_color="#884444", line_width=2)

show(p)
