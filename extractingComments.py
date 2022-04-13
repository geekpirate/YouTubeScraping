from googleapiclient.discovery import build

DEVELOPER_KEY = "AIzaSyCdeloVdg_LCBau0DbT9WrgRUVzkjVj9DI"
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"
commentsAll = []


# repliesAll = []


def video_comments(video_id, count_Comments, count_Replies, length_of_Comments, comments_dict, replies_dict, users_dict,
                   token=None):
    print("log: starting video_comments")
    # empty list for storing reply
    replies = []

    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=DEVELOPER_KEY)

    # retrieve youtube video results
    try:
        print("try getting:", video_id)
        video_response = youtube.commentThreads().list(
            part='snippet,replies',
            videoId=video_id,
            pageToken=token
        ).execute()
    except:
        print("except getting:", video_id)
        return None, count_Comments, count_Replies, length_of_Comments, comments_dict, replies_dict, users_dict
    print("else getting:", video_id)
    if 'nextPageToken' in video_response:
        token = video_response['nextPageToken']
    else:
        token = None
        print("log: no data in video_comments")
    # iterate video response
    while video_response:
        # extracting required info
        # from each result object
        for item in video_response['items']:
            count_Comments += 1

            # break
            commentDict = {}
            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            # print(comment)
            length_of_Comments += len(comment)
            comments_dict['youID'].append(video_id)
            comments_dict['comments'].append(comment)

            commentDict["comment"] = item['snippet']['topLevelComment']['snippet']['textDisplay']
            commentDict["likeCount"] = item['snippet']['topLevelComment']['snippet']['likeCount']
            commentDict["publishedAt"] = item['snippet']['topLevelComment']['snippet']["publishedAt"]

            # counting number of replies for each comment

            replycount = item['snippet']['totalReplyCount']
            count_Replies += replycount

            # to extract user name who has commented

            users_dict["user_name"].append(item['snippet']['topLevelComment']['snippet']['authorDisplayName'])

            # if reply is there

            if replycount > 0:
                repliesDict = {}
                # iterate through all reply
                print(replycount, video_id, item)
                if "replies" in item:
                    for reply in item['replies']['comments']:
                        print(item)
                        # Extract reply
                        repliesDict["replies"] = reply['snippet']['textDisplay']
                        repliesDict["likeCount"] = reply['snippet']['likeCount']
                        repliesDict["publishedAt"] = reply['snippet']['publishedAt']

                        replies_dict['youID'].append(video_id)
                        replies_dict['replies'].append(reply['snippet']['textDisplay'])

                        users_dict["user_name"].append(reply['snippet']['authorDisplayName'])
                        # Store reply is list
                        replies.append(repliesDict)
                        # repliesAll.append(reply)
                else:
                    count_Replies -= replycount


                # commentDict["replies"] = reply['snippet']['authorDisplayName']

            commentsAll.append(commentDict)
            replies = []
        print("log: ending video_comments")
        return token, count_Comments, count_Replies, length_of_Comments, comments_dict, replies_dict, users_dict


# videoID = "Fm8-ImJly1M"

# method to pass every video and get comments and replies to each comments

def getVideo(videoID, comments_dict, replies_dict, users_dict):
    print("log: starting getVideo")
    count_Comments = 0
    count_Replies = 0
    length_of_Comments = 0
    length_of_Replies = 0

    token, count_Comments, count_Replies, length_of_Comments, comments_dict, replies_dict, users_dict = \
        video_comments(videoID, count_Comments, count_Replies, length_of_Comments, comments_dict, replies_dict,
                       users_dict)

    while token != "last_page" and token is not None:
        # count_Comments += 1
        if token is not None:
            token, count_Comments, count_Replies, length_of_Comments, comments_dict, replies_dict, users_dict = \
                video_comments(videoID, count_Comments, count_Replies, length_of_Comments, comments_dict,
                               replies_dict, users_dict, token=token)
    # print(count_Comments, count_Replies, round(length_of_Comments/count_Comments, 2))
    avg_length = length_of_Comments
    if count_Comments > 0:
        avg_length = round(length_of_Comments / count_Comments, 2)
    print("log: ending getVideo")
    return comments_dict, count_Comments, count_Replies, avg_length, replies_dict, users_dict

# videoID = "_-P0WA2sCZM"
# result = getVideo(videoID)

# print(result)
