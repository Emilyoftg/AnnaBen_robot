if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Emilyoftg/EVA-3.0.git /Update
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Update
fi
cd /EVA-3.0
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
