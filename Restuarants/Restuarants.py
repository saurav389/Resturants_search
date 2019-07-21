import requests
from bs4 import BeautifulSoup
base_url = 'https://www.swiggy.com/'
swiggy_r = requests.get(base_url)
print(swiggy_r.status_code)#200
swiggy_soup = BeautifulSoup(swiggy_r.text,'html.parser')
#print(swiggy_soup.prettify())
#print(swiggy_soup.find_all('a'))
restu = 'jamshedpur/restaurants'
locname = input("Enter city name")
#print(swiggy_soup)
    #input("Enter Your location")
for location in swiggy_soup.find_all('a',{'class':'_3TjLz b-Hy9'}):
    loc = location.text
    if loc == locname:
        print(loc)
        url = base_url + locname
        print(url)
        swiggy_re = requests.get(url)
        print(swiggy_re.status_code)  # 200
        swiggy_soupe = BeautifulSoup(swiggy_re.text, 'html.parser')
        #print(swiggy_soupe)
        #print(swiggy_soupe.find_all('a',{'class':'_1j_Yo'}))
        restaurants = swiggy_soupe.find_all('div',{'class':'_3XX_A'})
        count = 0
        for rest in restaurants:
            #print(rest)
            name = rest.findAll('div',{'class':'nA6kb'})[0].text
            print(count+1,"\trestaurant name = ",name)
            title = rest.findAll('div',{'class':'_1gURR'})[0].text
            print("\ttype = ",title)
            time_cost = rest.findAll('div',{'class':'_3Mn31'})[0].text
            print("\tTime & cost = ",time_cost)
            #offer = rest.findAll('div',{'class':'Zlfdx'})[0].text
            #print("OFFER = ",offer)

            count=count+1
        print("\n\nTotal",count,"Restaurants found ")
