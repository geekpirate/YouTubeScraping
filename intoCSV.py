import csv


def processTOCSV(data):
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