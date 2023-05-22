from bs4 import BeautifulSoup
import pandas 
import time
from selenium import webdriver
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("C:/Users/yousu/Downloads/PRO-C127-Student-Boilerplate-Code-main/PRO-C127-Student-Boilerplate-Code-main/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
scraped_data=[]
def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table=soup.find("table", attrs={"class","wikitable"})
    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find_all('tr')
    for row in table_rows:
        table_cols = row.find_all('td')
        temp_list = []
        for col_data in table_cols:
            data=col_data.text.strip()
            temp_list.append(data)
    scraped_data.append(data)
scrape()
stars_data = []
for i in range(0,len(scraped_data)):
    Star_names = scraped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scraped_data[i][3]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)
headers = ['Star_names','Distance','Mass','Radius','Luminosity']

star_df_1 =pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv('scraped_data.csv',index=True,index_label="id")

try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,"html.parser")
        temp_list=[]
        for tr_tag in soup.find_all("tr", attrs={"class":"fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_planets_data.append(temp_list)
except:
        time.sleep(1)
        scrape_more_data(hyperlink)

planet_df_1 = pd.DataFrame(planets_data, columns=headers)


planet_df_1.to_csv('updated_scraped_data.csv',index=True, index_label="id")