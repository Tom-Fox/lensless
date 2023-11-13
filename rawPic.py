import requests

def getRawPic(gps, direction, filename="streetview.jpg"):
    base_url = "https://maps.googleapis.com/maps/api/streetview?"
    
    lat = gps[0]
    lon = gps[1]
    
    params = {
        "size": "600x400",  
        "location": f"{lat},{lon}",  
        "heading": direction,  
        "key": "AIzaSyAFDq5A5VaEtsQZuGpe_oCbjLbPGoUuL7A"
    }
    
    # 发送 GET 请求
    response = requests.get(base_url, params=params)
    
    # 如果请求成功，保存图片
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Error: {response.status_code} - {response.text}")

get_street_view_image_by_heading(gps, heading)
# # 使用
# #api_key = "AIzaSyAFDq5A5VaEtsQZuGpe_oCbjLbPGoUuL7A"
# #lat, lon = 35.71199560076601, 139.76073339623915  
# heading = 90  # 东方




