#Wordpress with Ansible.

##1. Các thành phần.

- Source wordpress lưu tại `/var/www`
- Apache2.
- Mysql.
- php5


###a. Cài đặt apache2.

- apt-get install -y apache2.
- Chỉnh lại file `etc/apache2/sites-available/000-default-conf` như sau:

```sh
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/wordpress

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet

```

###b. Cài đặt PHP.

- install php5

###c. Cài đặt mysql-server.

###d. Tải và setup wordpress:

- tải file tại : `wget http://wordpress.org/latest.tar.gz`
- Coppy sang thư mục `/var/www`
- Giải nén.


**Playbook apache**

```sh
---

#!bin/ansible-playbook
- name : cai dat apache 
  hosts: wordpress
  sudo: true
  tasks:
	 - name: install apache
	   apt: name=apache2 update_cache=yes state=present
     - name: config file
       lineinfile:
		dest=/etc/apache2/sites-available/000-default.conf
	    regexp="(.)+DocumentRoot /var/www/html"
	    line="DocumentRoot /var/www/wordpress"
     - name: restart apache
       service: name=apache2 state=restarted
	 - name: install php5
	   apt: name={{item}} update_cache=yes state=present
 	   with_items:
		php5
		libapache2-mod-php5
		php5-mcrypt
	 - name: install mysql
	   apt: name=mysql-server
	 #- mysql_user_home: /root
	 #- mysql_root_username: root
	 #- mysql_root_password: root
	 #- mysql_ root_password_update: no
	 #- mysql_enable_on_startup: yes
```