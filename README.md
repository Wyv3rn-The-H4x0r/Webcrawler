# Webcrawler

[EN]
Easy to Use :
First :
Install the required Libs

-> python3 -m pip install requirements.txt

Second :
Setup the Config file (show below)

Last but not least:
starte den crawler mit
->  Python3 Crawler.py

Then have fun and Disc Space :3

The Config
The Start, from here we begin to Crawl
targetSite=https://example.com

How deep we want to Crawl
targetTime=100

request delay (if Crawler trigger the  DDOS Protection  (recommed 0.5 -> 1 Sek)
delay=0.0

sites we dont want to crawl (why?  because it take time or has not what we want)
forbiddenToCrawl=youtube,instagram,facebook

it will only sites saved where has the keyword in it
Actually we can only use ONE keyword (wait for an update or doit yourself :P
if you want to crawl ALL just change the entry to -> keyword=all
but beware ! it will need allooott of space
keyword=service

[DE]
Einfach zu nutzen

Erstens :
Installier die benötigten Bibliotheken

-> python3 -m pip install requirements

Zweitens :
den stelle die Config ein (siehe unten)

Drittens:
starte den crawler mit
->  Python3 Crawler.py

und dan hab geduld und speicherplatz :3

Die Konfiguration
Der Startpunkt von wo aus Daten gesammelt werden
targetSite=https://example.com

Wieviele seiten Gesammelt werden auf basis des Starts (tiefe)
targetTime=100

Anfrage verzögerung (falls Crawler die DDOS Protection auslöst (empfohlen 0.5 -> 1 Sek)
delay=0.0

Seiten die vom crawlen ausgeschlossen werden (weil lange dauert?)
forbiddenToCrawl=youtube,instagram,facebook

Es werden nur seiten gespeichert die dieses Schlüsselwort inne haben (z.b nen vorname)
Aktuell geht nur 1 Wort
Wenn du einfach ALLES sammeln willst änder den wert auf ->  keyword=all
keyword=service
