import requests
import csv
from bs4 import BeautifulSoup
import os



def crawl(f,class_attr):
    # html = requests.get(base_url).text
    html  = f.read()
    soup = BeautifulSoup(html,'html.parser')


    list_rows = soup.find_all('tr')
    sub_re_list = []
    # raw_result = list_rows[13].text.strip()
    # list_each = raw_result.split('\n')
    # print(list_each)
    for i in range(12,80):
        raw_result = list_rows[i].text.strip()
        list_each = raw_result.split('\n')
        if len(list_each)>5:
            need_list_each=[list_each[4],list_each[5],list_each[0]]

            sub_re_list.append(need_list_each)

    return sub_re_list


if __name__ =='__main__':
    # 'one-third column omega'
    # base_url = 'http://cdiac.ess-dive.lbl.gov/climate/temp/us_recordtemps/states.html'
    # output_file = 'digit_abbr.csv'
    # result_list = []
    # result_list.append(crawl(base_url,'one-third column alpha'))
    # result_list.append(crawl(base_url, 'one-third column'))
    # result_list.append(crawl(base_url, 'one-third column omega'))
    # # open(os.path.join(os.path.expanduser('~'), output_file, 'w'))


    # wikitable sortable jquery-tablesorter
    file = 'U.S._state_abbreviations.htm'
    f = open(file, 'r')
    base_url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
    output_file = 'digit_abbr.csv'
    result_list = []
    result_list.append(crawl(f, 'wikitable sortable'))


    with open(output_file, 'w')  as outfile:
        outfile.write("State Number,State Abbreviation,State\n")
        for each in result_list:

            for one in each:
                print(one)
                try :
                    int(one[0])
                    outfile.write("{},{},{}\n".format(one[0],one[1],one[2]))
                except:
                    pass