set /P "wj=input *.go name"

go build %wj%

echo "build %wj% ok" 

pause