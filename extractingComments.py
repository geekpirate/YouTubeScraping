from googleapiclient.discovery import build

DEVELOPER_KEY = "AIzaSyBVQTVMsO5b8hTPN8I72y_3NBRsCxcizik"
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"
commentsAll = []
# repliesAll = []


def video_comments(video_id, count_Comments, count_Replies, length_of_Comments, token=None):
    # empty list for storing reply
    replies = []

    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=DEVELOPER_KEY)

    # retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id,
        pageToken=token
    ).execute()
    if 'nextPageToken' in video_response:
        token = video_response['nextPageToken']
    else:
        token = None
    # iterate video response
    while video_response:
        # extracting required info
        # from each result object
        for item in video_response['items']:
            count_Comments += 1
            # print(count_Comments, item['snippet']['topLevelComment']['snippet']['textDisplay'])
            print(item)
            # break
            commentDict = {}
            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            length_of_Comments += len(comment)

            commentDict["comment"] = item['snippet']['topLevelComment']['snippet']['textDisplay']
            commentDict["likeCount"] = item['snippet']['topLevelComment']['snippet']['likeCount']
            commentDict["publishedAt"] = item['snippet']['topLevelComment']['snippet']["publishedAt"]

            # counting number of replies for each comment

            replycount = item['snippet']['totalReplyCount']
            count_Replies += replycount
            # if reply is there
            if replycount > 0:
                repliesDict = {}
                # iterate through all reply
                for reply in item['replies']['comments']:
                    # Extract reply
                    repliesDict["replies"] = reply['snippet']['textDisplay']
                    repliesDict["likeCount"] = reply['snippet']['likeCount']
                    repliesDict["publishedAt"] = reply['snippet']['publishedAt']

                    # Store reply is list
                    replies.append(repliesDict)
                    # repliesAll.append(reply)

                commentDict["replies"] = replies

            commentsAll.append(commentDict)
            replies = []

        return token, count_Comments, count_Replies, length_of_Comments


videoID = "Fm8-ImJly1M"

# method to pass every video and get comments and replies to each comments
def getVideo(videoID):
    count_Comments = 0
    count_Replies = 0
    length_of_Comments = 0
    length_of_Replies = 0

    token, count_Comments, count_Replies, length_of_Comments = \
        video_comments(videoID, count_Comments, count_Replies, length_of_Comments)

    while token != "last_page" and token is not None:
        # count_Comments += 1
        if token is not None:
            token, count_Comments, count_Replies, length_of_Comments = \
                video_comments(videoID, count_Comments, count_Replies, length_of_Comments, token=token)
    # print(count_Comments, count_Replies, round(length_of_Comments/count_Comments, 2))
    return commentsAll, count_Comments, count_Replies, round(length_of_Comments/count_Comments, 2)

# videoID = "_-P0WA2sCZM"
result = getVideo(videoID)


# print(result)

