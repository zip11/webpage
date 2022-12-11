## python将原生cookie转换为字典dict格式 ##

    def cookietodict(b):
    
	    cookie ={}
	    
	    for line in b.split(';'):
	    
		    key, value = line.split('=', 1)
		    cookie[key] = value
	    
	    #print(cookie)
	    return cookie
    
    b1 = '__gads=ID=2bc94af25696a743:T=1618288095:S=ALNI_MaHTWlgywNGGe-g_7lRS3BdLUIWzA; __yadk_uid=4YChvgeANLBEh4iV00n1tc0HQ8zpmSl1'

    c1=cookietodict(b1)
    
    print(c1)