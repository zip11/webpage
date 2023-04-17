# cf_dns_api #

## cf dns 更新api ##

官方api例子

[https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-update-dns-record](https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-update-dns-record)


今年第一篇贴一个通过Cloudflare API更新DNS记录的脚本

过程基于OpenWRT系统，需要先安装curl和jsonfilter

先在Profile->api-tokens中申请一个API Token，权限需要Zone->Zone以及Zone->DNS的Edit权限

得到的token作为变量cftoken

需要知道zone的ID，可以在域名Overview中看到,作为变量zoneid

需要DDNS的域名作为变量record_name

以下是更新A记录的脚本

update_dns.sh


    #!/bin/sh
    wanip_v4=`curl -s -k https://ip.cn | jsonfilter -e "$.ip"`
    record_name='abc.example.com'
    zoneid='cd7d0123e3012345da9420df9514dad0'
    cftoken='YQSn-xWAQiiEh9qM58wZNnyQS7FUdoqGIUAbrh7T'
    zoneinfo=`curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zoneid/dns_records?name=$record_name&type=A" \
     -H "Authorization: Bearer $cftoken" \
     -H "Content-Type:application/json"`
    
    recordid=`jsonfilter -s $zoneinfo -e '$.result[0].id'`
    
    result_cf=`curl -s -X PUT "https://api.cloudflare.com/client/v4/zones/$zoneid/dns_records/$recordid" \
     -H "Authorization: Bearer $cftoken" \
     -H "Content-Type: application/json" \
     --data "{\"type\":\"A\",\"name\":\"$record_name\",\"content\": \"$wanip_v4\", \"ttl\":1,\"proxied\":false}"`
    echo $result_cf