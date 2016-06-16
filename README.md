# Juniper Support Scraper
This python script is used for downloading files (e.g. Junos Space Virtual Appliance, Service Now, Junos, etc...) from support.juniper.net

# Usage
1. Get link to software from support.juniper.net by going to page of software you want (e.g. https://www.juniper.net/support/downloads/?p=servicenow#sw), and copying the link of the desired software version (it will look like: https://webdownload.juniper.net/swdl/dl/secure/site/1/record/60879.html)

2. Execute script with:
```
python juniper-support-scraper.py https://webdownload.juniper.net/swdl/dl/secure/site/1/record/60879.html JUNIPER_USERNAME_HERE JUNIPER_PASSWORD_HERE
```

# Notes

 - If your username or password contain any special characters, enclose them in single-quotes, e.g.:
 ```
 python juniper-support-scraper.py https://webdownload.juniper.net/swdl/dl/secure/site/1/record/60879.html JUNIPER_USERNAME_HERE 'JUNIPER_PASSWORD_HERE!!!'
 ```
