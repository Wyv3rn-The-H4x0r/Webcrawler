########################
#   Osint-Webcrawler   #
#         by           #
#        Wyv3rn        #
#    Version 1.0.0     #
########################
import requests
from bs4 import BeautifulSoup
import wget
import time
import os
from multiprocessing import Process
# Start
links = []
crawled = []
forbidden_sites = ""
keyword = ""

# --------------------------  config --------------------------------------- #
CrawlerConf = []
print("[*] Loading Server Config")
try:
    CrawlerConfigFile = open("WebCrawler.chaos", "r")
    for line in CrawlerConfigFile:
        line = line.replace("\n", "")
        line = line.replace("targetSite=", "")
        line = line.replace("targetTime=", "")
        line = line.replace("delay=", "")
        line = line.replace("keyword=", "")
        if "forbiddenToCrawl=" in line:
            line = line.replace("forbiddenToCrawl=", "")
            fb = line.split(",")
            forbidden_sites = fb
        CrawlerConf.append(line)
except:
    print("[-] Something goes wrong by try\nto Load Config File")

keyword = CrawlerConf[4]
# -------------------------------------------------------------------------- #
# Set Target
links.append(CrawlerConf[0])
forbiddenToCrawl = CrawlerConf[3].split(",")
# data Save functions
def createFolder(targetlink:str):
    targetlink = targetlink.split('//')[1].split('/')[0]
    try:
        os.mkdir('CrawledRawData/' + targetlink)
    except:
        pass
    return 'CrawledRawData/' + targetlink

def saveRawData(targetsite, r, sitename):
    if keyword in r:
        with open(targetsite+ '/['+ sitename.replace("://", "").replace("www.", "").replace("/", "") + "].html", 'w+') as f:
            f.write(r)
        f.close()
    if keyword == "all":
        with open(targetsite+ '/['+ sitename.replace("://", "").replace("www.", "").replace("/", "") + "].html", 'w+') as f:
            f.write(r)
        f.close()

# Site Processing
def processSite(r):
    doc = BeautifulSoup(r.text, "html.parser")
    for a in doc.find_all("a", href=True):
        links.append(a['href'])

# Crawl Methods
def basecrawl():
    Deepness = 1
    DeepnessMax = 10
    for i in links:
        time.sleep(float(CrawlerConf[2]))
        if i in crawled or not i.startswith('http') or i in forbidden_sites:
            continue
        else:
            print("[*]" + "Depnesslevel arrived : " + str(Deepness) + " base start crawling: " + i)
            Deepness += 1
            targetfolder = createFolder(i)
            r = requests.get(i)
            crawled.append(i)
            processSite(r)
            saveRawData(targetfolder, r.text, i)
            if Deepness >= DeepnessMax:
                return

def crawl(linklist, id):
    for i in linklist:
        time.sleep(float(CrawlerConf[2]))
        if i in crawled or not i.startswith('http') or i in forbidden_sites:
            continue
        elif "pdf" in i and i not in crawled:
            newI = str(i.rsplit("/", 1))
            newI = newI.split(',')
            newI = newI[1].replace("'", "").replace("]", "").replace("[", "").replace(" ", "")
            exists = os.path.isfile('pdf/'+ newI)
            if exists:
                continue
            else:
                crawled.append(i)
                wget.download(i, out="pdf/")
        elif "txt" in i and i not in crawled:
            newI = str(i.rsplit("/", 1))
            newI = newI.split(',')
            newI = newI[1].replace("'", "").replace("]", "").replace("[", "").replace(" ", "")
            exists = os.path.isfile('txt/'+ newI)
            if exists:
                continue
            else:
                crawled.append(i)
                wget.download(i, out="txt/")

        elif "jpg" in i or "png" in i and i not in crawled:
            newI = str(i.rsplit("/", 1))
            newI = newI.split(',')
            newI = newI[1].replace("'", "").replace("]", "").replace("[", "").replace(" ", "")
            exists = os.path.isfile('img/'+ newI)
            if exists:
                continue
            else:
                crawled.append(i)
                wget.download(i, out="img/")

        else:
            print("[*]"+ str(id) +" start crawling: " + i )
            crawled.append(i)
            targetfolder = createFolder(i)
            r = requests.get(i)
            processSite(r)
            saveRawData(targetfolder, r.text, i)

def crawled_sites():
    try:
        with open("AlreadyCrawled.txt", "w+") as f:
            for line in crawled:
                if (len(line) < 100):
                    f.write(line)
            f.close()
    except Exception as err:
        print(err)

# Main Loop
crawlTime = 0
print("[*] CPU Core Count : " + str(os.cpu_count()))
threats = []


while True:
        print("[*]  ####################    Iteration " + str(crawlTime) + "    #######################")
        print("[*] Start Base Crawler")
        p = Process(target=basecrawl())
        p.start()
        print("[*] Split Crawled-List into split-1 to split-6")
        split1 = links[:len(links) // 2]
        split2 = links[len(links) // 2:]
        split3 = links[len(split1) // 2:]
        split4 = links[:len(split2) // 2]
        print("[*] Link-List Splittet\n")
        # Threats to Start
        print("[*] Start Subcrawler with ID : " + str(1))
        threats.append(Process(target=crawl, args=(split1, 0)))
        print("[*] Start Subcrawler with ID : " + str(2))
        threats.append(Process(target=crawl, args=(split2, 1)))
        print("[*] Start Subcrawler with ID : " + str(3))
        threats.append(Process(target=crawl, args=(split3, 2)))
        print("[*] Start Subcrawler with ID : " + str(4))
        threats.append(Process(target=crawl, args=(split4, 3)))
        print("[*]  ####################    Iteration " + str(crawlTime) + "    #######################")

        for process in threats:
                try:
                    process.start()
                except:
                    pass
        # Set Crawl Around Time
        crawlTime += 1
        if crawlTime >= int(CrawlerConf[1]):
            for process in threats:
                print("\nStart -> KILL Crawlers")
                for process in threats:
                    try:
                        print("Killed Crawler with PID : " + str(process.pid))
                        process.terminate()
                    except:
                        pass
                print("\n[*] Finished Crawling")
                exit(0)






