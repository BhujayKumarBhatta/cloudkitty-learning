from cloudkitty.api import app

application = app.build_wsgi_app(argv=[])

#from pecan.deploy import deploy
#application = deploy('/var/www/simpleapp/config.py')

# apt install libapache2-mod-wsgi
#(pecan-env) bhujay@ubuntu:~/eclipse-workspace/cloudkitty-learning/cloudkitty$ sudo vi /etc/apache2/sites-enabled/mysite.conf

#<VirtualHost h1>
#    ServerName h1


#    WSGIDaemonProcess simpleapp  threads=5 python-path=/home/bhujay/pecan-env/lib/python2.7/site-packages
#    WSGIScriptAlias / /home/bhujay/eclipse-workspace/cloudkitty-learning/cloudkitty/cloudkitty/api/app.wsgi

#    <Directory /home/bhujay/eclipse-workspace/cloudkitty-learning/cloudkitty/cloudkitty>
#        WSGIProcessGroup simpleapp
#        WSGIApplicationGroup %{GLOBAL}
#        AllowOverride all
#        Order allow,deny
#        Allow from all
#        Require all granted
#    </Directory>
#</VirtualHost>






