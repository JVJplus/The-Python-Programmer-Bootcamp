try:
	import sys 
	sys.stdin = open('input.txt', 'r') 
# 	sys.stdout = open('output.txt', 'w')
	# sys.stderr = open('debug_log.txt', 'w')
except:
	pass

'''
	notes

n=input()
arr=list(map(int,input().split()))
print(arr,end='')
'''

N=123

def run():
	n=int(input())
	arr=list(map(int,input().split()))

	#start here
	print(arr)



#######################################################

def main():
	t=1
	t=int(input())

	while(t>0):
		run()
		t=t-1


#calling main
main()