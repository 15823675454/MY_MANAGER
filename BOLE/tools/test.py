

def test(list1):
    list2 = []
    for i in list1:
        if i['parent_id'] == 0:
            list2.append({'id': i['id'], 'chidren': []})
        elif i['parent_id'] != 0:
            for j in list2:
                if j['id'] == i['parent_id']:
                    j['chidren'].append({'id': i['id']})
    return list2
# [
# {id:1,chidren:[{id:2},...]},
# {id:2,chidren:[{id:4},...]}
# ]
def selectionSort(nums):
    for i in range(0, len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j]['score'] > nums[min]['score']:
                min = j
        nums[i], nums[min] = nums[min], nums[i]

if __name__ == '__main__':
    # list1 = [
    #     {'id': 1, 'score': 23},
    #     {'id': 2, 'score': 56},
    #     {'id': 3, 'score': 78},
    #     {'id': 4, 'score': 56},
    #     {'id': 5, 'score': 12},
    #     {'id': 6, 'score': 3},
    #     {'id': 7, 'score': 77}
    #         ]
    # # a = test(list1)
    # # print(a)
    # selectionSort(list1)
    # print(list1)

    res = {"code": 200, "data": [{"name": "20190100", "art": [{"score": "88.00", "img": "picture/u31915972823907253254fm26gp0.jpg"}, {"score": "66.00", "img": "picture/\u77ed\u53d1\u7f8e\u5973\u6843\u82b1\u56ed\u552f\u7f8e\u5199\u771f\u6e05\u65b0\u53ef\u4eba.jpg"}, {"score": "55.00", "img": "picture/\u767d\u7699\u5c11\u5973\u590f\u65e5\u552f\u7f8e\u5199\u771f\u6e05\u7eaf\u52a8\u4eba.jpg"}]}, {"name": "20190101", "art": [{"score": "99.00", "img": "picture/timg.jpeg"}, {"score": "77.00", "img": "picture/\u5927\u957f\u817f\u767d\u889c\u5b50\u5973\u751f\u9006\u5149\u62cd\u6444\u552f\u7f8e\u5199\u771f.jpg"}]}, {"name": "20190102", "art": [{"score": "100.00", "img": "picture/\u767d\u8863\u957f\u88d9\u5c11\u5973\u6237\u5916\u552f\u7f8e\u6e05\u7eaf\u5199\u771f.jpg"}, {"score": "56.00", "img": "picture/\u51ac\u5b63\u5c11\u5973\u6bdb\u8338\u8338\u4e0a\u8863\u5929\u53f0\u7eaf\u51c0\u552f\u7f8e\u7167.jpg"}, {"score": "54.00", "img": "picture/\u7a97\u8fb9\u5475\u6c14\u5c0f\u6e05\u65b0\u5236\u670d\u7f8e\u5973\u517b\u773c\u5199\u771f.jpg"}]}, {"name": "20190410", "art": []}]}
    for i in range(len(res['data'])):
        if len(res['data'][i]['art']) > 0:
            min = res['data'][i]['art'][0]['score']
        for j in range(i+1, len(res['data'])):
            if len(res['data'][j]['art'])>0:
                if res['data'][j]['art'][0]['score'] > min:
                    res['data'][i], res['data'][j] = res['data'][j], res['data'][i]

    print(res['data'])

