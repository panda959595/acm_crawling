import requests
from bs4 import BeautifulSoup
import copy



pb_num = input()

f = open('id_list.txt','r')
id_list = f.readlines()

for id in id_list:
    id=id[:-1]
    res = requests.get("https://www.acmicpc.net/user/"+id)
    soup = BeautifulSoup(res.content, 'html.parser')
    pb_list = soup.find_all(class_='problem_number')
    flag = False
    for solve_pb in pb_list:
        print solve_pb.get_text()
        print type(solve_pb.get_text())
        str = copy(solve_pb)+""
        print str
        print type(str)
        if str(solve_pb.get_text()) is '1000':
            print 111
        a = input()

        if pb_num is solve_pb.get_text():
            flag = True
            print 1
            break
    if flag is True:
        print id
    else :
        print -1
f.close()


# print a[1].get_text()