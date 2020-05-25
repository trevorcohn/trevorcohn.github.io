#/bin/bash 

if [ ! -d /Volumes/mywebpages ]
then
    open 'smb://shares.eng.unimelb.edu.au/mywebpages'
fi

jekyll build --baseurl '/tcohn/'
#rsync -av ~/Website/_site/ /Volumes/mywebpages
rsync -av ./_site/ /Volumes/mywebpages
