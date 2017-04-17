# -*- coding:utf-8 -*-
import random


# 获得用户对电影评分数据（总数据）
def loadMovieLens(path='./movielens'):  # 改数据集在这里改目录
    # 从'u.item'中根据id 获取电影标题 返回字典格式{id:title}
    movies = {}
    for line in open(path + '/u.item'):  # 后期改成with打开文件
        (id, title) = line.split('|')[0:2]  # 获取前两项：id title
        movies[id] = title

    # 从'u.data'中获取每个用户对各个电影的评分 返回字典格式{userID:{title: scores}}
    prefs = {}
    for line in open(path + '/u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs


# 默认 将用户数据随机分成8份， 选取1份做测试集， 7做训练集
def generate_dataset(data, pivot=0.875):
    train = {}
    test = {}

    # 遍历总数据，将数据分隔分别放入测试集和训练集
    for key, value in data.iteritems():
        if random.random() < pivot:
            train.update({key: value})
        else:
            test.update({key: value})
    return train, test


if __name__ == "__main__":
    AllDict = loadMovieLens()

    SplitData = generate_dataset(AllDict, pivot=0.875)
    trainSet = SplitData[0]
    testSet = SplitData[1]

    print len(AllDict)
    print len(trainSet)
    print len(testSet)

    print """ 测试通过 """
    print """ 下一版将此处数据存入MongoDB  持久化 """