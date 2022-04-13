import csv
import collections

# function to write the video data into csv

def processVideoTOCSV(data):
    # data = youtube.youTubeDic

    fields = ['youID', 'title', 'accountName', 'pub_date', 'description', 'link', 'duration', 'TotalComments',
              'Avglength', 'TotalReplies']
    writedata = []

    for i in range(len(data['youID'])):
        writeEachDict = {}
        writeEachDict['youID'] = data['youID'][i]
        writeEachDict['title'] = data['title'][i]
        # when
        writeEachDict['pub_date'] = data['pub_date'][i]
        # who
        writeEachDict['accountName'] = data['accountName'][i]
        # description
        writeEachDict['description'] = data['description'][i]
        # link
        writeEachDict['link'] = data['link'][i]
        # duration
        writeEachDict['duration'] = data['duration'][i]
        # storing all the stats
        writeEachDict['TotalComments'] = data['TotalComments'][i]
        writeEachDict['Avglength'] = data['Avglength'][i]
        writeEachDict['TotalReplies'] = data['TotalReplies'][i]

        writedata.append(writeEachDict)

    with open("AllData/combined_YouTube_Data.csv", 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(writedata)

# function to write the video comments data into csv

def processCommentsTOCSV(data):
    # data = youtube.youTubeDic

    fields = ['youID', 'comments']
    writedata = []

    for i in range(len(data['youID'])):

        writeEachDict = {'youID': data['youID'][i], 'comments': data['comments'][i]}

        writedata.append(writeEachDict)

    with open("AllData/Comments_YouTube_Data.csv", 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(writedata)


# function to write the video replies data into csv

def processRepliesTOCSV(data):
    # data = youtube.youTubeDic

    fields = ['youID', 'replies']
    writedata = []

    for i in range(len(data['youID'])):
        writeEachDict = {'youID': data['youID'][i], 'replies': data['replies'][i]}
        writedata.append(writeEachDict)

    with open("AllData/Replies_YouTube_Data.csv", 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(writedata)


# function to get freq of usernames and write into csv

def processUserCountToCSV(data):
    fields = ['user_name', 'count']
    writedata = []

    userFreq = collections.Counter(data['user_name'])
    for usrnm in userFreq:
        writeEachDict = {'user_name': usrnm, 'count': userFreq[usrnm]}
        writedata.append(writeEachDict)

    with open("AllData/User_YouTube_Data.csv", 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(writedata)