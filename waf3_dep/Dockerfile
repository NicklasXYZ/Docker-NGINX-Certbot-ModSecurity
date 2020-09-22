# # Use the Ubuntu 20.04 Long Term Support (LTS) release as the base image 
# FROM ubuntu:20.04
# # Install dependencies and build nginx with ModSecurity
# RUN apt-get update && \
# 	apt-get install -y wget tar apt-utils autoconf automake build-essential git libcurl4-openssl-dev libgeoip-dev liblmdb-dev libpcre++-dev libtool libxml2-dev libssl-dev libyajl-dev pkgconf zlib1g-dev && \
# 	git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity && \
# 	cd ModSecurity && \
# 	git submodule init && \
# 	git submodule update && \
# 	./build.sh && \
# 	./configure && \
# 	make && \
# 	make install && \
# 	cd / && \
# 	git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git && \
# 	wget http://nginx.org/download/nginx-1.18.0.tar.gz && \
# 	tar zxvf nginx-1.18.0.tar.gz && \
# 	cd nginx-1.18.0 && \
# 	./configure  --user=root --group=root --with-debug --with-ipv6 --with-http_ssl_module --with-compat --add-module=/ModSecurity-nginx --without-http_access_module --without-http_auth_basic_module --without-http_autoindex_module --without-http_empty_gif_module --without-http_fastcgi_module --without-http_referer_module --without-http_memcached_module --without-http_scgi_module --without-http_split_clients_module --without-http_ssi_module --without-http_uwsgi_module && \
# 	make && \
# 	make install && \
# 	cd / && \
# 	git clone https://github.com/SpiderLabs/owasp-modsecurity-crs.git /usr/src/owasp-modsecurity-crs && \
# 	cp -R /usr/src/owasp-modsecurity-crs/rules/ /usr/local/nginx/conf/  && \
# 	mv /usr/local/nginx/conf/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example  /usr/local/nginx/conf/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf && \
# 	mv /usr/local/nginx/conf/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example  /usr/local/nginx/conf/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf && \
# 	apt-get remove -y --purge apt-utils autoconf automake build-essential git pkgconf && \
# 	apt-get autoremove -y

# COPY nginx.conf /usr/local/nginx/nginx.conf
# COPY modsec_includes.conf /usr/local/nginx/modsec_includes.conf
# COPY modsecurity.conf /usr/local/nginx/modsecurity.conf
# COPY crs-setup.conf /usr/local/nginx/crs-setup.conf
# CMD sleep 10000
# # CMD nginx -g "daemon off;"
# EXPOSE 80








################ OLD START
	
# # Use the Ubuntu 20.04 Long Term Support (LTS) release as the base image 
# FROM ubuntu:20.04

# ENV TZ=Europe/Copenhagen
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# # Install dependencies and build nginx with ModSecurity (https://github.com/SpiderLabs/ModSecurity)
# # RUN apt-get update && \
# # 	apt-get install -y wget tar apt-utils autoconf automake build-essential git libcurl4-openssl-dev libgeoip-dev liblmdb-dev libpcre++-dev libtool libxml2-dev libssl-dev libyajl-dev pkgconf zlib1g-dev && \
# # 	git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity && \
# # 	cd ModSecurity && \
# # 	git submodule init && \
# # 	git submodule update && \
# # 	./build.sh && \
# # 	./configure && \
# # 	make && \
# # 	make install && \
# # 	make clean

# RUN apt-get update && \
# 	apt-get install -y \
# 		wget \
# 		tar \
# 		apt-utils \
# 		autoconf \
# 		automake \
# 		build-essential \
# 		git \
# 		libcurl4-openssl-dev \
# 		liblmdb-dev \
# 		libpcre++-dev \
# 		libtool \
# 		libxml2-dev \
# 		libssl-dev \
# 		libyajl-dev \
# 		pkgconf \
# 		libgeoip-dev \
# 		zlib1g-dev && \
# 	git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity && \
# 	cd ModSecurity && \
# 	git submodule init && \
# 	git submodule update && \
# 	./build.sh && \
# 	./configure && \
# 	make && \
# 	make install && \
# 	make clean && \
# 	apt-get autoremove -y

################ OLD END








# 	&& \
# 	cd / && \
# 	git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git && \
# 	wget http://nginx.org/download/nginx-1.18.0.tar.gz && \
# 	tar zxvf nginx-1.18.0.tar.gz && \
# 	cd nginx-1.18.0 && \
# 	./configure --prefix=/usr/local/nginx \
# 				--sbin-path=/sbin/nginx \
# 				--modules-path=/modules \
# 				--user=root \
# 				--group=root \
# 				--with-debug \
# 				--add-module=/ModSecurity-nginx \
# 				--with-http_ssl_module \
# 				--with-compat \
# 				--without-http_access_module \
# 				--without-http_auth_basic_module \
# 				--without-http_autoindex_module \
# 				--without-http_empty_gif_module \
# 				--without-http_fastcgi_module \
# 				--without-http_referer_module \
# 				--without-http_memcached_module \
# 				--without-http_scgi_module \
# 				--without-http_split_clients_module \
# 				--without-http_ssi_module \
# 				--without-http_uwsgi_module && \
# 	make && \
# 	make install && \
# 	cd / && \
# 	git clone https://github.com/SpiderLabs/owasp-modsecurity-crs.git /usr/src/owasp-modsecurity-crs && \
# 	cp -R /usr/src/owasp-modsecurity-crs/rules/ /usr/local/nginx/conf/  && \
# 	mv /usr/local/nginx/conf/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example  /usr/local/nginx/conf/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf && \
# 	mv /usr/local/nginx/conf/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example  /usr/local/nginx/conf/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf && \
# 	apt-get remove -y --purge apt-utils autoconf automake build-essential git pkgconf && \
# 	apt-get autoremove -y
# COPY nginx.conf /usr/local/nginx/nginx.conf
# COPY modsec_includes.conf /usr/local/nginx/modsec_includes.conf
# COPY modsecurity.conf /usr/local/nginx/modsecurity.conf
# COPY crs-setup.conf /usr/local/nginx/crs-setup.conf
# CMD sleep 100000
# # CMD nginx -g "daemon off;"
# EXPOSE 80
	
	
	
	


# Use the Ubuntu 20.04 Long Term Support (LTS) release as the base image 
# FROM ubuntu:20.04


# ENV TZ=Europe/Copenhagen
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install dependencies and build nginx with ModSecurity (https://github.com/SpiderLabs/ModSecurity)
# RUN apt-get update && \
# 	apt-get install -y wget tar apt-utils autoconf automake build-essential git libcurl4-openssl-dev libgeoip-dev liblmdb-dev libpcre++-dev libtool libxml2-dev libssl-dev libyajl-dev pkgconf zlib1g-dev && \
# 	git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity && \
# 	cd ModSecurity && \
# 	git submodule init && \
# 	git submodule update && \
# 	./build.sh && \
# 	./configure && \
# 	make && \
# 	make install && \
# 	make clean

################ NEW

FROM alpine:3.12.0

RUN apk update && \
		apk add alpine-sdk \
		bash \
		wget \
		tar \
		git \
		autoconf \
		automake \
		curl-dev \
		lmdb-dev \
		pcre-dev \
		libtool \
		libxml2-dev \
		openssl-dev \
		yajl-dev \
		pkgconf \
		geoip-dev \
		linux-headers \
		zlib-dev && \
	git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity && \
	cd ModSecurity && \
	git submodule init && \
	git submodule update && \
	./build.sh && \
	./configure && \
	make && \
	make install && \
	make clean


# https://cornercase.info/setup-nginx-alpine-docker-container-modsecurity-redis/



# FROM alpine:latest

# RUN rm -rf /var/cache/apk/* \
#     && rm -rf /tmp/*

# RUN cat /etc/apk/repositories

# RUN apk add --update gcc \
#                      libc-dev \
#                      linux-headers \
#                      zlib-dev \
#                      openrc \
#                      autoconf \
#                      automake \
#                      git \
#                      libressl-dev \
#                      geoip-dev \
#                      lmdb-dev \
#                      pcre-dev \
#                      libtool \
#                      libxml2-dev \
#                      yajl-dev \
#                      pkgconf \
#                      wget \
#                      zlib-dev \
#                      g++ \
#                      libcurl \
#                      make \
#                      redis


# # Mod_Security Setup
# RUN git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity
# WORKDIR /ModSecurity
# RUN git submodule init \
#     && git submodule update \
#     && ./build.sh \
#     && ./configure \
#     && make \
#     && make install \
#     && make clean

# WORKDIR /
# RUN git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git \
#     && wget http://nginx.org/download/nginx-1.17.0.tar.gz \
#     && tar zxvf nginx-1.17.0.tar.gz

# WORKDIR /nginx-1.17.0
# RUN  ./configure --with-compat --with-http_ssl_module \
#     && make \
#     && make install \
#     && make clean \
#     && mkdir /etc/nginx \
#     && mkdir /etc/nginx/modules/ \
#     && mkdir /usr/local/nginx/modules/ \
#     && mkdir /var/log/nginx

# RUN ./configure --with-compat --with-http_ssl_module --add-dynamic-module=../ModSecurity-nginx \
#     && make \
#     && make modules \
#     && ls -la /etc/nginx \
#     && cp /nginx-1.17.0/objs/ngx_http_modsecurity_module.so /usr/local/nginx/modules/ngx_http_modsecurity_module.so \
#     && make clean

# WORKDIR /
# RUN mkdir /etc/nginx/modsec \
#     && echo "load_module modules/ngx_http_modsecurity_module.so;" >> /etc/nginx/nginx.conf \
#     && cp /usr/local/nginx/conf/mime.types /etc/nginx/

# ADD nginx_config/modsecurity.conf /etc/nginx/modsec/modsecurity.conf
# ADD nginx_config/modsec.main.conf  /etc/nginx/modsec/main.conf

# # Nginx Config
# ADD nginx_config/my_webapp_nginx.conf /etc/nginx/conf.d/
# ADD nginx_config/nginx.conf /etc/nginx/nginx.conf

# # Install productlisting_framework Libraries
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /run/nginx
# RUN mkdir /my_webapp

# ADD start-nginx-server.sh /my_webapp/

# RUN chmod 777 /my_webapp/start-nginx-server.sh

# EXPOSE 8000
# RUN adduser -D nginx
# ENTRYPOINT /my_webapp/start-nginx-server.sh




# RUN apt-get update && \
# 	apt-get install -y \
# 		wget \
# 		tar \
# 		apt-utils \
# 		autoconf \
# 		automake \
# 		build-essential \
# 		git \
# 		libcurl4-openssl-dev \
# 		liblmdb-dev \
# 		libpcre++-dev \
# 		libtool \
# 		libxml2-dev \
# 		libssl-dev \
# 		libyajl-dev \
# 		pkgconf \
# 		libgeoip-dev \
# 		zlib1g-dev && \
# 	git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity && \
# 	cd ModSecurity && \
# 	git submodule init && \
# 	git submodule update && \
# 	./build.sh && \
# 	./configure && \
# 	make && \
# 	make install && \
# 	make clean && \
# 	apt-get autoremove -y

################ NEW