import sys,getopt
def main(argv):
    key=''
    string=''
    try:
        opts,args=getopt.getopt(argv,"hk:s:",["key=","str="])
    except getopt.GetoptError:
        print("caser.py -k <key> -s <str>")
        print("caser.py -h (get help~)")
        sys.exit()
    for opt,arg in opts:
        if opt in ("-h"):
            print("caser.py -k <ket> -S <str>")
            sys.exit()
        elif opt in ("-k","--key"):
            key=arg
        elif opt in ("-s","--str"):
            string=arg
    print("hello:"+string+"  "+key)
if __name__ == "__main__":
    main(sys.argv[1:])

            
