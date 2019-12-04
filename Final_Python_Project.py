# Importing beautiful soup module
import requests
import bs4
res = requests.get("""https://eservices.minnstate.edu/registration/search/advancedSubmit.html?campusid=305&searchrcid
=0305&searchcampusid=305&yrtr=20205&subject=ITEC&courseNumber=&courseId=&openValue=OPEN_PLUS_WAITLIST&delivery=ALL&
showAdvanced=&starttime=&endtime=&mntransfer=&credittype=ALL&credits=&instructor=&keyword=&begindate=&site=&
resultNumber=250
""")
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
print(noStarchSoup)
