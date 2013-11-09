# !/bin/sh 

# Description: Update POS Software automatic

BASEPATH=$(dirname $0)
cd $BASEPATH

git fetch

DIFF_FILE_COUNT=`git diff --name-status master..origin/master |wc -l`

#======================================
#
#Functions
#
#======================================

function UpdateSoftware () {
	echo "Updating $DIFF_FILE_COUNT Files "
	git merge origin/master
	sudo sh install.sh
	sudo ps -ef | grep keyboard-input.py | grep -v grep | awk '{print $2}'|sudo xargs kill -9 
	sleep 3
	sudo service pos-printer stop
	sudo service pos-printer start
}

# $? Exit code of git diff. exit code == 0 if no different

if [ $DIFF_FILE_COUNT -gt 0 ]; then
	UpdateSoftware
else
	echo "Already last version!"
fi