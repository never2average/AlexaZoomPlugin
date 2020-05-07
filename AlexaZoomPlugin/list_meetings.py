import requests
from datetime import datetime, timedelta
from dateutil.parser import parse


def listmeetings(pageno=1, userid="foo@bar.com", jwt=""):
    url = "https://api.zoom.us/v2/users/{}/meetings"
    url = url.format(userid)
    querystring = {
        "type":"upcoming",
        "page_size":"100",
        "page_number":str(pageno)
    }
    headers = {
        'Accept': "application/json, application/xml",
        'Content-Type': "application/json",
        'Authorization': jwt
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    today_s_meetings = []
    for i in data["meetings"]:
        if (
            parse(i["created_at"]) >= datetime.now() and 
            parse(i["created_at"]) <= datetime.now()+timedelta(days=1)
        ):
            today_s_meetings.append(i) 
    data["meetings"] = today_s_meetings
    data["statusCode"] = response.status_code
    return data