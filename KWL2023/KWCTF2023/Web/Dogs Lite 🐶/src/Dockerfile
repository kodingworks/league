FROM php:alpine

WORKDIR /app

COPY . .

RUN docker-php-ext-install \
  pdo && \
  docker-php-ext-enable pdo

EXPOSE 1337

CMD php -S 0.0.0.0:1337
