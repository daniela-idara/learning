# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
import urllib.request

def main():
    weburl = urllib.request.urlopen("http://www.dropbox.com")
    print("result code:", weburl.getcode()) ## return code know if it the request was reachable
    data = weburl.read()    ## Adding the read the code for the webpage is viewed. 
    print(data)             ## the print result displays the code
if __name__ == "__main__":
    main()
