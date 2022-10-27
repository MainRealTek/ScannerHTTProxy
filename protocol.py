from urllib2 import ProxyHandler,build_opener,install_opener,Request,urlopen
from colorama import Fore,Style
from threading import Thread
from sys import exit






class get_scan(Thread,object):
    def __init__(self,ip_list=str(),port=str(),out_file=str()):
        self.ip_list        = ip_list
        self.port           = port
        self.out_file       = out_file

        self.C_found        = 0
        self.C_error        = 0
        self.C_not_response = 0

    def read(self):
        returnx = []
        ii = open(self.ip_list,'r')
        lines = ii.readlines()
        for i in lines:
            line = i.rstrip('\n\r')
            returnx.append(line)

        return returnx


    def write(self,line):
        ii = open(self.out_file,'a')
        ii.write(line)
        ii.write('\n')
        ii.close()

    def p_green(self,val,iport):
        print(Fore.GREEN+Style.BRIGHT+'['+val+']FOUND['+val+'] ---> '+iport+Fore.RESET+Style.RESET_ALL)

    def p_red(self,val,iport):
        print(Fore.RED+Style.BRIGHT+'['+val+']ERROR['+val+'] ---> '+iport+Fore.RESET+Style.RESET_ALL)

    def p_yellow(self,val,iport):
        print(Fore.YELLOW+Style.BRIGHT+'['+val+']TIMEOUT['+val+'] ---> '+iport+Fore.RESET+Style.RESET_ALL)


    def main_scan(self):

        listx = self.read()

        for ip_check in listx:
            try:
                proxy_handler = ProxyHandler({'http':str(ip_check)+str(self.port)})
                opener = build_opener(proxy_handler)
                install_opener(opener)
                req = Request("http://www.google.com")
                try:
                    sock=urlopen(req, timeout= 7)
                    rs = sock.read(1000)
                    if '<title>Google</title>' in rs:
                        self.C_found+=1
                        self.p_green(str(self.C_found),str(ip_check)+':'+str(self.port))
                        self.write(ip_check)
                    else:
                        self.C_error+=1
                        self.p_red(str(self.C_error),str(ip_check)+':'+str(self.port))
                except Exception:
                    self.C_not_response+=1
                    self.p_yellow(str(self.C_not_response),str(ip_check)+':'+str(self.port))
            except Exception as i:
                print(i)
                print('OKK')





