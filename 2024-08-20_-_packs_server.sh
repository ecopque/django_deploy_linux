# ssh gnulinuxdebian@34.28.163.241 #1:
# sudo apt update -y
# sudo apt upgrade -y
# sudo apt autoremove -y
# sudo apt install build-essential -y #2:
# sudo add-apt-repository ppa:deadsnakes/ppa #3:
# sudo apt install python3.11 python3.11-venv
# sudo apt install nginx -y #4:
# sudo apt install certbot python3-certbot-nginx -y #5:
# sudo apt install postgresql postgresql-contrib -y #6:
# sudo apt install libpq-dev -y #7:
# sudo apt install git -y #8:
# git config --global user.name 'Edson Copque'
# git config --global user.email 'ecop@disroot.org'
# git config --global init.defaultBranch main
# mkdir ~/schedulerepo ~/scheduleapp
# cd ~/schedulerepo
# git init --bare #9:
# cd ..
# cd ~/scheduleapp
# git init
# git remote add schedulerepo ~/schedulerepo #10:
# git add .
# git commit -m 'Initial'
# git push schedulerepo main -u # erro
# No diretório my_project: git remote add schedulerepo gnulinuxdebian@34.28.000.000:~/schedulerepo (parece que tenho que fazer no diretório do my_project). #11:
# No diretório my_project: git push schedulerepo main. #12:
# No servidor gnulinuxdebian@djangodeploy na pasta ~/scheduleapp: git pull schedulerepo main. #13:
