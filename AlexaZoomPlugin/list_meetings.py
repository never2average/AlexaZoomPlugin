import requests


def listmeetings(pageno=1, userid="foor@bar.com", jwt=""):
    url = "https://api.zoom.us/v2/users/{}/meetings"
    url = url.format(userid)
    querystring = {"type":"upcoming","page_size":"5","page_number":str(pageno)}
    headers = {
        'Accept': "application/json, application/xml",
        'Content-Type': "application/json",
        'Authorization': jwt
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()