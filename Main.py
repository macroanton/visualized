import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.ticker as FormatStrFormatter

# Data for plotting
f = open('meteordata.json', 'r')

data = json.loads(f.read())

Mass=[]
Year=[]
for d in data:
       if 'mass' in d and 'year' in d:
              if len(d['mass']) >6:
                     Mass.append(d['mass'])
                     Year.append(d['year'])

#Year=[]
#for d in data:
       #if 'year' in d:
              #Year.append({'year':d['year']})
#print('year=', Year)
print('mass=', Mass)
t = sorted(np.array(Year))
s = sorted(np.array(Mass))

fig, ax = plt.subplots()
ax.plot(t, s)


#ax.yaxis.set_major_formatter('{x:<7.1f}')
#ax.xaxis.set_major_formatter('{x:<7.1f}')

ax.set(xlabel='years (s)', ylabel='Tons',
    title='Biggest Meteor in given years')
ax.grid()
#print(dir(ax))
fig.savefig("meteor.jpg")
plt.show()