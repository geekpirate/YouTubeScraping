from youtube_tutorial_part1 import getYouTubeData
from intoCSV import processVideoTOCSV, processRepliesTOCSV, processCommentsTOCSV, processUserCountToCSV

searchWords = ["Toddler Physical Development", "Toddler Cognitive Development", "Toddler Emotional Development",
               "Toddler Social and Language Development", "Toddler Sensory and Motor skills Development",
               "child Physical Development", "child Cognitive Development", "child Emotional Development",
               "child Social and Language Development", "child Sensory and Motor skills Development",
               "kid Physical Development", "kid Cognitive Development", "kid Emotional Development",
               "kid Social and Language Development", "kid Sensory and Motor skills Development"]

video_dict = {
    'youID': [],
    'title': [],
    'accountName': [],
    'pub_date': [],
    'description': [],
    'link': [],
    'duration': [],
    'TotalComments': [],
    'Avglength': [],
    'TotalReplies': []
}

comments_dict = {
    'youID': [],
    'comments': []
}

replies_dict = {
    'youID': [],
    'replies': []
}

users_dict = {
    'user_name': []
}

writedata = []

# for word in searchWords:
#     video_dict, comments_dict, replies_dict, users_dict = \
#         getYouTubeData(word, video_dict, comments_dict, replies_dict, users_dict)

# pending = 0
video_dict, comments_dict, replies_dict, users_dict = getYouTubeData(searchWords[2], video_dict, comments_dict,
                                                                     replies_dict, users_dict)

processVideoTOCSV(video_dict)
processCommentsTOCSV(comments_dict)
processRepliesTOCSV(replies_dict)
processUserCountToCSV(users_dict)



