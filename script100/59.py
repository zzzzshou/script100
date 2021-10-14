import json
import re

import requests





def Get_hot():
    url = 'https://www.kuaishou.com/'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 '
                      'Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
    }

    response = requests.request("GET", url, headers=headers)
    res = response.text

    resu = re.findall('({"rank.*?VisionHotRankItem"})',res)
    print(resu)
    '''
    pattern = re.compile('[\u4e00-\u9fa5]":(.*?),"VisionHotRankItem')
    resu = pattern.search(res)
    print(resu.groups())
    '''

    '''
    
    res = response.text.split(';(function()')
    resu = res[0]
    res = resu.split('window.__APOLLO_STATE__=')
    resu = res[1]  # 至此就取出了热播所有的信息，为了便于观察。对数据进行处理一下
    json_data = json.loads(resu)
    # print(resu)
    names_list = json_data['defaultClient']['$ROOT_QUERY.visionHotRank({"page":"home"})']['items']
    # print(names_list)
    for i in range(0, 49):
        name = names_list[i]['id']
        hotValue = json_data['defaultClient'][name]['hotValue']
        poster = json_data['defaultClient'][name]['poster']
        print('名称：' + name)
        print('热度：' + hotValue)
        print('封面图片:' + poster)
    
    '''

'''
https://www.kuaishou.com/graphql
Host: www.kuaishou.com
Connection: keep-alive
Content-Length: 622
accept: */*
content-type: application/json
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36
Origin: https://www.kuaishou.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.kuaishou.com/short-video/3x2m3pijyzfra2q?authorId=3x5taxva8rnfxps&streamSource=find&area=homexxbrilliant
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: 
也不晓得给我买串香蕉 评论
替换掉3x2m3pijyzfra2q视频ID
3x5taxva8rnfxps作者ID

1_v/2000962649046509330_xpcwebhomexxbrilliant0 exptag 这三个可以通过operationName=brilliantDataQuery这个操作获取


{"operationName":"visionAddComment","variables":{"photoId":"3x2m3pijyzfra2q","photoAuthorId":"3x5taxva8rnfxps","content":"也不晓得给我买串香蕉","expTag":"1_v/2000962649046509330_xpcwebhomexxbrilliant0"},"query":"mutation visionAddComment($photoId: String, $photoAuthorId: String, $content: String, $replyToCommentId: ID, $replyTo: ID, $expTag: String) {\n  visionAddComment(photoId: $photoId, photoAuthorId: $photoAuthorId, content: $content, replyToCommentId: $replyToCommentId, replyTo: $replyTo, expTag: $expTag) {\n    result\n    commentId\n    content\n    timestamp\n    status\n    __typename\n  }\n}\n"}
{"operationName":"visionFollow","variables":{"touid":"3x625ixny9akbsy","ftype":1,"followSource":3,"expTag":"1_i/2000960425902201474_xpcwebhomexxbrilliant0"},"query":"mutation visionFollow($touid: String, $ftype: Int, $followSource: Int, $expTag: String) {\n  visionFollow(touid: $touid, ftype: $ftype, followSource: $followSource, expTag: $expTag) {\n    result\n    followStatus\n    hostName\n    error_msg\n    __typename\n  }\n}\n"}
{"operationName":"visionFollow","variables":{"touid":"3x625ixny9akbsy","ftype":2,"followSource":3,"expTag":"1_i/2000960425902201474_xpcwebhomexxbrilliant0"},"query":"mutation visionFollow($touid: String, $ftype: Int, $followSource: Int, $expTag: String) {\n  visionFollow(touid: $touid, ftype: $ftype, followSource: $followSource, expTag: $expTag) {\n    result\n    followStatus\n    hostName\n    error_msg\n    __typename\n  }\n}\n"}
第二条数据包是关注
第三条是取关

'''

if __name__ == '__main__':
    Get_hot()
