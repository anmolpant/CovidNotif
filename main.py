from plyer import notification
import requests
import time
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "D:\Projects\CovidNotif\covidIcon.ico",
        timeout = 15
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
        #notifyMe("Made By", "Anmol Pant")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        #print(myHtmlData)
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = (myDataStr.split("\n\n"))

        states =['Delhi','Tamil Nadu']
        for item in itemList[0:33]:
            dataList = (item.split("\n"))
            if dataList[1] in states:
                print(dataList)
                notif = 'Cases of Covid-19'
                notif_text = f"State : {dataList[1]}\nCases : {dataList[2]}\nCured : {dataList[3]}\nDeaths : {dataList[4]} "
                notifyMe(notif, notif_text)
                time.sleep(2)