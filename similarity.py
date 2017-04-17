# -*- coding:utf-8 -*-
from math import sqrt
"""
    Finding Similar Users
    还需要再加几个别的相似度测量公式

"""


# Euclidean Distance Score
def sim_distance(prefs, person1, person2):
    sim = {}
    for item in prefs[person1]:  # Find items had been rated by both of guys
        if item in prefs[person2]:
            sim[item] = 1
    if len(sim) == 0:
        return 0
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])
    # 返回相似度评分
    return 1/(1+sqrt(sum_of_squares))


# Pearson Correlation Score
def sim_pearson(prefs, person1, person2):
    sim = {}
    for item in prefs[person1]:  # Find items had been rated by both of guys
        if item in prefs[person2]:
            sim[item] = 1
    n = len(sim)
    if n == 0:
        return 0
    sum1 = sum([prefs[person1][it] for it in sim])
    sum2 = sum([prefs[person2][it] for it in sim])
    #  平方和
    sum1Sq = sum([pow(prefs[person1][it], 2) for it in sim])
    sum2Sq = sum([pow(prefs[person2][it], 2) for it in sim])
    #  乘积和 ∑XiYi
    pSum = sum([prefs[person1][it]*prefs[person2][it] for it in sim])
    #  计算皮尔逊评价值
    num = pSum-(sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1, 2)/n)*(sum2Sq-pow(sum2, 2)/n))
    if den == 0:
        return 0
    result = num/den
    # 返回相似度评分
    return result