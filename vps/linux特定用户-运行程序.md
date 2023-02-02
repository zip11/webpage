默认情况下，root用户拥有系统最高权限，很多时候我们在linux部署应用程序时，程序可能需要取得某些系统权限才能正常运行，比如在所属组为root的目录里新建一个*.pid文件,普通用户是没有权限的，所以我们一般直接使用root用户来运行应用程序，这样就不用担心权限不足的问题，但是root用户账户下运行应用程序可能存在安全风险，所以这样的做法是不安全的。

很多服务启动需要root权限，但是服务启动后，root账户通常将其转移到服务账户，这里就是mysql账户，linux中的服务账户才是标准的用户账户，主要区别就是服务账户仅仅用来运行一个服务，该账户不需要拥有像登陆用户那样指定shell和类似/home/username的家目录，取而代之的是该用户的初始工作目录可能是应用程序安装目录。



----------


### 首先创建用户组 ###

    sudo addgroup --system test 


### 查看 刚创建的用户组 ###

    cat /etc/group

### 创建 用户 ###

    adduser --system --ingroup test --no-create-home --disabled-password test


创建了一个用户test，指定所属组为test，--system表示该用户是系统用户， --ingroup 指定所属组 --no-create-home 表示不为该用户创建家目录 --disabled-password 该用户不用来登录


----------


### 设置-用户的工作目录 ###

我们创建的用户用来运行我们的应用，所以需要指定该用户的工作目录为应用安装目录 /usr/local/MyApp

    usermod -c "这里是用户描述" -d /usr/local/MyApp -g test test

### 修改应用目录的所属组和用户 ###


    sudo chown -R test:test /usr/local/MyApp  
    # 应用安装目录所属组为test，所属用户为test
    
    sudo chmod u+rwx,g+rxs,o= /usr/local/MyApp  
    # 修改目录权限
    
