# Fluentd
>Nginx log to MySQL logs table.

## Getting Started
```bash
$ docker-compose up -d
```

## Access Web Server
Access to http://localhost:80 to generate log.

## Check MySQL Server
```bash
$ docker exec -it mysql bash
```

```bash
root@xxxx:/# mysql -umysql_user -pmysql_pass
mysql> select * from test_db.logs;
```
