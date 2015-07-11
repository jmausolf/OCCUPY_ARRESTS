##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


python get_arrests_link.py

mkdir Arrest_Stories
cp __arrest_urls.csv Arrest_Stories/
cd Arrest_Stories

wget -i __arrest_urls.csv 


for f in *; do mv "$f" "$f.html"; done
for f in *.html.html; do mv "$f" "${f%.html}"; done

mv __arrest_urls.csv.html __arrest_urls.csv

