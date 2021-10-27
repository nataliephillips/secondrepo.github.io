import json
import pprint
import matplotlib.pyplot as plt
import numpy as np

with open ('week07/SP.POP.TOTL.json', encoding = 'ascii') as f:
    UStext = f.read()
    USdata = json.loads(UStext)
UScensus = USdata[1]
US_date_value = {year['date']: year['value'] for year in UScensus}
pprint.pprint(US_date_value)
USdates = US_date_value.keys()
USdates = (sorted(USdates))
USpop = [US_date_value[key] for key in USdates]
fig, ax = plt.subplots()
ax.scatter(USdates, USpop)
ax.set_xticks(USdates[::4])
ax.set_xticklabels(USdates[::4], rotation=45)
ax.set(title = "Population Starting in 2020\nUnited States",
       xlabel = "Date\n(year)",
       ylabel = "Population\n(people in billions)")
plt.show()

with open ('week07/NY.GDP.MKTP.CD.json', encoding = 'ascii') as f:
    CNtext = f.read()
    CNdata = json.loads(CNtext)
CNcensus = CNdata[1]
CN_date_value = {year['date']: year['value'] for year in CNcensus}
CNdates = CN_date_value.keys()
CNdates = (sorted(CNdates))
CNpop = [CN_date_value[key] for key in CNdates]
fig, ax = plt.subplots()
ax.plot(CNdates, CNpop, c = 'r', label = 'China')
ax.plot(USdates, USpop, c = 'b', label = 'United States')
ax.set_xticks(CNdates[::4])
ax.set_xticklabels(CNdates[::4], rotation=45)
ax.set(title = "Population Starting in 2020\nChina vs United States",
       xlabel = "Date\n(year)",
       ylabel = "Population\n(people in billions)")
plt.legend(loc='upper left')
plt.show()


