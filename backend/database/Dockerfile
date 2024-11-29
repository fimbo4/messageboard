FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=messageboard

COPY ./message_board_db.sql /docker-entrypoint-initdb.d/

EXPOSE 1300