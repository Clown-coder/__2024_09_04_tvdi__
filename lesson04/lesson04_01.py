import requests
from requests import Response



def main():
    url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=5481753E-52AF-40DA-9A8A-9E192B245E13'
    res:Response = requests.request('GET',url)

    if res.status_code ==200:
        print("Download Successfully")
        res.encoding='utf-8'
        content:str = res.text
        with open('a1.csv','w',encoding='utf8',newline='') as file:
            print(type(file))       #TextWrapper 的實體
            file.write(content)

    else:
        print("Download Fail")

if __name__ =='__main__':
    main()


"""
3. __name__ 和 '__main__' 的概念：
__name__ 是 Python 的一個內建變數，它代表了當前模塊的名稱。
如果這個 Python 檔案是直接執行的（例如通過 python script.py），那麼 __name__ 的值會被設置為 '__main__'。
__main__ 是一個特殊的字串，用於標識當前運行的 Python 腳本。
詳細解釋：
當 Python 執行一個腳本時，每個模塊（包括腳本本身）都有一個 __name__ 變數。
如果這個腳本是直接執行的（如通過命令行或其他方式），那麼 __name__ 會被設置為 '__main__'，並且 if __name__ == '__main__' 這個條件會為 True。
如果這個腳本是被其他模塊導入（例如用作模塊或庫），那麼 __name__ 會是這個模塊的名稱，而不是 '__main__'，這樣條件判斷會是 False，main() 函式就不會被執行。

"""


