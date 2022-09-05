
from bs4 import BeautifulSoup
import requests
import re
from tkinter import *
from tkinter import ttk
import webbrowser




page = 1

st = -1
listOfPrices = []
listOfNames = []
listOfUrls = []
h3 = []
counter = 0

baseLink = "https://www.bolha.com"
a1 = ""


win = Tk()
win.geometry("1300x800")


#Frame
main_frame = Frame(win)
main_frame.pack(fill=BOTH, expand=1)

#Canvas
canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

#Scrollbar
scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scroll.pack(side=RIGHT, fill=Y)

#Canvas configuation
canvas.configure(yscrollcommand = scroll.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

#second Frame in canvas
secondFrame = Frame(canvas)


canvas.create_window((0,0), window=secondFrame, anchor="nw")

priceLabel = Label(secondFrame, text="price", width=15)
priceLabel.grid(row=0, column=0)

nameLabel = Label(secondFrame, text="name", width=30)
nameLabel.grid(row=0, column=1)

linkLabel = Label(secondFrame, text="link", width=55)
linkLabel.grid(row=0, column=2)
# sb = Scrollbar(, orient=VERTICAL)
# sb.grid(row=0, column=1, sticky=NS)




while st != 0:
    url = "https://www.bolha.com/nvidia-graficne-kartice?page="+str(page)
    result = requests.get(url)
    doc = BeautifulSoup(result.text,"html.parser")

    p1 = doc.find("div",class_="EntityList--Regular")
    
    if p1 ==  None:
        break;    

    prices = p1.find_all("div",class_="entity-prices")
    index = 0

    
    for pr in prices:
        tempDic = {}
        
        h3 = p1.find_all("h3", class_="entity-title")[index]
        p2 = pr.find_all("li")[0]
        p3 = pr.find("strong").text.strip()

        a2 = h3.find("a")
        linkToItem = a2.get('href')
        a1 = a2.text.strip()
        # print(a1 + "  |||"  + p3 + "|||  " + baseLink+linkToItem)

        numbers = re.findall("([0-9.]*[0-9]+)", p3)
        # tempDic['price'] = 0
        # tempDic['name'] = ""
        
        number1 = 0
        if (len(numbers) > 1):
            tempDic['price'] = int(numbers[0])+1

        elif (len(numbers) == 1):
            tempNum = numbers[0].split(".")
            index1 = 0
            
            while (len(tempNum) > index1):
                number1 *= 1000
                number1 += int(tempNum[index1])
                index1 += 1
             
            tempDic['price'] = number1
        
        else:
            tempDic['price'] = -999


        tempDic['name'] = a1
        tempDic['link'] = baseLink + linkToItem
        counter += 1


        
        # print(a1 + " " + str(number) + " " + linkToItem)

        listOfPrices.append(tempDic);   
        index += 1

    if (prices == 0):
        st += 1
    
    page += 1



def sorting(prices):
    return prices.get("price")

# listofPrices = listOfPrices.sort(key=sorting())
# print(counter)
newList = sorted(listOfPrices, key=lambda i: i['price'])
# print(newList)

position = 1
newIndex = 0
for thing in newList:
    tempLabel1 = Label(secondFrame, text=(str(thing['price'])+'€'))
    tempLabel1.grid(row=position, column=0)

    tempLabel2 = Label(secondFrame, text=thing['name'])
    tempLabel2.grid(row=position, column=1)

    tempLabel3 = Label(secondFrame, text=thing['link'], fg="blue", cursor="hand2")
    
    tempLabel3.grid(row=position, column=2)
    
    tempLabel3.bind("<Button-1>", lambda e: callback(tempLabel3.cget("text")))

    newIndex += 1
    position += 1


def callback(url):
    
    webbrowser.open_new(url)


# url = "https://www.bolha.com/nvidia-graficne-kartice?page="+str(page)
# result = requests.get(url)
# doc = BeautifulSoup(result.text,"html.parser")
# # 
# # p0 = prices
# p1 = doc.find("div",class_="EntityList--Regular")
# h3 = p1.find_all("h3", class_="entity-title")[0]
# a1 = h3.find("a").text.strip()




# prices = p1.find_all("div",class_="entity-prices")[0]
# p2 = prices.find("li")
# p3 = p2.find("strong").text.strip()

# print(a1 + ": " + p3)



win.mainloop()
