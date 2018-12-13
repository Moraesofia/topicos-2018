import urllib.request
import csv

count = 0
url = ""
with open('beautiful_animals.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        url = str(row)
        url = url.replace("['", "", 1)
        url = url.replace("']", "", 1)
        name = "anm" + str(count).zfill(3) + ".jpg"
        print("Downloading image " + url + " as " + name)
        urllib.request.urlretrieve(url, name)
        count += 1

print("The end")

