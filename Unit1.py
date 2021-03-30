# Course: https://youtu.be/XVv6mJpFOb0
from bs4 import BeautifulSoup

try:
    with open('main.html', 'r') as html_file:
        content = html_file.read()
        # print(content)
        
        soup = BeautifulSoup(content, 'lxml')
        # print(soup.prettify())
        # tags = soup.find('h5') : Find first

        # Course names
        # courses_html_tags = soup.find_all('h5')
        # for course in courses_html_tags:
        #     print(course.text)

        # Course Cards
        course_cards = soup.find_all('div', class_ = 'card')
        for course in course_cards:
            course_name = course.h5.text
            course_price = course.a.text.split()[-1]
            print(f"{course_name} costs {course_price}")

except FileNotFoundError:
    print('not found')

