"""This is the script used to scrap corona virus numbers from worldometers website and then store them in the CSV format , using requests and BeautifulSoup library"""

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.worldometers.info/coronavirus/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

table = soup.find("table", {"id": "main_table_countries_today"})

rows = table.find_all("tr")

with open("corona_virus.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Country", "Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "Active Cases", "Serious Critical", "Total Cases/1M Population", "Deaths/1M Population", "Total Tests", "Tests/1M Population"])
    for row in rows:
        data = row.find_all("td")
        if data:
            country = data[0].text
            total_cases = data[1].text
            new_cases = data[2].text
            total_deaths = data[3].text
            new_deaths = data[4].text
            total_recovered = data[5].text
            active_cases = data[6].text
            serious_critical = data[7].text
            total_cases_per_1M_population = data[8].text
            deaths_per_1M_population = data[9].text
            total_tests = data[10].text
            tests_per_1M_population = data[11].text
            csv_writer.writerow([country, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases, serious_critical, total_cases_per_1M_population, deaths_per_1M_population, total_tests, tests_per_1M_population])
