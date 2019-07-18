from django.shortcuts import render
from . import formofurl
from . import function_doc
import requests
import re
import json
import browser_cookie3
cj = browser_cookie3.chrome()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# Create your views here.
def URL(request):
    if request.method == "POST":
        form = formofurl.SubmitEmbed(request.POST)
        if form.is_valid():
            try:
                url = form.cleaned_data['url']
                d1 = {}
                # print(url)
                if (str(url).__contains__("AllItems")):
                    cont = requests.get(url, cookies=cj)
                    data1 = cont.text
                    # print(url)
                    # print(data1)
                    urllist = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
                    wopi = urllist.findall(data1)
                    inlines = []
                    # print(wopi)
                    for j in wopi:
                        if (str(j).__contains__("WopiFrame")):
                            inlines.append(j)
                    # print(inlines)
                    for itemx in inlines:
                        if itemx in inlines:
                            inlines.remove(itemx)
                    # print(inlines)
                    url2 = []
                    for item in inlines:
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
                                url2.append(url1.split(".docx", 1)[0] + '.docx')
                                # print(url2)
                            else:
                                url2.append(url1.split(".doc", 1)[0] + '.doc')
                                # print(url2)

                        except IndexError:
                            url2.append(url1.split(".doc", 1)[0] + '.doc')
                    for item in url2:
                        # d1[str(item).split("file=", 1)[1].replace("%20",' ').replace("&amp;action=default','','915','0','0','0xb008431061','','')",'')] = [str(requests.get('http://10.97.157.174:5000/url/' + item).content.decode().replace("[\n",'').replace("\n",'').replace("\\\\x15\\\\",'').replace("07\\\\x07",''))]
                        d1[str(item).split("file=", 1)[1].replace("%20", ' ').replace(
                            "&amp;action=default','','915','0','0','0xb008431061','','')", '')] = [str(
                            requests.get('http://10.97.157.174:5000/url/' + item).content.decode("ascii", "replace").replace("\n",
                                                                                                           '').replace(
                                "\n", '').replace("\\\\x15\\\\", '').replace("07\\\\x07", '').replace("\\\\r",'').replace("\\\\x",'').replace("\\\\n",'').replace("\\\\t",'     '))]
                    # # print(d1)
                if (str(url).__contains__('WopiFrame')):
                    urlx = str(url).replace('/:w:/r', '')
                    urlx = str(urlx).replace('WopiFrame', 'download')
                    urlx = str(urlx).replace('sourcedoc', 'Uniqueid')
                    urlx = str(urlx).replace('?', '$32')
                    url1 = str(urlx).replace('-', '%2D')
                    char = '.doc'
                    test = url1.find(char)
                    url2 = []
                    try:
                        str2 = url1.__getitem__(test + 4)
                        if (str2 == 'x'):
                            url2.append(url1.split(".docx", 1)[0] + '.docx')
                            # url2 = url1.split(".docx", 1)[0] + '.docx'
                            print(url2)
                        else:
                            url2.append(url1.split(".doc", 1)[0] + '.doc')
                            # url2 = url1.split(".doc", 1)[0] + '.doc'
                            print(url2)

                    except IndexError:
                        # url2 = url1.split(".doc", 1)[0] + '.doc'
                        url2.append(url1.split(".doc", 1)[0] + '.doc')
                        print(url2)

                    for item in url2:
                        # d1[str(item).split("file=", 1)[1].replace("%20",' ').replace("&amp;action=default','','915','0','0','0xb008431061','','')",'')] = [str(requests.get('http://10.97.157.174:5000/url/' + item).content)]
                        d1[str(item).split("file=", 1)[1].replace("%20", ' ').replace(
                            "&amp;action=default','','915','0','0','0xb008431061','','')", '')] = [str(
                            requests.get('http://10.97.157.174:5000/url/' + item).content.decode().replace("[\n",
                                                                                                           '').replace(
                                "\n", '').replace("\\\\x15\\\\", '').replace("07\\\\x07", ''))]

                if(str(url).__contains__('download')):
                    url1 = str(url).replace('?', '$32')
                    char = '.doc'
                    test = url1.find(char)
                    url2= []
                    # print(url1)
                            # try:
                            #     str2 = url1.__getitem__(test + 4)
                            #     if(str2 == 'x'):
                            #         url2 = url1.split(".docx", 1)[0] + '.docx'
                            # except IndexError:
                            #     url2 = url1.split(".doc", 1)[0] + '.doc'
                    try:
                        str2 = url1.__getitem__(test + 4)
                        # print(str2)
                        if (str2 == 'x'):
                                # url2 = url1.split(".docx", 1)[0] + '.docx'
                            url2.append(url1.split(".docx", 1)[0] + '.docx')
                            print(url2)
                        else:
                                # url2 = url1.split(".doc", 1)[0] + '.doc'
                            url2.append(url1.split(".doc", 1)[0] + '.doc')
                            print(url2)

                    except IndexError:
                            # url2 = url1.split(".doc", 1)[0] + '.doc'
                        url2.append(url1.split(".doc", 1)[0] + '.doc')
                        print(url2)

                    for item in url2:
                        # d1[str(item).split("file=", 1)[1].replace("%20",' ').replace("&amp;action=default','','915','0','0','0xb008431061','','')",'')] = [str(requests.get('http://10.97.157.174:5000/url/' + item).content)]
                        d1[str(item).split("file=", 1)[1].replace("%20", ' ').replace(
                            "&amp;action=default','','915','0','0','0xb008431061','','')", '')] = [str(
                            requests.get('http://10.97.157.174:5000/url/' + item).content.decode().replace("[\n",
                                                                                                            '').replace(
                                    "\n", '').replace("\\\\x15\\\\", '').replace("07\\\\x07", ''))]

            except:
                return ("URL is incompatible with the content you are looking for")

            # return render(request, 'output.html', {'url': url, 'data': d1})

            # r = requests.get('http://10.97.157.174:5000/url/' + url2)
            # json = r.json()
            # # json = r.json().dumps

            return render(request, 'output.html', {'url': url, 'data': d1})
    else:
        form = formofurl.SubmitEmbed()
        return render(request, 'FMurl.html', {'form': form})
