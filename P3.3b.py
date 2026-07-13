#3b. Write a python code to retrieve data from HTML file.
from bs4 import BeautifulSoup

# Step 1: Open and read the HTML file
with open('Practical3.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Step 2: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract and print all the text from the HTML
text = soup.get_text()

print("Extracted data:")
print(text)
