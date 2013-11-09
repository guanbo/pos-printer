# !/bin/sh 

# Description: Update POS Software automatic

git fetch

DIFF_FILE_COUNT=`git diff --name-status master..origin/master |wc -l`

#======================================
#
#Functions
#
#======================================

function UpdateSoftware () {
	echo "Updating Data"
	git merge origin/master
	# sudo sh install.sh
	# sudo service pos-printer restart
}

# $? Exit code of git diff. exit code == 0 if no different

if [[ $DIFF_FILE_COUNT ]]; then
	UpdateSoftware
fi