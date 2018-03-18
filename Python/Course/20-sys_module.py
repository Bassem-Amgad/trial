import sys
sys.stderr.write('this is stderr\n')
sys.stderr.flush()
sys.stdout.write('this is stdout\n')
'''
allow you to pass arguments through to Python from the command line. 
acts as a bridge to the ability to communicate between Python and other language 
'''
print(sys.argv)
if len(sys.argv) >1:
    print(sys.argv[1])
'''
open command line in this folder
write--> python 20-sys_module.py "hi there"
output is -->
this is stderr
this is stdout
['0-sys_module.py' ,'hi there']
hi there
'''
# another way to do it
def main(arg):
    print(arg)

main(sys.argv[1])

### actually it will give error in idle as sys.argv[1] is out of range 
