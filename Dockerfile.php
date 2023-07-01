# Dockerfile.php
FROM php:8.1-fpm

WORKDIR /var/www/php-py

# Install PHPUnit
RUN curl --location --output /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar \
    && chmod +x /usr/local/bin/phpunit

COPY . .