git clone https://github.com/seb-m/pyinotify.git
cd pyinotify/
python setup.py install
sudo nohup python /data/www/watch.py > /data/www/log.txt 2>&1 &
