#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
import subprocess;

'''
print('$ nslookup www.python.org') ;
r = subprocess.call(['nslookup', 'www.python.org']);
print('exit code:', r);
'''

print('$ nslookup');
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
output, err = p.communicate(b'set q=mx\npython.org\nexit\n');
print(output.decode('utf-8'));
print('exit code', p.returncode);

