##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################



def arrests_urls(input_url):
    """Returns all the arrest links URLs extentions for the 
    according website."""
    
    import urllib2,sys
    import pandas as pd
    from bs4 import BeautifulSoup

    #Base Page
    soup = BeautifulSoup(urllib2.urlopen(input_url).read())
	
    content = soup.find("tr")
    speeches = ["".join(x.findAll("a")) for x in content.findAll(href=True)]

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



arrests_urls("http://stpeteforpeace.org/occupyarrests.sources.html")



