import collections
# dict = {'kind': 'youtube#commentThread', 'etag': '_vYDJJdXwZvu4nZnjaegaVD2kwM', 'id': 'Ugy7550i3P49fX-fk6N4AaABAg',
#         'snippet': {'videoId': 'Fm8-ImJly1M', 'topLevelComment': {'kind': 'youtube#comment',
#                                                                   'etag': 'Hx0r9Qs7IBwM4yQwrGE7i4r5w7c',
#                                                                   'id': 'Ugy7550i3P49fX-fk6N4AaABAg',
#                                                                   'snippet': {'videoId': 'Fm8-ImJly1M',
#                                                                               'textDisplay': 'Did you have your baby?',
#                                                                               'textOriginal': 'Did you have your baby?',
#                                                                               'authorDisplayName': 'Ovella Oneal',
#                                                                               'authorProfileImageUrl': 'https://yt3.ggpht.com/ytc/AKedOLTmRk0YRQBTmUZgkNPeidh1X6B6prYJ4w2DJpm1uw=s48-c-k-c0x00ffffff-no-rj',
#                                                                               'authorChannelUrl': 'http://www.youtube.com/channel/UCIPnX4hlwqJimyTbfX_K2nQ',
#                                                                               'authorChannelId': {
#                                                                                   'value': 'UCIPnX4hlwqJimyTbfX_K2nQ'},
#                                                                               'canRate': True, 'viewerRating': 'none',
#                                                                               'likeCount': 3,
#                                                                               'publishedAt': '2020-09-13T04:12:33Z',
#                                                                               'updatedAt': '2020-09-13T04:12:33Z'}},
#                     'canReply': True, 'totalReplyCount': 1, 'isPublic': True},
#         'replies': {'comments': [{'kind': 'youtube#comment',
#                                   'etag': 'X3_xAa_bedKlMjjrlBxddsLU9Y4',
#                                   'id': 'Ugy7550i3P49fX-fk6N4AaABAg.9DXXNJU8hYr9IiSqLo2_T3',
#                                   'snippet': {
#                                       'videoId': 'Fm8-ImJly1M',
#                                       'textDisplay': 'Yes Sarah have baby Josiah',
#                                       'textOriginal': 'Yes Sarah have baby Josiah',
#                                       'parentId': 'Ugy7550i3P49fX-fk6N4AaABAg',
#                                       'authorDisplayName': 'Ashley Jackson',
#                                       'authorProfileImageUrl': 'https://yt3.ggpht.com/ytc/AKedOLRbh3DMKauRGHmwjOntir3Ne3Umf6Hwhzr4Q4Z3=s48-c-k-c0x00ffffff-no-rj',
#                                       'authorChannelUrl': 'http://www.youtube.com/channel/UCKzxqjqyNOITXTuap3q_8tA',
#                                       'authorChannelId': {'value': 'UCKzxqjqyNOITXTuap3q_8tA'},
#                                       'canRate': True, 'viewerRating': 'none',
#                                       'likeCount': 0, 'publishedAt': '2021-01-20T02:00:49Z', 'updatedAt': '2021-01-20T02:00:49Z'}}]}}
#
#
# # print(dict['replies']['comments'][0]['snippet']['authorDisplayName'])
#
# arr =[1,3,4,2,4,1,1,3,4,4,2,4,5,3,3,2,2,1,1]
# cnt = collections.Counter(arr)
#
# print(cnt)
#
# for each in cnt:
#     print(each)
#     print(cnt[each])


dict = {'kind': 'youtube#commentThread', 'etag': 'b6itnehbTcgjeb3s-G30jF5S1vE', 'id': 'UgwalJo5c_VJscX9XFh4AaABAg', 'snippet': {'videoId': '7nQxWCn_dBg', 'topLevelComment': {'kind': 'youtube#comment', 'etag': 'm9SAQzS7HO1p6sJdFtUY2qV7wXE', 'id': 'UgwalJo5c_VJscX9XFh4AaABAg', 'snippet': {'videoId': '7nQxWCn_dBg', 'textDisplay': 'Does anyone have the APA citation for this video already~?', 'textOriginal': 'Does anyone have the APA citation for this video already~?', 'authorDisplayName': 'siobhan campion', 'authorProfileImageUrl': 'https://yt3.ggpht.com/ytc/AKedOLQMZUP_VG3kMnHcd81qay8LF1x3qVHnDaDLZWLTVw=s48-c-k-c0x00ffffff-no-rj', 'authorChannelUrl': 'http://www.youtube.com/channel/UCxeJrilgxaIzsAz7bMxxv6g', 'authorChannelId': {'value': 'UCxeJrilgxaIzsAz7bMxxv6g'}, 'canRate': True, 'viewerRating': 'none', 'likeCount': 1, 'publishedAt': '2019-03-20T12:26:28Z', 'updatedAt': '2019-03-20T12:26:28Z'}}, 'canReply': True, 'totalReplyCount': 2, 'isPublic': True}}

if 'replies' in dict:
    print(True)
else:
    print(False)