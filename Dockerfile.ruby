FROM ruby:latest

RUN bundle config --global frozen 1

WORKDIR /var/www/php-py
COPY Gemfile Gemfile.lock ./
RUN bundle install