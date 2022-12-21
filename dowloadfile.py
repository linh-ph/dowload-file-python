import requests
import csv
arr = [
    "https://www.python.org/static/community_logos/python-logo.png"
]
with open('image.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        print('/')
        # return row
        # r = requests.get(", ".join(row))
        # print(r.content) 

# key = 1;
# for img in arr:
#     # URL of the image to be downloaded is defined as image_url
#     r = requests.get(img) # create HTTP response object
    
#     # send a HTTP request to the server and save
#     # the HTTP response in a response object called r
#     with open("img_"+str(key)+".png",'wb') as f:  
#         # write the contents of the response (r.content)
#         f.write(r.content)

#     key+=1
