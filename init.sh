sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
sudo gunicorn3 -c etc/dj.py ask.wsgi:application --chdir /home/box/web/ask/

sudo service mysql start
mysql -uroot -e "CREATE USER 'django' IDENTIFIED BY '11111111';"
mysql -uroot -e "CREATE DATABASE 'qa'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON 'qa'.* TO 'django';"
mysql -uroot -e "FLUSH PRIVILEGES;"