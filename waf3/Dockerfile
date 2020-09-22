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
	
	
	

# Use the Ubuntu 20.04 Long Term Support (LTS) release as the base image 
# FROM ubuntu:18.04
# FROM ubuntu:20.04
From waf3_dep:latest

# ENV TZ=Europe/Copenhagen
# # FROM ubuntu:18.04
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
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
RUN	cd / && \
	git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git && \
	wget http://nginx.org/download/nginx-1.18.0.tar.gz && \
	tar zxvf nginx-1.18.0.tar.gz && \
	cd nginx-1.18.0 && \
	./configure --prefix=/usr/local/nginx \
				--sbin-path=/sbin/nginx \
				--modules-path=/modules \
				--user=root \
				--group=root \
				--with-debug \
				--add-module=/ModSecurity-nginx \
				--with-http_ssl_module \
				--with-compat \
				--without-http_access_module \
				--without-http_auth_basic_module \
				--without-http_autoindex_module \
				--without-http_empty_gif_module \
				--without-http_fastcgi_module \
				--without-http_referer_module \
				--without-http_memcached_module \
				--without-http_scgi_module \
				--without-http_split_clients_module \
				--without-http_ssi_module \
				--without-http_uwsgi_module && \
	make && \
	make install && \
	make clean && \
	cd / && \
	git clone https://github.com/SpiderLabs/owasp-modsecurity-crs.git /usr/src/owasp-modsecurity-crs && \
	cp -R /usr/src/owasp-modsecurity-crs/rules/ /usr/local/nginx/conf/  && \
	mv /usr/local/nginx/conf/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example  /usr/local/nginx/conf/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf && \
	mv /usr/local/nginx/conf/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example  /usr/local/nginx/conf/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf && \
	apk del alpine-sdk \
		wget \
		tar \
		git \
		pkgconf \
		autoconf \
		automake
	# apk del alpine-sdk \
	# 	wget \
	# 	tar \
	# 	git \
	# 	autoconf \
	# 	automake \
	# 	curl-dev \
	# 	lmdb-dev \
	# 	pcre-dev \
	# 	libtool \
	# 	libxml2-dev \
	# 	openssl-dev \
	# 	yajl-dev \
	# 	pkgconf \
	# 	geoip-dev \
	# 	linux-headers \
	# 	zlib-dev
# Error loading shared library libpcre.so.1: No such file or directory (needed by /sbin/nginx)
# Error loading shared library libcurl.so.4: No such file or directory (needed by /usr/local/modsecurity/lib/libmodsecurity.so.3)
# Error loading shared library libGeoIP.so.1: No such file or directory (needed by /usr/local/modsecurity/lib/libmodsecurity.so.3)
# Error loading shared library libxml2.so.2: No such file or directory (needed by /usr/local/modsecurity/lib/libmodsecurity.so.3)
# Error loading shared library libpcre.so.1: No such file or directory (needed by /usr/local/modsecurity/lib/libmodsecurity.so.3)
# Error loading shared library libyajl.so.2: No such file or directory (needed by /usr/local/modsecurity/lib/libmodsecurity.so.3)
# Error loading shared library libstdc++.so.6: No such file or directory (needed by /usr/local/modsecurity/lib/libmodsecurity.so.3)
# Error loading shared library libgcc_s.so.1: No such file or directory (needed by /usr/local/modsecurity/lib/libmodsecurity.so.3)

	# apt-get remove -y --purge apt-utils autoconf automake build-essential git pkgconf && \
	# apt-get autoremove -y


# COPY nginx.conf /usr/local/nginx/nginx.conf
COPY modsec_includes.conf /usr/local/nginx/modsec_includes.conf
COPY modsecurity.conf /usr/local/nginx/modsecurity.conf
COPY crs-setup.conf /usr/local/nginx/crs-setup.conf
# CMD sleep 100000
CMD nginx -g "daemon off;"
# EXPOSE 80
	
	
	
	