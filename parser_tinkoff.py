import requests
import pandas as pd

def parser_tinkoff(start, end):

    start = start
    end = end
    regionName = ['all', 'Амурская область', 'Камчатский край', 'Приморский край',
                  'Республика Саха (Якутия)', 'Сахалинская область', 'Хабаровский край']

    for reg in regionName:
        print(reg)

        url = f'https://index.tinkoff.ru/corona-index/papi/period_region_total?regionName={reg}&start={start}&end={end}'

        r = requests.get(url)

        df = pd.DataFrame(r.json()['consumerTotalPoints'])

        # print(df)

        writer = pd.ExcelWriter('tinkoff_index.xlsx', engine='openpyxl', if_sheet_exists='replace', mode='a')

        df.to_excel(writer, sheet_name=reg)
        writer.close()
        #writer.save()