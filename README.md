# Juniper Support Scraper
This python script/module is used for downloading files (e.g. Junos Space Virtual Appliance, Service Now, Junos, etc...) from support.juniper.net

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

 - If you try to copy and paste a record link and it is just a link to the current page, click the link so the alert box pops up, and then copy the link from "If you understand this alert and are still certain, you may Continue to Download..."

# Ideas
 - Catalogue the record IDs of the more popular Juniper software, assign names to them, and allow devs to pull based on name rather than the long-winded record ID URL (.e.g. instead of https://webdownload.juniper.net/swdl/dl/secure/site/1/record/60879.html, we could reference it as "Service_Now_15.1R3")
