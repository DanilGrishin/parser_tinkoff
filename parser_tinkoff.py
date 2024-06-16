import requests
import pandas as pd

def parser_tinkoff(start, end):

    start = start
    end = end
    regionName = ['all', 'Амурская область', 'Камчатский край', 'Приморский край',
                  'Республика Саха (Якутия)', 'Сахалинская область', 'Хабаровский край']

    writer = pd.ExcelWriter('tinkoff_index.xlsx', engine='openpyxl', if_sheet_exists='replace', mode='a')
#
    for reg in regionName:
        print(reg)

        url = f'https://index.tinkoff.ru/corona-index/papi/period_region_total?regionName={reg}&start={start}&end={end}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
            'Accept': 'application/json',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        # http_proxy = "http://ip:port"
        # https_proxy = "https://ip:port"

        # proxyDict = {
        #     # "http": http_proxy,
        #     "https": https_proxy
        # }

        r = requests.get(url, headers=headers) # , proxies=proxyDict

        df = pd.DataFrame(r.json()['consumerTotalPoints'])

        # print(df)

        df.to_excel(writer, sheet_name=reg)

    writer.close()
    # #writer.save()