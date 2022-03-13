import datetime
import time
import requests
from pprint import pprint



if __name__ == '__main__':


    now = datetime.datetime.now()
    end_date= datetime.datetime(now.year, now.month, now.day)
    start_date = end_date - datetime.timedelta(days=2)

    end_date_unix = int(end_date.timestamp())
    start_date_unix = int(start_date.timestamp())

    #print(start_date_unix)


    url = "https://api.stackexchange.com/2.3/questions"
    page = 1
    questions_links = []
    while True:
        params = {"page": page, "pagesize": 100, "fromdate": start_date_unix , "todate": end_date_unix, "order": "desc",
                  "sort": "activity", "tagged": "Python", "site": "stackoverflow"}
        response = requests.get(url=url, params=params)
        response_json = response.json()
        #print(response)
        #pprint(response_json)
        questions = response_json["items"]

        for question in questions:
            questions_links.append(question["link"])

        if response_json["has_more"]:
            page += 1
            time.sleep(0.33)
        else:
            #pprint(response_json)
            break

    print(f"Количество вопросов по Python за последние 2 дня составляет {len(questions_links)}")
    print("Ссылки на них:")
    print(questions_links)






