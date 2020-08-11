from gwpy.timeseries import TimeSeries


data = TimeSeries.read('HLV-HW100916-968654552-1.gwf', 'L1:LDAS-STRAIN')
white = data.whiten(4, 2)

from gwpy.plot import Plot
plot = Plot(data, white, separate=True, sharex=True)
plot.axes[0].set_ylabel('Y-arm power [counts]', fontsize=16)
plot.axes[1].set_ylabel('Whitened amplitude', fontsize=16)
plot.show()


# Bary
from astropy import time, coordinates as coord, units as u
from astropy.coordinates import SkyCoord
from astropy.time import Time

#gal_center = SkyCoord.from_name('Sgr A*')

#L1 = coord.SkyCoord("30:33:46.42", "+90:46:27.27", unit=(u.hourangle, u.deg), frame='icrs')

# GPS 1164556817 = 2016-11-30T16:00:00
times = time.Time(
    [1164556817.123, 1164556818.123],
    format="gps",
    location=coord.EarthLocation.of_site("Greenwich")  # "H1"
    )

"""
The method returns an TimeDelta object, which can be added to your times to give the 
arrival time of the photons at the barycentre or heliocentre.
"""

barycentered_time = times + times.light_travel_time(SkyCoord.from_name('Sgr A*'))  
print(time.Time(times, format="gps"))  # seconds
t = time.Time(times, format="gps")
print(t[0])
print(time.Time(barycentered_time, format="gps"))  # seconds
