import requests
from bs4 import BeautifulSoup 
import re 
import pandas as pd 

# Get website HTML
response = requests.get("https://www.jajanken.net/en/sakuhins/aAg89lnKZQ")
# Raise any problems
response.raise_for_status()

# Parse HTML and get the rows that store chapter data
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', class_='chapters')
rows = table.find_all('tr')

chapter_data = []
for row in rows:
    # 1. Sequence
    seq_td = row.find('td', class_='sequence')
    if not seq_td:
        continue # skip header rows
    sequence = seq_td.text.strip()

    # 2. Issue date
    issue_td = row.find('td', class_='issue')
    issue_a = issue_td.find('a')
    href = issue_a['href'] if issue_a else ""
    # The href looks like "/en/issues/1998-06-01/"
    issue_date = href.split('/')[-2] if href else None

    # 3. Chapter number
    title_td = row.find('td', class_='title')
    title_text = title_td.text.strip()
    # The title text looks like "Chapter 1: Romance Dawn"
    match = re.search(r'Chapter (\d+)', title_text)
    if match:
        chapter_number = match.group(1)
    else:
       # If it doesn't say "Chapter X", record whole text to investigate
       chapter_number = title_text

    # Put it all in a dictionary
    chapter_info = {
        'sequence': sequence,
        'date': issue_date,
        'chapter': chapter_number
    }
       
    chapter_data.append(chapter_info)

df = pd.DataFrame(chapter_data)
df.to_csv('chapter_data.csv', index=False)








