sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#cd /home/box/web/
sudo /etc/init.d/mysql start
mysql -uroot -e "create database web"
mysql -uroot -e "CREATE USER box@localhost IDENTIFIED BY 'user'"
mysql -uroot -e "GRANT ALL ON web.* TO box@localhost"
sudo gunicorn -w 1 -b 0.0.0.0:8000 ask.wsgi --pythonpath '/home/box/web/ask' --daemon &
#sudo gunicorn -w 1 -b 0.0.0.0:8000 ask.wsgi --pythonpath '/home/alezu/Рабочий\ стол/web/ask' --daemon &

