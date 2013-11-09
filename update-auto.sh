# !/bin/sh 

# Description: Update POS Software automatic

git fetch

EXIT_CODE=`git diff origin/master --exit-code`

#======================================
#
#Functions
#
#======================================

function UpdateSoftware () {
	echo "Updating Data"
	git merge origin/master
	sudo sh install.sh
	sudo service pos-printer restart
}

# $? Exit code of git diff. exit code == 0 if no different

if [[ $? ]]; then
	UpdateSoftware
fi