import sys

def fizzbuzz(N):

	NUMBERS = range(1,N+1)
        i = 1


	for i in NUMBERS:
        	if (i%2 == 0):
                	if (i%3 == 0):
                        	print "fizzbuzz"
			else:
				print "fizz"
        	elif (i%3 == 0):
                	print "buzz"
	        else:
        	        print i
		i = i+1

if __name__ == '__main__':
	N = int(sys.argv[1])
        fizzbuzz(N)
