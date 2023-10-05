# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:28:16 2023

"""

#import libraries
import requests
from bs4 import BeautifulSoup
import re

#open output file
outFile = open("out.txt", "w")

#iterate through pages
for i in range(1,100):
    print(i)
    try:
        #get 
        req = requests.get('https://hatebase.org/search_results/page=' + str(i))
        
        #retain relevant part of code
        req = str(req.content).split("<!-- PAGE CONTENT BEGINS -->")[1]
        req = req.split("<!-- PAGE CONTENT ENDS -->")[0]
    
        #parse HTML code 
        soup = BeautifulSoup(req, "html.parser")
        href = soup.find_all("a", href=True)
        
        #identify hatewords in HTML code
        for ref in href:
           j = re.split("/", str(ref))
           if j[1] == "vocabulary":
                k = j[2].split("\\")
                hateword = k[0].replace("039", "'") #ascii encoding
               
                if any(char.isdigit() for char in hateword) == False:   #eliminate integer containing strings
                    #write to file
                    outFile.write(hateword + "\n")
    except:
        pass

outFile.close()