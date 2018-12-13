import urllib.request
import csv

count = 0
url = ""
with open('beautiful-buildings-512-url.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        url = str(row)
        url = url.replace("['", "", 1)
        url = url.replace("']", "", 1)
        name = "b" + str(count).zfill(4) + ".jpg"
        print("Downloading image " + url + " as " + name)
        urllib.request.urlretrieve(url, name)
        count += 1

print("The end")

