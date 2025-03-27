# score1 = [17,18,19,20]
# score2 = [15,17,18,20]
# score3 = [10,15,16,20]
# def getAvg(*args):
#     return sum(args) / len(args)
# print(list(map(getAvg , score1,score2,score3)))
# # [14.0, 16.666666666666668, 17.666666666666668, 20.0]


def getAvg(scoresList):
    global zero_indexes_list,one_indexes_list,two_indexes_list,three_indexes_list,avg_list
    zero_indexes_list = []
    one_indexes_list = []
    two_indexes_list = []
    three_indexes_list = []
    avg_list = []
    
    for score in scoresList:
        zero_indexes_list.append(score[0])
        one_indexes_list.append(score[1])
        two_indexes_list.append(score[2])
        three_indexes_list.append(score[3])

    avg_indexes_zero = sum(zero_indexes_list)/len(zero_indexes_list)
    avg_indexes_one = sum(one_indexes_list)/len(one_indexes_list)
    avg_indexes_two = sum(two_indexes_list)/len(two_indexes_list)
    avg_indexes_three = sum(three_indexes_list)/len(three_indexes_list)

    avg_list.append(avg_indexes_zero)
    avg_list.append(avg_indexes_one)
    avg_list.append(avg_indexes_two)
    avg_list.append(avg_indexes_three)

    return avg_list

print(getAvg([[17,18,19,20],[15,17,18,20],[10,15,16,20]]))




