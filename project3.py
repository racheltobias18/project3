import urllib.request
urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log','serverlogs.txt')

file = open("serverlogs.txt", "r")
total_requests = 0

for aline in file:
    line = aline.strip()
    words = line.split
    total_requests += 1
file.close()

print("The number of requests is", total_requests)
