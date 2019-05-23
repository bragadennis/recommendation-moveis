#to be included into /etc/nginx/conf.d/ file

upstream my_http_servers {
    server 127.0.0.1:444;
    server 127.0.0.1:445;
    server 127.0.0.1:446;
    server 127.0.0.1:447;
}
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;
    location / {
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   Host      $http_host;
        proxy_pass         http://my_http_servers;
    }
}