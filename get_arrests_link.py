##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################




def arrests_urls(sub_pages_url):
    """Returns all the arrest links URLs extentions for the 
    according website."""
    
    import urllib2,sys
    import pandas as pd
    from bs4 import BeautifulSoup

    #Base Page
    soup = BeautifulSoup(urllib2.urlopen(sub_pages_url).read())
	
    #Speech URLs
    #content = soup.find("tr", {"td":"a"})
    content = soup.find("tr")
    print content
    speeches = ["".join(x.findAll("a")) for x in content.findAll(href=True)]
    
    #base_url = "http://www.whitehouse.gov"

    try:
        f=open('arresturls.txt', 'w')
        for link in content.findAll('a', href=True):
            url = link['href']
            arrest_url = url
            f.write(u'%s\n' % (arrest_url))
    finally:
        f.close()



	#Write to CSV
	data = pd.read_csv("arresturls.txt", index_col=0, delimiter='|')
	data.to_csv("__arrest_urls.csv", encoding='utf-8', header=False)



#arrests_urls("http://stpeteforpeace.org/occupyarrests.sources.html")


import urllib

import urllib2

attempts = 0

url = "http://seattletimes.nwsource.com/html/localnews/2017613231_occupy28m.html"

while attempts < 3:
    try:
        response = urllib2.urlopen(url, timeout = 5)
        content = response.read()
        f = open( "local/example.html", 'w' )
        f.write( content )
        f.close()
        break
    except urllib2.URLError as e:
        attempts += 1
        print type(e)






