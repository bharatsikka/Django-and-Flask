# url='https://nokia.sharepoint.com/sites/Service_Documentation/Published_Documentation/Nokia%20shared/Forms/AllItems.aspx?RootFolder=%2Fsites%2FService_Documentation%2FPublished_Documentation%2FNokia%20shared%2FIPR%20and%20Innovations%2FEPOLINE&FolderCTID=0x01200011AE13B60450E0498F4D5CA1B700634A&View=%7BAF33C617-1111-4C9D-BC3C-F0AD7048E262%7D'
url = 'https://nokia.sharepoint.com/sites/Service_Documentation/Published_Documentation/Nokia%20shared/Forms/AllItems.aspx?RootFolder=%2Fsites%2FService_Documentation%2FPublished_Documentation%2FNokia%20shared%2FPortals%20and%20integrations%2FIntranet%20Portal%20%28EPS%29%2FUP%20Documents&FolderCTID=0x01200011AE13B60450E0498F4D5CA1B700634A&View=%7BAF33C617-1111-4C9D-BC3C-F0AD7048E262%7D'
import requests
import browser_cookie3

cj = browser_cookie3.chrome()

cont = requests.get(url,cookies = cj)
data =cont.text
import re

urllist = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

wopi = urllist.findall(data)
new = []
for i in wopi:
    if(str(i).__contains__("WopiFrame")):
        new.append(i)
print(new)
for item in new:
    if item in new:
        new.remove(item)
# print(new[2])
url2 = []
for item in new:
    urlx = str(item).replace('/:w:/r', '')
    urlx = str(urlx).replace('WopiFrame', 'download')
    urlx = str(urlx).replace('sourcedoc', 'Uniqueid')
    urlx = str(urlx).replace('?', '$32')
    url1 = str(urlx).replace('-', '%2D')
    char = '.doc'
    test = url1.find(char)
    try:
        str2 = url1.__getitem__(test + 4)
        if (str2 == 'x'):
            url2.append( url1.split(".docx", 1)[0] + '.docx')
            # print(url2)
        else:
            url2.append(  url1.split(".doc", 1)[0] + '.doc')
            # print(url2)

    except IndexError:
            url2.append(url1.split(".doc", 1)[0] + '.doc')
            # print(url2)

print(url2)
import json
jsond = []
d1 = {}
for item in url2:
    d1[str(item).split("file=", 1)[1]] = [str(requests.get('http://10.97.157.174:5000/url/' + item).content)]

# dict_ = {"20090209.02s1.1_sequence.txt": [645045714, 3559.6422951221466, 206045184], "20090209.02s1.2_sequence.txt": [645045714, 3543.8322949409485, 234618880]}
values = [{"file_name": k, "file_information": v} for k, v in d1.items()]
json.dumps(values, indent=4)
# print(values)

