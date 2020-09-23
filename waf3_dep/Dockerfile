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