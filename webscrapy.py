import requests
from bs4 import BeautifulSoup


html_text= requests.get("https://group.jumia.com/")
# soup= BeautifulSoup(html_text,"html.parser")
print(html_text.text)
# job= soup.find("li", class_= "clearfix job-bx wht-shd-bx" )
# company_name= job.find("h3", class_= "joblist-comp-name")
# print(company_name)
                    