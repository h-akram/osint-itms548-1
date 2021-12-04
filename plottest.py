import matplotlib.pylab as plt
import csv

x = []
y = []
y_num = []
x_filtered = []

# open csv file generated using
with open('reddit_dataset.csv','r') as reddit_csv:
	reddit_data = csv.reader(reddit_csv, delimiter = ',')
	next(reddit_csv)
	
	for row in reddit_data:
		x.append(row[1])
		y.append(row[4])
		
# convert all values in list y from str to int
for i in y:
    j=int(i)
    y_num.append(j)

# convert x and y lists to a dictionary
myDict = {x[i]: y_num[i] for i in range(len(x))}
myList = myDict.items()
myList = sorted(myList)
x, y = zip(*myList)

# creating line graph using dictionary
plt.xlabel('Authors')
plt.ylabel('Number of Comments')
plt.plot(x, y)
plt.show()
