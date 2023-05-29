

    curl -X GET "https://api.cloudflare.com/client/v4/zones/023e105f4ecef8ad9ca31a8372d0c353/dns_records?type=A&name=example.com&content=127.0.0.1&page=1&per_page=20&order=type&direction=desc&match=all" \
	     -H "X-Auth-Email: user@example.com" \
	     -H "X-Auth-Key: c2547eb745079dac9320b638f5e225cf483cc5cfdda41" \
	     -H "Content-Type: application/json"