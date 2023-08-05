# 1st step import modules
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest



job_titles = []
job_skillss = []
location_namee = []
company_namee = []



# 2nd step use requests to fetch the url
URL = 'https://wuzzuf.net/search/jobs/?q=python&a=navbl'
page = requests.get(URL)
# 3rd step save page content/markup
src = page.content

# 4th step create soup object to parse content
soup = BeautifulSoup(src, "lxml")

# 5th step extract information
job_title = soup.find_all('h2', class_ ='css-m604qf')
company_name = soup.find_all('a',class_ ='css-17s97q8')
location_name = soup.find_all('span', class_= 'css-5wys0k')
job_skills = soup.find_all('div', class_ = 'css-y4udm8')

# 6th step
for i in range(len(job_title)):
    job_titles.append(job_title[i].get_text())
    company_namee.append(company_name[i].get_text())
    location_namee.append(location_name[i].get_text())
    job_skillss.append(job_skills[i].get_text())




list = [job_titles,company_namee,location_namee,job_skillss]
exported = zip_longest(*list)

with open("/Users/Horus/Projects/wuzzuf.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title","company_name","location_name","job_skills"])
    wr.writerows(exported)




