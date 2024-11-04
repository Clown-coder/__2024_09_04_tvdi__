import requests
import sqlite3

def get_sitename()->list[str]:
    """
    docString
    parameter:
    return:
        傳出所有站點名稱
    """
    conn = sqlite3.connect("AQI.db")
    with conn:
        cursor = conn.cursor()
        sql= """SELECT DISTINCT sitename FROM record"""
        cursor.execute(sql)
        sitenames = [items[0] for items in cursor.fetchall()]   #comprehension寫法

    return sitenames

def get_county()->list[str]:
    """
    docString
    parameter:
    return:
        傳出所有城市名稱
    """
    conn = sqlite3.connect("AQI.db")
    with conn:
        cursor = conn.cursor()
        sql= """SELECT DISTINCT county FROM record"""
        cursor.execute(sql)
        counties = [items[0] for items in cursor.fetchall()]   #comprehension寫法

    return counties



def get_selected_data(sitename:str)->list[list]:
    '''
    使用者選擇麼sitename,並將sitename傳入
    Parameter:
        sitename: 站點的名稱
    Return:
        所有關於此站點的相關資料
    '''
    conn = sqlite3.connect("AQI.db")
    with conn:
        cursor = conn.cursor()
        sql= """
            SELECT date,county,AQI,PM25,status,lat,lon
            FROM record 
            WHERE sitename=?
            ORDER  BY date ASC

            """
        cursor.execute(sql,(sitename,))
        sitename_list = [list(items) for items in cursor.fetchall()]
        return sitename_list

    
    
    
def download_data():
    conn = sqlite3.connect("AQI.db")
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'

    try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
    except Exception as e:
                print(e)

    else:
        sitenames = set()
        with conn:
            cursor =conn.cursor() 
            for items in data['records']:
                sitenames = items['sitename']
                county = items['county']
                aqi = int(items['aqi']) if items['aqi'] !='' else 0
                status = items['status']
                pm25 = float(items['pm2.5']) if items['pm2.5'] !='' else 0
                date = items['datacreationdate']
                lat = float(items['latitude']) if items['latitude'] !='' else 0
                lon = float(items['longitude']) if items['longitude'] != '' else 0
                sql = '''
                    INSERT OR IGNORE INTO record(sitename,county,aqi,status,pm25,date,lat,lon)
                    VALUES (?, ?, ?, ?,?, ?,?,?);
                    ''' 
                cursor.execute(sql,(sitenames,county,aqi,status,pm25,date,lat,lon))
