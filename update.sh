# !/bin/sh 

# Description: Update POS Software automatic

echo "Begin Update `date`"
BASEPATH=$(dirname $0)
cd $BASEPATH

git fetch
DIFF_FILE_COUNT=`git diff --name-status master..origin/master |wc -l`


#======================================
#
#Functions
#
#======================================

# function UpdateSoftware () {
# }

# $DIFF_FILE_COUNT Exit code of git diff. exit code == 0 if no different
echo $DIFF_FILE_COUNT

if [ $DIFF_FILE_COUNT -gt 0 ]; then
	sudo service pos-printer stop
  sudo pkill python

	# UpdateSoftware
	echo "Updating $DIFF_FILE_COUNT Files "
	git merge origin/master
	sudo sh install.sh

  # sudo ps -ef | grep keyboard-input.py | grep -v grep | awk '{print $2}'|sudo xargs kill -9 
	sleep 10
	sudo service pos-printer start
else
	echo "Already last version!"
fi

echo "End Update `date`"