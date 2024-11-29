import random
import time

def getRandomDate(startDate,endDate):
    print("To print a random date between start date and end date")
    randomGenerator = random. random()
    dateFormat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate,dateFormat))
    randomTime = startTime + randomGenerator * (endTime-startTime)
    randomDate = time. strftime(dateFormat,time.localtime(randomTime))
    return randomDate

print("Random date:",getRandomDate("2/1/2024","4/08/2024"))


