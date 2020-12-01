import csv
from datetime import date
from datetime import time
from datetime import datatime

with open('chart1.txt', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    

import matplotlib.pyplot as plt
reader['Close'].plot()
plt.show()
    
