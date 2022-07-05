
tracks = ['FINANCE', 'GI', 'HEALTH', 'INVESTMENTALM', 'LIFE', 'RETIREMENT', 'RM']

from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

browser = Browser()
browser.visit('https://www.actuarialdirectory.org/SearchDirectory.aspx')
browser.select('dnn$ctr3472$DirectorySearch$ddlCountry', 'KENYA')
browser.select('dnn$ctr3472$DirectorySearch$ddlState', 'ID')
browser.select('dnn$ctr3472$DirectorySearch$ddlPrimaryAreaofPractice', 'HEALTH')
browser.find_by_name('dnn$ctr3472$DirectorySearch$btnSearch').click()
soup = BeautifulSoup(browser.html)

table = soup.find("table", {"id" : "dnn$ctr3472$DirectorySearch$dgSearchResult" })
print(table)


myData = pd.DataFrame(soup)
myData.to_csv("dat.csv")



#'dnn$ctr3472$DirectorySearch$tblSearchResult'

print(ans.value)





#soup = BeautifulSoup()





browser.quit()



