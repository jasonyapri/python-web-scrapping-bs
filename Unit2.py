# Course: https://youtu.be/XVv6mJpFOb0
from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}...')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text)
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    company_names = {}
    count = 0

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text.strip()
        if published_date == "Posted few days ago": # Execute only if the job is posted a few days ago
            
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            if company_name in company_names.keys():
                company_names[company_name] += 1
            else:
                company_names[company_name] = 1

            skills = job.find('span', class_ = 'srp-skills').text.strip()
            url = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as file:
                    file.write(f'Company Name: {company_name}\n')
                    file.write(f'Required Skills: {skills}\n')
                    file.write(f'Url: {url}\n\n')
                    count+= 1
                print(f"File saved in {index}.txt")
    # print(count)

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} minute(s)...', end = '\n\n')
        time.sleep(time_wait * 60)

