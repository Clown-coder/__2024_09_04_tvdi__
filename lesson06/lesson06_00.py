import requests


url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'

response = requests.get(url)
#print(type(response))   #type 為 Response

data = response.json()
# print(data,type(data))


"""
從online json viewer 去查看資料 可以看到
這個檔案裏面有很多key
其中要的內容在records裡面
因此可以用以下方法來呼叫
其中
for items in data['records']
這個 data['record'] 叫做 subscript

補充
具體來說，這種結構表示：

data 是一個字典。
'record' 是 data 字典中的一個鍵。
data['record'] 表示存取該鍵所對應的值。
"""

for items in data['records']:
    print(items)



