#!/usr/bin/env python

import requests
import threading
import sys 
import re
import urllib.parse as up
class Enumeration:
    '''enumeration class to perform subdomain and directory enumeration'''
    def __init__(self, target_url):
        self.target_url = target_url
        self.target_links = []

    def request(self, url):
        try:
            return requests.get('http://' + url)
        
        except requests.exceptions.ConnectionError:
            pass

    def subdomain_enumeration(self):
        '''discovering website subdomain'''
        with open("subdomains-wodlist.txt", "r") as wordlist_file:
            for line in wordlist_file:
                test_url = line.strip() + '.' + self.target_url
                response = self.request(test_url)
                if response:
                    with open("subdomains", "a") as sub_file:
                        sub_file.write("[+] Discovered Subdomain --> " + test_url + "\n")
                    #print("[+] Discovered Subdomain --> "+ test_url)


    def directory_enumeration(self):
        '''discovering hidden paths in website like directories'''
        with open("files-and-dirs-wordlist.txt", "r") as wordlist_file:
            for line in wordlist_file:
                test_url = self.target_url + "/" + line.strip()
                response = self.request(test_url)
                if response:
                    with open("directories", "a") as sub_file:
                        sub_file.write("[+] Discovered Directory --> " + test_url + "\n")
                    #print("[+] Discovered Directory -->" + test_url)


    def spider(self):
        '''to extract useful data from response we'll use regex'''
        response = requests.get('http://' + self.target_url)
        content = response.content.decode('utf-8')
        href_links = re.findall('(?:href=")(.*?)"', content) #extraction complete
        for link in href_links:
            '''some urls are incomplete, to make them complete 
            we can use the library called urllib'''
            link = up.urljoin(self.target_url, link)
            #for unique links that comes with a '#' and prevent the repeatitiveness of the links 
            if "#" in link:
                link = link.split("#")[0]
            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                #print(link)
                with open("spider", "a") as sp:
                    sp.write("[+] Extracted Unique link --> " + link + "\n")
                self.spider()
                

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 web_crawler.py example.com")
        exit(1)
    e = Enumeration(sys.argv[1])
    #multithreading
    thread1 = threading.Thread(target=e.subdomain_enumeration)
    thread2 = threading.Thread(target=e.directory_enumeration)
    thread3 = threading.Thread(target=e.spider)
    #starting the thread
    thread1.start()
    thread2.start()
    thread3.start()
    #joining the thread so that the program continues
    thread1.join()
    thread2.join()
    thread3.join()
    print("[+] Enumeration completed successfully")
    
if __name__ == main():
    main()
