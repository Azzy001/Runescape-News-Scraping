# for communicating with website
import requests
# for the extracting html content
from bs4 import BeautifulSoup
# for importing table features
from prettytable import PrettyTable

# creating a table using the PrettyTable function
runescape_table = PrettyTable()
# Creating column names
runescape_table.field_names = ["Event Number", "Post Title", "Posted by", "Posted Date"]

# Runescape news link
url = "https://secure.runescape.com/m=news/#_ga=2.186047341.511212105.1667843989-948072805.1667843989"
response = requests.get(url)

# extracting all html content from the below html tags and classes
soup = BeautifulSoup(response.content, "lxml")
date = soup.find_all("time", class_="news-list-article__date")
author = soup.find_all("a", class_="news-list-article__category")
title = soup.find_all("a", class_="news-list-article__title-link")

# will increment by 1 each time the range loop in line 19 runs
num = 0

# to increment on each text from the extracted content above
for i in range(len(date)):
    num += 1
    # placeholders will be filled by extracted texts
    runescape_table.add_row([f"{num}", 
                             f"{title[i].get_text()}", 
                             f"{author[i].get_text()}", 
                             f"{date[i].get_text()}"])

print("\nWelcome to the Runescape Live News Program\n")
# printing the table after extraction
print(runescape_table)
print("\nRun this program to get the latest news of Runescape, from double xp, events to updates!\n")
