
alj="/home/pi/Alist"
agz="alist-linux-arm-7.tar.gz"

mkdir $alj

#unzip

tar -zxvf $agz

chmod +x alist

# move file

mv alist $alj

mv $agz $alj

mv install-alist.sh $alj