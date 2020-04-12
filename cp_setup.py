'''
	Jay Prakash Mahto
	JVJplus	
	https://jvjplus.github.io/
'''

import sys 
try:
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')
	# sys.stderr = open('debug_log.txt', 'w')
except:
	pass

intinp = lambda : int(input()) 
def listinp(func= int): return list(map(func,input().split())) 
def nsepline(n,func=str): return [func(input()) for _ in range(n)]
def printlist(li,glue=' '): fop( glue.join(list(map(str,li))) )
# fast io
def fop(s): sys.stdout.write(str(s)+'\n')
def fip(): return sys.stdin.readline()
fintinp = lambda : int(fip()) 
def flistinp(func= int): return list(map(func,fip().split())) 
def fnsepline(n,func=str): return [func(fip()) for _ in range(n)]


PI=3.1415926535897932384626
MOD=1000000007



N=100005;
arr=[]

def run():
	n=fintinp()
	arr=flistinp()

	#start here
	


	

#######################################################

def main():
	t=1
	t=int(input())

	while(t>0):
		run()
		t=t-1


#calling main
main()