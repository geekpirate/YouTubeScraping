import csv
import json
import requests
from convertDurationToSeconds import convert_YouTube_duration_to_seconds
# https://www.googleapis.com/youtube/v3/videos?id=xZyzWjyj1Vc&part=contentDetails&key=AIzaSyBVQTVMsO5b8hTPN8I72y_3NBRsCxcizik"


def getDuration(youTubeID):
    url = "https://www.googleapis.com/youtube/v3/videos?id=" + youTubeID + \
          "&part=contentDetails&key=AIzaSyBVQTVMsO5b8hTPN8I72y_3NBRsCxcizik"
    r = requests.get(url)
    files = r.json()
    try:
        duration = convert_YouTube_duration_to_seconds(files["items"][0]["contentDetails"]["duration"])
    except:
        return 0
    else:
        return duration

#
# durationList = []
#
# with open('Output/youTubeID.txt') as f:
#     # print(getVideo("Fm8-ImJly1M"))
#     lines = f.readlines()
#     for index, each in enumerate(lines):
#         dur = {}
#         each = each.strip()
#         print(index, each)
#         url = "https://www.googleapis.com/youtube/v3/videos?id=" + each + \
#               "&part=contentDetails&key=AIzaSyBVQTVMsO5b8hTPN8I72y_3NBRsCxcizik"
#         r = requests.get(url)
#         files = r.json()
#         try:
#             duration = convert_YouTube_duration_to_seconds(files["items"][0]["contentDetails"]["duration"])
#         except:
#             dur['duration'] = each
#         else:
#             dur['duration'] = duration
#
#         durationList.append(dur)
#
# fields = ['duration']
#
# with open("Output/Duration_Data.csv", 'w') as csvfile:
#     # creating a csv dict writer object
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#
#     # writing headers (field names)
#     writer.writeheader()
#
#     # writing data rows
#     writer.writerows(durationList)