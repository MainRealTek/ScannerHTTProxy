from protocol import get_scan
from sys import argv






def main(ip_list=str(),port=str(),out_file=str()):
    obj = get_scan(ip_list=ip_list,port=port,out_file=out_file)
    obj.main_scan()








if __name__ == '__main__':
    main(ip_list=argv[1],port=argv[2],out_file=argv[3])