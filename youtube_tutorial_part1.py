import csv
import sys
sys.path.append('/Users/abhinavreddy/PycharmProjects/youtubeScraping')
from youtube_videos import youtube_search, video_comments
from extractTimeDuration import getDuration
from extractingComments import getVideo


def grab_videos(keyword, video_dict, comments_dict, replies_dict, users_dict, token=None):
    print("log: starting grab_videos")
    writeEachDict = {}
    res = youtube_search(keyword, token=token)
    token = res[0]
    videos = res[1]
    # print(token)
    for vid in videos:
        # for csv
        # print(vid)
        # break
        # writeEachDict['youID'] = (vid['id']['videoId'])
        # writeEachDict['title'] = (vid['snippet']['title'])
        # # when
        # writeEachDict['pub_date'] = (vid['snippet']['publishedAt'])
        # # who
        # writeEachDict['accountName'] = (vid['snippet']['channelTitle'])
        # # description
        # writeEachDict['description'] = (vid['snippet']['description'])
        # # link
        # writeEachDict['link'] = ("https://www.youtube.com/watch?v="  + vid['id']['videoId'])
        # writedata.append(writeEachDict)

        # code for saving all the video details into csv

        youTubeID = vid['id']['videoId']

        video_dict['youID'].append(youTubeID)
        video_dict['title'].append(vid['snippet']['title'])
        # when
        video_dict['pub_date'].append(vid['snippet']['publishedAt'])
        # who
        video_dict['accountName'].append(vid['snippet']['channelTitle'])
        # description
        video_dict['description'].append(vid['snippet']['description'])
        # link
        video_dict['link'].append("https://www.youtube.com/watch?v=" + vid['id']['videoId'])
        # duration
        video_dict['duration'].append(getDuration(youTubeID))
        # get all stats
        comments_dict, TotalComments, count_Replies, length_of_comments, replies_dict, users_dict = \
            getVideo(youTubeID, comments_dict, replies_dict, users_dict)
        video_dict['TotalComments'].append(TotalComments)
        video_dict['Avglength'].append(length_of_comments)
        video_dict['TotalReplies'].append(count_Replies)

    print("log: ending grab_videos")
    # print("added " + str(len(videos)) + " videos to a total of " + str(len(video_dict['youID'])))
    return token, video_dict, comments_dict, replies_dict, users_dict


# (toddler | kid) (Physical | Cognitive | Emotional | Social and Language | Sensory and Motor skills) (Development)
# search_word = "child Physical Development"

def getYouTubeData(search_word, video_dict, comments_dict, replies_dict, users_dict):
    print("log: starting getYouTubeData")
    token, video_dict, comments_dict, replies_dict, users_dict = \
        grab_videos(search_word, video_dict, comments_dict, replies_dict, users_dict, token=None)
    while token != "last_page":
        # print(token)
        token, video_dict, comments_dict, replies_dict, users_dict = \
            grab_videos(search_word, video_dict, comments_dict, replies_dict, users_dict, token=token)
    print("log: ending getYouTubeData")
    return video_dict, comments_dict, replies_dict, users_dict

# processTOCSV(video_dict)

# print(video_dict)

