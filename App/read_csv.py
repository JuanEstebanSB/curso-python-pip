import csv
#import matplotlib.pyplot as plt

def read_csv(path): 
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        heater = next(reader)
        data =[]
        for row in reader:
            iterable = zip(heater, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
            return data
        
if __name__ == '__main__':
    data = read_csv('data.csv')
    print(data[0])

'''
x = []
y = []

with open('App/data.csv') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))



plt.show()
'''

