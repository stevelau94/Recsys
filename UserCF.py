# -*- coding:utf-8 -*-
from similarity import sim_distance, sim_pearson
"""
    Ranking the Users
    
"""


# 获取对item评分的K个最相似用户（K默认20）
# def topK_Matches(prefer, person, itemId, k=20, similarity=sim_pearson):
#     userSet = []
#     users = []
#     # 找出所有prefer中评价过Item的用户,存入userSet
#     for user in prefer:
#         if itemId in prefer[user]:
#             userSet.append(user)
#     # 计算相似性
#     scores = [(similarity(prefer, person, other), other) for other in userSet if other != person]
#     scores.sort()
#     scores.reverse()     # 按相似度排序
#
#     if len(scores) <= k:       # 如果小于k，只选择这些做推荐。
#         for item in scores:
#             users.append(item[1])  # 提取每项的userId
#         return users
#     else:                   # 如果>k,截取k个用户
#         kscore = scores[0:k]
#         for item in kscore:
#             users.append(item[1])  # 提取每项的userId
#         return users               # 返回K个最相似用户的ID



# 获取整体相似度最高的的n个最相似用户（n默认5）
def topN_Matches(prefs, person, n=5, similarity=sim_pearson):
    # 计算相似性
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort()
    scores.reverse()  # 按相似度排序
    return scores[0:n]


def getRecommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simSums = {}

    for other in prefs:
        if other == person:
            continue        # 不与自己比较

        sim = similarity(prefs, person, other)

        # 忽略 <= 0 情况
        if sim <= 0:
            continue

        for item in prefs[other]:
            # 只对自己没看过的电影评分
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score相似度 * 分数
                totals.setdefault(item, 0)  # 初始化字典
                totals[item] += prefs[other][item] * sim  # 给字典增加键值对
                # 统计相似度
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # 存为项是（分数，电影）元组格式的列表
    rankings = [(total / simSums[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()  # 排序&反转
    return rankings
