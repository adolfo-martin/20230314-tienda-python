FROM mariadb:10.7.8-focal
MAINTAINER adolfo.martin@iesramonarcas.es
ENV MARIADB_ROOT_PASSWORD Hola1234
ADD ./tienda.sql /docker-entrypoint-initdb.d
EXPOSE 3306

# docker build -t mariadb_tienda:1.0 .
# docker run -d --name mariadb_tienda --publish 3306:3306 mariadb_tienda:1.0
# docker exec -it mariadb_tienda mariadb -u root -p tienda