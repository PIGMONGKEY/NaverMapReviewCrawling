import requests

class NaverAPI:
    def geocoding(self, addr):
        client_id = "n4vlz6cuy2"
        client_secret = "lJKtQFtBLyBOyyLLfQ2GXJ6VD6HJlS8VMkAyqrtW"

        url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?{addr}"
        headers = {"X-NCP-APIGW-API-KEY-ID": client_id,
                   "X-NCP-APIGW-API-KEY": client_secret}

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            
