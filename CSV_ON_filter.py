import csv
# read csv file
csvFile = open('address.csv')
reader = csv.reader(csvFile)
# create result dictionary
result = {}
for resident in reader:
    if __name__ == '__main__':
        if resident[3]=="Ontario":
            print(resident)
