import requests
import bs4

def unheartReq(id, cookie):
    req = requests.post("https://weheartit.com/entry/"+id+"/heart",data="_method=delete",headers={"cookie":cookie})

cookie = input("Input cookie:")
profilename = input("Profile name:")

firstpage = requests.get("https://weheartit.com/"+profilename+"?scrolling=true&page=1")

while firstpage.text != "":
    firstpage = requests.get("https://weheartit.com/"+profilename+"?scrolling=true&page=1")
    bs = bs4.BeautifulSoup(firstpage.content, "html.parser")
    elements = bs.find_all(class_="entry grid-item")
  
    for x in elements:
        postid = x['data-entry-id']
        print("Attempting post "+ postid)
        unheartReq(postid, cookie)

print("done")        