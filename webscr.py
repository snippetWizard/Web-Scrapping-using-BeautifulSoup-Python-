from bs4 import BeautifulSoup
import requests
import pandas as p

url = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&as-pos=2&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=35ef8f72-f65f-4eff-9e3d-025042f8a7f6&as-backfill=on"

response = requests.get(url)
print(response)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

# Creating a empty lists to store the data we have scrapped
titles = []
prices = []
images = []

for f in soup.find_all('div', attrs={'class':'_2kHMtA'}):
    title = f.find('div', attrs={'class':'_4rR01T'})
    # print(title.string)
    price = f.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    # print(price.string)
    image = f.find('img', attrs={'class':'_396cs4 _3exPp9'})
    # print(images.get('src'))

    # Appending the scrapped data into empty lists 
    titles.append(title.string)
    prices.append(price.string)
    images.append(image.get('src'))



# now we have to save the list items in csv file or we can directely save it on database from django web framework
dict = {'Title of the product':titles, 'Price of the product':prices, 'Image src':images}

fm = p.DataFrame(dict)
fm.to_csv('laptops_data.csv')
    