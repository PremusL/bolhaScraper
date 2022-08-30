from bs4 import BeautifulSoup
import requests

page = 1

st = -1
listOfPrices = []
listOfNames = []
listOfUrls = []






while st != 0:
    url = "https://www.bolha.com/nvidia-graficne-kartice?page="+str(page)
    result = requests.get(url)
    doc = BeautifulSoup(result.text,"html.parser")

    p1 = doc.find("div",class_="EntityList--Regular")
    
    if p1 ==  None:
        break;    

    prices = p1.find_all("div",class_="entity-prices")
    index = 0

    counter = 0
    tempDic = {}
    for pr in prices:
        h3 = p1.find_all("h3", class_="entity-title")[index]
        a1 = h3.find("a").text.strip()
        p2 = pr.find_all("li")[0]
        p3 = pr.find("strong").text.strip()
        # print(p3, ": ", a1)

        # orderedList[counter] = p3 
        tempDic['price'] = p3
        tempDic['name'] = a1

        listOfPrices.append(tempDic)

        
        st += 1
        index += 1
    

    page += 1

def sorting(prices):
    return prices.get("price")

listofPrices = listOfPrices.sort(key=sorting)
# print(len(listOfPrices))
print(listOfPrices)


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



