import urllib.request as urllib


print("This is a site connectivity checker program.")
input_url = input("Input the url of the site: ")
    
def main(url):
    responce = urllib.urlopen(url)
    print("The response code is: ", responce.getcode())
    
main(input_url)