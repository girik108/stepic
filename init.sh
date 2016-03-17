sudo apt-get update && sudo apt-get install mc python-mysqldb python3-dev libmysqlclient-dev -y
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn stop

sudo pip3 install django==1.8
sudo pip3 install gunicorn
sudo pip3 install mysqlclient

#sudo gunicorn -c etc/dj.py ask.wsgi:application --chdir /home/box/web/ask/

sudo service mysql start

mysql -u root -e "CREATE USER 'django'@'localhost' IDENTIFIED BY '11111111';"
mysqladmin create qabase -u root 
mysql -u root -e "GRANT ALL PRIVILEGES ON qabase.* TO django"
mysqladmin flush-privileges -u root 

ask/manage.py makemigrations qa
ask/manage.py migrate

#gunicorn3 -c etc/dj.py ask.wsgi:application --chdir /home/box/web/ask/