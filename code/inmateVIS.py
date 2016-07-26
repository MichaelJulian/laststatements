import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import numpy as np
import seaborn as sb

inmates = pd.read_csv("data/Inmate_info.csv")
plt.hist(inmates['Age'])
plt.title("Inmate Age")
plt.show()

inmates['Date'] = pd.to_datetime(inmates['Date'])
inmates['MonthYear'] = inmates['Date'].apply(lambda x:x.date().strftime('%m %Y'))
inmates['Month'] = inmates['Date'].apply(lambda x:x.date().strftime('%m'))
inmates['Day'] = inmates['Date'].apply(lambda x:x.date().strftime('%d'))
inmates['Year'] = inmates['Date'].apply(lambda x:x.date().strftime('%Y'))

plt.hist(list(map(int,inmates['Year'])))
plt.title("Deaths Per Year")
plt.savefig("Deaths Per Year")
plt.show()

plt.hist(list(map(int, inmates['Month'])))
plt.title("Deaths by Month")
plt.savefig("Deaths by Month")
plt.show()

plt.hist(list(map(int, inmates['Day'])))
plt.title("Deaths by Month Date")
plt.savefig("Deaths by Month Date")
plt.show()

labels, values = zip(*Counter(inmates['Race']).items())
indexes = np.arange(len(labels))
plt.bar(indexes, values, 1)
plt.xticks(indexes+1*.5, labels)
plt.title("Deaths by Race")
plt.savefig("Deaths Per Year")
plt.show()
#
# labels, values = zip(*Counter(inmates['County']).most_common(15).items())
# indexes = np.arange(len(labels))
# plt.bar(indexes, values, 1)
# plt.xticks(indexes+1*.5, labels)
# plt.title("Deaths by County")
# plt.savefig("Deaths by County")
# plt.show()

c = Counter(inmates['County'])
most_common_counties = c.most_common(15)
labels = [mcc[0] for mcc in most_common_counties]
values = [mcc[1] for mcc in most_common_counties]
plt.bar(range(len(labels)), values)
plt.xticks(range(len(labels)), labels)
plt.title("Deaths by County")
plt.savefig("Deaths by County")
plt.show()

# violin_data = inmates.ix[:, 6:]
# daterace = violin_data.ix[:, (0,2)]
# sb.violinplot(x = "Race", y = "Age", data = daterace)
# plt.show()
