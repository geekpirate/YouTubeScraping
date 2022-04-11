from extractingComments import getVideo
count = 0
noComments = []
commentsError = []
with open('Output/youTubeID.txt') as f:
    # print(getVideo("Fm8-ImJly1M"))
    lines = f.readlines()
    for each in lines:
        count += 1
        each = each.strip()
        print(count, each)
        # print(len(each), each == "r4QerpKuJsc")
        try:
            commentsAll = getVideo(each)
        except:
            if len(commentsAll) == 0:
                noComments.append(each)
            else:
                commentsError.append(each)
        else:
            # print(commentsAll)
            w = open("./CommentsFile/youtube_" + each + ".txt", "w+")
            w.write(str(commentsAll))

print(noComments)
print(commentsError)
# _3AsA3c8nkM

