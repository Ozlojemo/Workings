import requests
from bs4 import BeautifulSoup

print("put some skill that you are not familiar with")
unfamiliar_skill= input(">")
print(f"filtering out {unfamiliar_skill}")
html_text= requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=PYTHON&txtLocation=").text
soup= BeautifulSoup(html_text,"lxml")
jobs= soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
for job in jobs:
    Published_date= job.find("span", class_= "sim-posted").span.text
    if "few " in Published_date:
        company_name= job.find ("h3",class_ = "joblist-comp-name").text.replace("","")
        skills= job.find("span", class_= "srp-skills").text.replace("","")
        more_info= job.header.h2.a["href"]
        # print(f""" company Name:{company_name} Required Skills:{skills} """)
        print(f"company_name: {company_name.strip()}")
        print(f"Required Skill: {skills.strip()}")
        print(f"more Info:{more_info}")
        
        print()

