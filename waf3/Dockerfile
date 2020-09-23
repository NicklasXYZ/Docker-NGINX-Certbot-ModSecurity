From waf3_dep:latest
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
	apk del wget \
		tar \
		git \
		pkgconf \
		autoconf \
		automake

COPY nginx.conf /usr/local/nginx/conf/nginx.conf
COPY modsec_includes.conf /usr/local/nginx/conf/modsec_includes.conf
COPY modsecurity.conf /usr/local/nginx/conf/modsecurity.conf
COPY crs-setup.conf /usr/local/nginx/conf/crs-setup.conf

