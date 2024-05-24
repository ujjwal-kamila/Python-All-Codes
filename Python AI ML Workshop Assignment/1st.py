# Import necessary libraries
import requests
from bs4 import BeautifulSoup as bsp
import pandas as pd

# Define the base URL for Internshala internships
url = 'https://internshala.com/internships/'

# Send a request to the URL and get the response
resp = requests.get(url, 'html.parser')
print(resp.status_code)  # Print the status code of the response

# Specify the field of interest (e.g., web development)
field = "web-development"
print(field)

# Create a modified URL for the specified field
modified_url = url + str(field) + '-internship/'
print(f"Status: {requests.get(modified_url)}")  # Print the status of the new request
print(modified_url)  # Print the modified URL

# Send a new request to the modified URL
resp_new = requests.get(modified_url)

# Parse the response content using BeautifulSoup
soup = bsp(resp_new.content, 'html.parser')

# Find the total number of pages available
pages = int(soup.find('span', id='total_pages').text)
print(pages)

# Generate a list of URLs for all pages
urlList = []
page = 1
while page <= pages:
    newUrl = modified_url + str(f"page-{page}/")
    urlList.append(newUrl)
    page += 1
print(urlList)  # Print the list of URLs

# Initialize a list to store the parsed content of each page
soup2 = []
for url in urlList:
    resp_new = requests.get(url)
    soup3 = bsp(resp_new.content, 'html.parser')
    soup2.append(soup3)
print(len(soup2))  # Print the number of pages parsed

# Initialize lists to store the internship details
name = []
for soup in soup2:
    names = soup.find_all('div', class_='individual_internship_header')
    for i in names:
        name.append(i)
print(len(name))  # Print the number of internship names found

# Extract and filter internship profiles
profile = []
for i in name:
    p = i.find('h3', class_='heading_4_5 profile')
    a = p.text.strip()
    profile.append(a)
print(f"All profiles available are: {profile}")

# Extract company names
company = []
for i in name:
    com = i.find('p').text.strip()
    company.append(com)
print(f"Companies are: {company}")

# Extract internship details
detail = []
for soup in soup2:
    detailList = soup.find_all('div', class_='individual_internship_internship')
    for i in detailList:
        detail.append(i)
print(len(detail))  # Print the number of internship details found

# Extract locations
location = []
for i in detail:
    loc = i.find('a').text
    location.append(loc)
print(f"Locations are: {location}")

# Extract durations of internships
duration_detail1 = []
for soup in soup2:
    duraList = soup.find_all('div', class_='item_body')
    for i in duraList:
        duration_detail1.append(i)
duration = []
i = 1
while i < len(duration_detail1):
    duration.append(duration_detail1[i].text.strip()[0])
    i += 3
print(f"Durations are: {duration}")

# Extract stipends
stipend = []
for soup in soup2:
    stipList = soup.find_all('span', class_='stipend')
    for i in stipList:
        val = i.text
        stipend.append(val)
print(f"Stipends are: {stipend}")

# Extract application links
cont = []
for soup in soup2:
    coutList = soup.find_all('div', class_='cta_container')
    for i in coutList:
        cont.append(i)

application_link = []
for i in cont:
    anc = i.find('a')
    link = anc.get('href')
    updated_link = 'https://internshala.com/' + link
    application_link.append(updated_link)
print(f"Application Links are: {application_link}")

# Create a DataFrame with the extracted data
dataTable = {
    'profile': profile,
    'company': company,
    'location': location,
    'stipend': stipend,
    'duration': duration,
    'application Link': application_link
}

df = pd.DataFrame(dataTable)
print(df.head())  # Print the first few rows of the DataFrame

# Save the DataFrame to a CSV file
df.to_csv('internshala_internships.csv', index=False)
print("DataFrame saved to 'internshala_internships.csv'")
