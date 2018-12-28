from optparse import OptionParser  
  
parser = OptionParser(usage="usage:%prog [options] arg1 arg2")  
parser.add_option("-t", "--timeout",  
                action = "store",  
                type = 'int',  
                dest = "timeout",  
                default = None,  
                help="Specify annalysis execution time limit"  
                )  
parser.add_option("-u", "--url",  
                action = "store_true",  
                dest = "url",  
                default = False,  
                help = "Specify if the target is an URL"  
                )
(options, args) = parser.parse_args() 
if options.url:  
    print(args[0])

