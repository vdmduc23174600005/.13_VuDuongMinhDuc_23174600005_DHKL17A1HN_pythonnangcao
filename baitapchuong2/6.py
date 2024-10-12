import requests
import xml.etree.ElementTree as ET
import csv

rss_url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
response = requests.get(rss_url)

xml_file = 'rss_feed.xml'
with open(xml_file, 'wb') as file:
    file.write(response.content)

tree = ET.parse(xml_file)
root = tree.getroot()

namespace = {'ns': 'http://purl.org/rss/1.0/'}

news_list = []

for item in root.findall('.//item'):
    news = {}
    news['title'] = item.find('title').text if item.find('title') is not None else 'N/A'
    news['link'] = item.find('link').text if item.find('link') is not None else 'N/A'
    news['description'] = item.find('description').text if item.find('description') is not None else 'N/A'
    news['pubDate'] = item.find('pubDate').text if item.find('pubDate') is not None else 'N/A'
    news_list.append(news)

csv_file = 'news_feed.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'link', 'description', 'pubDate'])
    writer.writeheader()
    writer.writerows(news_list)

print(f"Lưu {len(news_list)} tin tức vào file {csv_file}")

xml_file = 'rss_feed.xml'
with open(xml_file, 'wb') as file:
    file.write(response.content)

tree = ET.parse(xml_file)
root = tree.getroot()

namespace = {'ns': 'http://purl.org/rss/1.0/'}

news_list = []

for item in root.findall('.//item'):
    news = {}
    news['title'] = item.find('title').text if item.find('title') is not None else 'N/A'
    news['link'] = item.find('link').text if item.find('link') is not None else 'N/A'
    news['description'] = item.find('description').text if item.find('description') is not None else 'N/A'
    news['pubDate'] = item.find('pubDate').text if item.find('pubDate') is not None else 'N/A'
    news_list.append(news)

csv_file = 'news_feed.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'link', 'description', 'pubDate'])
    writer.writeheader()
    writer.writerows(news_list)

print(f"Lưu {len(news_list)} tin tức vào file {csv_file}")