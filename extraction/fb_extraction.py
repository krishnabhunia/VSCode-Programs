import requests
from bs4 import BeautifulSoup

# URL of the Facebook friends page
url = input("Enter Facebook URL about friends \
list https://www.facebook.com/[friends_name]/friends")

# Headers (replace cookies with authenticated session cookies)
headers = {
    "User-Agent": "Your User-Agent",
    "Cookie": "Your-Cookie"
}

# Fetch the page
response = requests.get(url, headers=headers)

# Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract friend names
names = [tag.text for tag in soup.find_all("a", class_="friend-class-name")]  
# Replace 'friend-class-name' with the actual class name.
print(names)
