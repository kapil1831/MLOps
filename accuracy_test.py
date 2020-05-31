import os

accuracy=open('/root/jenkins_job1_data/accuracy.txt','r').read()
if float(accuracy) >= 0.85:
    os.system('curl --user "admin:redhat" http://192.168.43.207:8082/job/job4/build?token=job4')
else:
    os.system('curl --user "admin:redhat" http://192.168.43.207:8082/job/job2/build?token=job2')