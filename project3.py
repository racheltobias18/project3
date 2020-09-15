import urllib.request
urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log','serverlogs.txt')

file = open("serverlogs.txt", "r")
last_year = 0
total_requests = 0

new_year = "remote - - [01/Jan/1995:00:31:54 -0700]"

for aline in file:
    line = aline.strip()
    words = line.split
    total_requests += 1
    
    if new_year in line:
        start = total_requests + 1
        
    total_requests += 1
file.close()
last_year = total_requests - start

print("The number of requests in the last year is", last_year, "and the total number of requests in the log timeframe is", total_requests)
