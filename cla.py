import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"h:i:o:a:b:c:d:e:f:g:j:k:l:m:n:p:q:r:s:t:u:v:w:x:y:",["ifile=","ofile=","rfile="])
   except getopt.GetoptError:
      print 'Correct Formatting: test.py -i <inputfile> -o <outputfile>'
      print 'Error:'
      a = getopt.GetoptError
      print a
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      else:
         badarg = 'bad'
         print "The variable " + opt + " (" + arg + ") is not defined."
         break
   try:
      badarg
   except UnboundLocalError:
      print 'Input file is "', inputfile
      print 'Output file is "', outputfile
   else:

      print ''

if __name__ == "__main__":
   main(sys.argv[1:])