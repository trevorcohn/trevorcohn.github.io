#/bin/bash 

if [ ! -d /Volumes/mywebpages ]
then
    open 'smb://silo-hq1.eng.unimelb.edu.au/mywebpages'
    #echo "Use finder to mount smb://silo-hq1.eng.unimelb.edu.au/mywebpages"
    #exit 1
fi

jekyll build --baseurl 'tcohn' --url 'https://people.eng.unimelb.edu.au/tcohn'
#rsync -av ~/Website/_site/ /Volumes/mywebpages
rsync -av ./_site/ /Volumes/mywebpages
