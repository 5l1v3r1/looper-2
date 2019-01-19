import re
from requests import get

try:
    from urllib.request import urlopen
except:
    from urllib import urlopen


#functions
def link_opener(link):
    print("Opening link: {}".format(link))
    try:
        header = get(link)
    except:
        try:
            link2 = 'http://www.' + link
            header = get(link2)
        except:
            try:
                link3 = 'https://www.' + link
                header = get(link3)
            except:
                pass

    return header.content

def converter(header):
    try:
        parsed_html = BeautifulSoup(header,
                                    features= 'html.parser')
        return parsed_html
    except Exception as err:
        print(err)

def link_generator(parsed_html, link):
    list_link = []
    for links in parsed_html.findAll('a'):
        if 'href' in links.attrs:
            list_link.append(links.attrs['href'])
    list_link = set(list_link)
    for a in list_link:
        if a.startswith('https://'+link) or a.startswith('http://'+link):
            link1.append(a)
        elif a.startswith('/'):
            link1.append(link+a)
    return set(link1)

def Regex(parsed_html):
    email_Regex = re.compile(r'''(
                [a-zA-Z0-9._%+-]+
                @
                [a-zA-Z0-9.-]+
                (\.[a-zA-Z]{2,4})
                )''',re.VERBOSE)
    try:
        text = str(parsed_html)
    except Exception as err:
        print(" {} \nFailed to read page!".format(err))
    matches = []

    for groups in email_Regex.findall(text):
        matches.append(groups[0])
    matches = set(matches)
    for emails in matches:
        if len(matches) > 0:
            return emails
        else:
            return "No email address found!!"


def looper(link, iter):
        try:
            html = link_opener(link)
            parsed_html = converter(html)
            all_emails = Regex(parsed_html)
            if iter == True:
		from bs4 import BeautifulSoup
                print('[*] Set to generate links')
                links = link_generator(parsed_html, link)
                print("[*] Generated links\n {}".format(links))
            else:
                pass
            return all_emails
        except:
            print("[-] Error 404")
