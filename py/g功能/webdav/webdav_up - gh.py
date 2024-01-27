from webdav4.client import Client

# username 为坚果云账号，password 为刚刚创建的密码
client = Client(base_url='https://dav.jianguoyun.com/dav/',
                auth=('admin', 'passwd'))

lsl = client.ls(path='/', detail=False)
print(lsl)

upl = client.upload_file(from_path='file.txt', to_path='/demo/file.txt', overwrite=True)
print(upl)