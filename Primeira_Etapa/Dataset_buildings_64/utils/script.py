import urllib.request
import csv

count = 0
url = ""
with open('beautiful_buildings.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        url = str(row)
        url = url.replace("['", "", 1)
        url = url.replace("']", "", 1)
        nome = "buildings" + str(count).zfill(3) + ".jpg"
        print("Downloading image " + url + " as " + nome)
        urllib.request.urlretrieve(url, nome)
        count += 1

print("The end")

