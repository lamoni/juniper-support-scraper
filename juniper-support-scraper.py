import argparse, pycurl, os, re
from urllib import urlencode
from StringIO import StringIO
from urlparse import urlparse
from os.path import basename, splitext

# Argument definitions
def argsInit():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL to support.juniper.net file to download")
    parser.add_argument("username", help="Username to access support.juniper.net")
    parser.add_argument("password", help="Password to access support.juniper.net.  "
                                         "Passwords with special characters must be "
                                         "enclosed in single-quotes")

    return parser.parse_args()

# Clear the cookies.txt file before and after execution
def clearCookies():
    try:
        os.remove('cookie.txt')
    except OSError:
        pass

# Executes curl on a given url, sends POST data (if set)
def executeCurl(input_url, params={}, write_function=lambda x: None):
    c = pycurl.Curl()
    c.setopt(c.URL, input_url)
    c.setopt(c.FOLLOWLOCATION, True)
    c.setopt(c.HEADER, False)
    c.setopt(c.SSL_VERIFYPEER, False)
    c.setopt(c.COOKIEJAR, 'cookie.txt')
    c.setopt(c.COOKIEFILE, 'cookie.txt')

    if params:
        c.setopt(c.POSTFIELDS, urlencode(params))

    c.setopt(c.WRITEFUNCTION, write_function)
    c.perform()
    c.close()

# Downloads the file once we've got the direct link
def downloadFile(input_url, write_data):
    c = pycurl.Curl()
    c.setopt(c.URL, input_url)
    c.setopt(c.FOLLOWLOCATION, True)
    c.setopt(c.HEADER, False)
    c.setopt(c.SSL_VERIFYPEER, False)
    c.setopt(c.COOKIEJAR, 'cookie.txt')
    c.setopt(c.COOKIEFILE, 'cookie.txt')
    c.setopt(c.WRITEDATA, write_data)
    c.perform()
    c.close()

# Retrieves the record ID from the inputted url
def getRecordID(input_url):
    recordID = urlparse(input_url)
    recordID, file_ext = splitext(basename(recordID.path))
    return recordID

# Parses page output for actual link to file
def getDownloadLink(content):
    download_link = re.search(
        pattern='Your download should start in a few seconds. If not <a href="(.*)">Click to Download</a>',
        string=content
    ).group(1)
    return download_link

# Parses actual file's filename
def getFilename(input_url):
    return basename(urlparse(input_url).path)

# Main
args = argsInit()
storage = StringIO()
clearCookies()

# 1. Get initial page so our cookies get set
executeCurl(args.url)

# 2. Send login credentials
executeCurl(
    input_url="https://webdownload.juniper.net/access/oblix/apps/webgate/bin/webgate.so",
    params={
        'HiddenURI': '',
        'LOCALE': 'en_us',
        'AUTHMETHOD': 'UserPassword',
        'username': args.username,
        'password': args.password

    }
)

# 3. Get to EULA page and submit
executeCurl(
    input_url="https://webdownload.juniper.net/swdl/dl/download",
    params={
        'recordId': getRecordID(args.url),
        'siteId': '1',
        'eulaAccepted': 'Yes'
    },
    write_function=storage.write
)

# 4. Parse download URL from content
download_link = getDownloadLink(storage.getvalue())

# 5. Calculate filename
filename = getFilename(download_link)

print "Downloading..."
fp = open(filename, "wb")

#6 . Download the file
downloadFile(download_link, fp)

fp.close()

clearCookies()

print "Done"