import os
import getpass
import subprocess



def main1(a):

	def menu(a):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			while True:			
				print("""	
				\n
				Press 1 : To run date
				Press 2 : To open calender
				Press 3 : To check IP
				Press 4 : To check Connectivity
				Press 5 : Create a file using gedit
				Press 6 : Create a file using vim editor
				Press 7 : Open firefox
				Press 8 : Open Python Interpreter
				Press 9 : To check particular command comes from which software 
				Press 10 : To check manual for particular command
				Press 11 : To read the packets coming
				Press 12 : To read the data in packets
				Press 13 : For Remote Login
				Press 14 : Go to main menu
				""")

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					subprocess.getoutput("date")
				elif int(ch)==2:
					subprocess.getoutput("cal")
				elif int(ch)==3:
					subprocess.getoutput("ifconfig enp0s3")
				elif int(ch)==4:
					subprocess.getoutput("ping -c 2 goo.gl")
				elif int(ch)==5:
					a=input("Enter file name : ")
					subprocess.getoutput("gedit {}".format(a))
				elif int(ch)==6:
					b=input("Enter file name : ")
					subprocess.getoutput("vim {}".format(a))
				elif int(ch)==7:
					subprocess.getoutput("firefox")
				elif int(ch)==8:
					subprocess.getoutput("python3")
				elif int(ch)==9:
					c=input("Enter command : ")
					subprocess.getoutput("yum whatprovides {}".format(c))
				elif int(ch)==10:
					d=input("Enter command : ")
					subprocess.getoutput("man {}".format(d))
					print("Press q to exit")
				elif int(ch)==11:
					subprocess.getoutput("tcpdump -i enp0s3 -n")
				elif int(ch)==12:
					subprocess.getoutput("tcpdump -i enp0s3 -n -X")
				elif int(ch)==13:
					e=input("Enter IP : ")
					subprocess.getoutput("ssh {}".format(e))
				elif int(ch)==14:
					break
				else: 
					print("Enter the valid choice")
				input("Press any key to continue...")
				subprocess.getoutput("clear")
				

	def remotemenu(b):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			while True:			
				print("""	
				\n
				Press 1 : To run date
				Press 2 : To open calender
				Press 3 : To check IP
				Press 4 : To check Connectivity
				Press 5 : Open Python Interpreter
				Press 6 : Go to main menu
				""")
				
				ip = input("Enter Remote IP : ")
				print(ip)
				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					subprocess.getoutput("ssh {} date".format(ip))
				elif int(ch)==2:
					subprocess.getoutput("ssh {} cal".format(ip))
				elif int(ch)==3:
					subprocess.getoutput("ssh {} ifconfig".format(ip))
				elif int(ch)==4:
					subprocess.getoutput("ssh {} ping -c 2 goo.gl".format(ip))
				elif int(ch)==5:
					subprocess.getoutput("ssh {} python3".format(ip))
				elif int(ch)==6:
					break
				else: 
					print("Enter the valid choice")
				input("Press any key to continue...")
				subprocess.getoutput("clear")	
		
	subprocess.getoutput("tput setaf 3")								
	print("\t\t\tBASIC LINUX COMMANDS!!")
	subprocess.getoutput("tput setaf 7")


	while True:
		print("\t\t---------------------------------------")
		print("""	
		\n
		PRESS 1 : RUN BASIC LINUX COMMANDS
		PRESS 2 : GO TO MAIN MENU
		""")

		a = input("Where you want to run your menu (local/remote) : ")
		print(a)

		if a=="local":
			ch = input("Enter your Choice : ") 
			print(ch)

			if int(ch)==1:
				menu(ch)
			else:
				break
			
		elif a=="remote":
			ch = input("Enter your Choice : ") 
			print(ch)

			if int(ch)==1:
				remotemenu(ch)
			else:
				break
		         
		else:
			exit()



def main2(b):
	def partition(a):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			
			while True:		
				print("""	
				\n
				Press 1 : to check details of Devices Attached(H.D.)
				Press 2 : to create physical partition
				Press 3 : to load the driver 
				Press 4 : to format the partition
				Press 5 : to mount to a folder
				Press 6 : to check it is successfully mounted or not
				Press 7 : to unmount folder/directory 
				Press 8 : to go back to main menu
				""")
		                
			

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					subprocess.getoutput("fdisk -l")
				elif int(ch)==2:
					a=input("Enter the device to make partition : ")
					subprocess.getoutput("fdisk {}".format(a))
				elif int(ch)==3:
					subprocess.getoutput("udevadm settle")
					print("\n")
					print("\t\t\tDriver loaded successfully")
				elif int(ch)==4:
					b=input("Enter the device/partition to format : ")
					subprocess.getoutput("mkfs.ext4 {}".format(b))
				elif int(ch)==5:
					c=input("Enter the device/partition : ")
					e=input("Create folder/directory to mount: ")
					d=input("Enter the folder created to mount : ")
					subprocess.getoutput("mkdir {}".format(e))
					subprocess.getoutput("mount {0} {1}".format(c,d))
				elif int(ch)==6:
					subprocess.getoutput("df -hT")
				elif int(ch)==7:
					f=input("Enter the folder to unmount : ")
					subprocess.getoutput("umount {}".format(f))
				elif int(ch)==8:
					break
				else: 
					print("Enter the valid choice")
					
				
			
	subprocess.getoutput("tput setaf 3")								
	print("\t\t\t  PARTITION CONCEPT!!")
	subprocess.getoutput("tput setaf 7")
	while True:
		print("\t\t---------------------------------------")
		print("""	
		\n
		PRESS 1 : CREATE PARTITION
		PRESS 2 : GO TO MAIN MENU
		""")

		ch = input("Enter your Choice : ") 
		print(ch)

		if int(ch)==1:
			partition(ch)
		else:
			break


def lvm(a):
	passwd=getpass.getpass("Enter your Password : ")
	actualpass="arth"
	if passwd!=actualpass:
		print("Incorrect Password...")
		exit()
	else:
		while True:
			print("""	
			\n
			Press 1 : to check devices attached
			Press 2 : to create physical volume
			Press 3 : to describe physical volume
			Press 4 : to create volume group
			Press 5 : to decribe volume group
			Press 6 : to create logical volume
			Press 7 : to describe logical volume
			Press 8 : to format the partition (with ext4 type)
			Press 9 : to mount/link the partition to a folder
			Press 10 : to check it is mountted successfully or not
			Press 11 : to unmount folder/directory 
			Press 12 : go back to main menu
			""")


			ch = input("Enter your Choice : ") 
			print(ch)

			if int(ch)==1:
				subprocess.getoutput("fdisk -l")
			elif int(ch)==2:
				a=input("Write your device names : ")
				subprocess.getoutput("pvcreate {}".format(a))
			elif int(ch)==3:
				x=input("Give your PV name : ")
				subprocess.getoutput("pvdisplay {}".format(x))
			elif int(ch)==4:
				b=input("Give Group name : ")
				c=input("Write your device names : ")
				subprocess.getoutput("vgcreate {0} {1}".format(b,c))
			elif int(ch)==5:
				d=input("Write Group name : ")
				subprocess.getoutput("vgdisplay {}".format(d))
			elif int(ch)==6:
				e=input("Give the size for logical volume : ")
				f=input("Give the name for your lv : ")
				g=input("Write the VG name from which you want to create LV :")
				subprocess.getoutput("lvcreate --size {0} --name {1} {2}".format(e,f,g))
			elif int(ch)==7:
				h=input("Give VG/LV name : ")
				subprocess.getoutput("lvdisplay {}".format(h))
			elif int(ch)==8:
				i=input("Provide device name to format : ")
				subprocess.getoutput("mkfs.ext4 {}".format(i))
				print("\t\t\tDevice formatted Successfully")
			elif int(ch)==9:
				j=input("Create folder/directory to mount: ")
				subprocess.getoutput("mkdir {}".format(j))
				k=input("Enter the device/partition : ")
				l=input("Enter created folder to mount on : ")
				subprocess.getoutput("mount {0} {1}".format(k,l))
				
			elif int(ch)==10:
				subprocess.getoutput("df -hT")
			elif int(ch)==11:
				f=input("Enter the folder to unmount : ")
				subprocess.getoutput("umount {}".format(f))
			elif int(ch)==12:
				break
			else: 
                            print("Enter a valid choice")
                            
				
def main3(c):
	def lvm1(b):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			while True:
				print("""	
				\n
				Press 1 : to see report of File System & disk
				Press 2 : Check available VG Size
				Press 3 : to extend logical volume
				Press 4 : to extend volume group
				Press 5 : to reduce logical volume
				Press 6 : go back to main menu
				""")

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					subprocess.getoutput("lsblk")
					print("\n")
					subprocess.getoutput("df -hT")
				elif int(ch)==2:
					a=input("Give VG name : ")
					subprocess.getoutput("vgdisplay {}".format(a))
				elif int(ch)==3:
					b=input("Give the size to extend (+size) : ")
					c=input("Give the device name : ")
					subprocess.getoutput("lvextend --size {0} {1}".format(b,c))
					print("After extending lv we have to format the extended part to use it")
					d=input("Enter device name : ")
					subprocess.getoutput("resize2fs {}".format(d))
				elif int(ch)==4:
					e=input("Give VG name to extend : ")
					f=input("Provide new Physical Volume : ")
					subprocess.getoutput("vgextend {0} {1}".format(e,f))
				elif int(ch)==5:
					print("Steps to follow")
					print("""	
					\n
					1 : unmount the mounted folder(offline)
					2 : Clean/Scan
					3 : format upto part you want to keep(online)
					4 : LV reduce
					5 : mount (online)
					""")
					g=input("1]Enter folder to unmount: ")
					subprocess.getoutput("umount {}".format(g))
					h=input("2]Enter device name to clean/scan : ")
					subprocess.getoutput("e2fsck -f {}".format(h))
					i=input("3]Enter device name to format(online) : ")
					j=input("Give the size upto you want to keep to format : ")
					subprocess.getoutput("resize2fs {0} {1}".format(i,j))
					k=input("4]Give the size to reduce : ")
					l=input("Give the device name : ")
					subprocess.getoutput("lvreduce --size {0} {1}".format(k,l))
					m=input("5]Enter device name to mount : ")
					n=input("Enter the folder/directory to mount on: ")
					subprocess.getoutput("mount {0} {1}".format(m,n))
				elif int(ch)==6:
					break					

				else: 
					print("Enter the valid choice")


	subprocess.getoutput("tput setaf 3")								
	print("\t\t-------LOGICAL VOLUME MANAGEMENT-------")
	subprocess.getoutput("tput setaf 7")
	while True:
		print("\t\t---------------------------------------")
		print("""	
		\n
		PRESS 1 : LVM PARTITION
		PRESS 2 : INCREASE OR DECREASE THE SIZE OF PARTITION
		PRESS 3 : GO TO MAIN MENU
		""")

		ch = input("Enter your Choice : ") 
		print(ch)

		if int(ch)==1:
			lvm(ch)
		elif int(ch)==2:
			lvm1(ch)
		else:
			break


def main4(d):
	def hadoop(a):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			while True:			
				print("""	
				\n
				Press 1 : To check the version of java & hadoop installed
				Press 2 : To install jdk
				Press 3 : To install hadoop
				Press 4 : Go to main menu
				""")

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					subprocess.getoutput("java -version")
					subprocess.getoutput("hadoop version")
				elif int(ch)==2:
					subprocess.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm")
				elif int(ch)==3:
					subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
				elif int(ch)==4:
					break
				else: 
					print("Enter the valid choice")

	def name(b):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			while True:			
				print("""	
				\n
				Press 1 : To Create directory
				Press 2 : To Edit hdfs-site.xml file
				Press 3 : To Edit core-site.xml file
				Press 4 : To format namenode
				Press 5 : To start namenode daemon service
				Press 6 : To check service started or not
				Press 7 : To check port number
				Press 8 : To see report
				Press 9 : To stop namenode daemon service
				Press 10 : To stop firewall
				Press 11 : Go to main menu
				""")

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					a=input("Give directory name : ")
					subprocess.getoutput("mkdir /{}".format(a))
				elif int(ch)==2:
					subprocess.getoutput("vim /etc/hadoop/hdfs-site.xml")
				elif int(ch)==3:
					subprocess.getoutput("vim /etc/hadoop/core-site.xml")
				elif int(ch)==4:
					subprocess.getoutput("hadoop namenode -format")
				elif int(ch)==5:
					subprocess.getoutput("hadoop-daemon.sh start namenode")
				elif int(ch)==6:
					subprocess.getoutput("jps")
				elif int(ch)==7:
					subprocess.getoutput("netstat -tnlp")
				elif int(ch)==8:
					subprocess.getoutput("hadoop dfsadmin -report")
				elif int(ch)==9:
					subprocess.getoutput("hadoop-daemon.sh stop namenode")
				elif int(ch)==10:
					subprocess.getoutput("systemctl stop firewall")
				elif int(ch)==11:
					break
				else: 
					print("Enter the valid choice")



	def data(b):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			while True:			
				print("""	
				\n
				Press 1 : To Create directory
				Press 2 : To Edit hdfs-site.xml file
				Press 3 : To Edit core-site.xml file
				Press 4 : To start datanode daemon service
				Press 5 : To check service started or not
				Press 6 : To check port number
				Press 7 : To see report
				Press 8 : To stop datanode daemon service
				Press 9 : To stop firewall
				Press 10 : Go to main menu
				""")

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					a=input("Give directory name : ")
					subprocess.getoutput("mkdir /{}".format(a))
				elif int(ch)==2:
					subprocess.getoutput("vim /etc/hadoop/hdfs-site.xml")
				elif int(ch)==3:
					subprocess.getoutput("vim /etc/hadoop/core-site.xml")
				elif int(ch)==4:
					subprocess.getoutput("hadoop-daemon.sh start datanode")
				elif int(ch)==5:
					subprocess.getoutput("jps")
				elif int(ch)==6:
					subprocess.getoutput("netstat -tnlp")
				elif int(ch)==7:
					subprocess.getoutput("hadoop dfsadmin -report")
				elif int(ch)==8:
					subprocess.getoutput("hadoop-daemon.sh stop datanode")
				elif int(ch)==9:
					subprocess.getoutput("systemctl stop firewall")
				elif int(ch)==10:
					break
				else: 
					print("Enter the valid choice")



	def client(c):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			while True:			
				print("""	
				\n
				Press 1 : To Edit core-site.xml file
				Press 2 : To check file storage of cluster
				Press 3 : To upload file 
				Press 4 : To read file
				Press 5 : To remove file
				Press 6 : To create a empty file
				Press 7 : Go to main menu
				""")

				ch = input("Enter your Choice : ") 
				print(ch)


				if int(ch)==1:
					subprocess.getoutput("vim /etc/hadoop/core-site.xml")
				elif int(ch)==2:
					subprocess.getoutput("hadoop fs -ls /")
				elif int(ch)==3:
					a=input("Enter file to upload : ")
					subprocess.getoutput("hadoop fs -put {} /".format(a))
				elif int(ch)==4:
					b=input("Enter file to read : ")
					subprocess.getoutput("hadoop fs -cat /{}".format(b))
				elif int(ch)==5:
					c=input("Enter file to remove : ")
					subprocess.getoutput("hadoop fs -rm /{}".format(c))
				elif int(ch)==6:
					c=input("Enter filename to create : ")
					subprocess.getoutput("hadoop fs -touchz /{}".format(c))
				elif int(ch)==7:
					break
				else: 
					print("Enter the valid choice")
					
		
	subprocess.getoutput("tput setaf 3")								
	print("\t\t\t  BIG DATA HADOOP!!")
	subprocess.getoutput("tput setaf 7")
	while True:
		print("\t\t---------------------------------------")
		print("""	
		\n
		PRESS 1 : HADOOP CONFIGURATION
		PRESS 2 : NAMENODE CONFIGURATION
		PRESS 3 : DATANODE CONFIGURATION
		PRESS 4 : CLIENT CONFIGURATION
		PRESS 5 : GO TO MAIN MENU
		""")

		ch = input("Enter your Choice : ") 
		print(ch)

		if int(ch)==1:
			hadoop(ch)
		elif int(ch)==2:
			name(ch)
		elif int(ch)==3:
			data(ch)
		elif int(ch)==4:
			client(ch)
		else:
			break

def main5(e):
	def config(a):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			while True:			
				print("""	
				\n
				Press 1 : To check docker-ce installed on our system or not 
				Press 2 : To intall docker-ce
				Press 3 : Start the service
				Press 4 : Check the status (active/inactive)
				Press 5 : Stop the service 
				Press 6 : To get docker information
				Press 7 : For help in docker
				Press 8 : Go to main menu
				""")

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					subprocess.getoutput("yum list docker-ce")			
				elif int(ch)==2:
					subprocess.getoutput("yum install docker-ce  --nobest")
				elif int(ch)==3:
					subprocess.getoutput("systemctl start docker")
				elif int(ch)==4:
					subprocess.getoutput("systemctl status docker")
				elif int(ch)==5:
					subprocess.getoutput("systemctl stop docker")
				elif int(ch)==6:
					subprocess.getoutput("docker info")
				elif int(ch)==7:
					subprocess.getoutput("docker --help")	
				elif int(ch)==8:
					break
				else: 
					print("Enter the valid choice")

	def operations(b):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			while True:			
				print("""	
				\n
				Press 1 : Show Docker Images
				Press 2 : To look for OS images to download from DockerHub
				Press 3 : Download/Pull docker image
				Press 4 : To check how many containers are running or stopped
				Press 5 : To Launch an new docker container
				Press 6 : To start existing Container
				Press 7 : To go inside a Container (attach)
				Press 8 : To stop existing Container
				Press 9 : To terminate all the OS(Container that exist)
				Press 10 : To see all existing container's id
				Press 11 : To remove container(OS)
				Press 12 : To remove docker image

				Press 13 : Go to main menu
				""")

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					subprocess.getoutput("docker images")

				elif int(ch)==2:
					a=input("Enter the OS image name to Search : ")
					subprocess.getoutput("docker search {}".format(a))
				elif int(ch)==3:
					b=input("Enter the OS image : ")			
					c=input("Enter the version : ")
					subprocess.getoutput("docker pull {0}:{1}".format(b,c))
				elif int(ch)==4:
					subprocess.getoutput("docker ps -a")
				elif int(ch)==5:
					e=input("Give a name to new container : ")			
					f=input("Enter image : ")
					g=input("Enter the version : ")
					subprocess.getoutput("docker run -it --name {0} {1}:{2}".format(e,f,g))
				elif int(ch)==6:
					h=input("Enter the OS name to start : ")
					subprocess.getoutput("docker start {}".format(h))	
				elif int(ch)==7:
					h=input("Enter the OS name to attach : ")
					subprocess.getoutput("docker attach {}".format(h))	
				elif int(ch)==8:
					h=input("Enter the OS name to stop : ")
					subprocess.getoutput("docker stop {}".format(h))
				elif int(ch)==9:
					subprocess.getoutput("docker rm `docker ps -a -q`")
				elif int(ch)==10:
					subprocess.getoutput("docker ps -a -q")	
				elif int(ch)==11:
					i=input("Enter the OS name to remove : ")
					subprocess.getoutput("docker rm -f {}".format(i))
				elif int(ch)==12:
					j=input("Enter the image name to remove : ")
					k=input("Enter the version : ")
					subprocess.getoutput("docker rmi -f {0}:{1}".format(j,k))	
				elif int(ch)==13:
					break
				else: 
					print("Enter the valid choice")

					
		
	subprocess.getoutput("tput setaf 3")								
	print("\t\t\tCONTAINERIZATION TECHNOLOGY!!")
	subprocess.getoutput("tput setaf 7")
	while True:
		print("\t\t---------------------------------------")
		print("""	
		\n
		PRESS 1 : DOCKER CONFIGURATION
		PRESS 2 : DOCKER OPERATIONS
		PRESS 3 : GO TO MAIN MENU
		""")

		ch = input("Enter your Choice : ") 
		print(ch)

		if int(ch)==1:
			config(ch)
		elif int(ch)==2:
			operations(ch)
		else:
			exit()
			break



def main6(f):
	def ansible(a):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			
			while True:		
				print("""	
				\n
				Press 1 : To Install ansible			
				Press 2 : To Check ansible version installed
				Press 3 : To See Inventories
				Press 4 : To ADD Inventories
				Press 5 : To ADD TN/MN to CN
				Press 6 : To check connectivity with TN/MN 
				Press 7 : Go to main menu
				""")
		                
			

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					subprocess.getoutput("pip3 install ansible")			
				elif int(ch)==2:
					subprocess.getoutput("ansible --version")
				elif int(ch)==3:
					subprocess.getoutput("ansible all --list-hosts")
				elif int(ch)==4:
					subprocess.getoutput("vim /etc/ansible/ansible.cfg")
				elif int(ch)==5:
					subprocess.getoutput("gedit /root/ip.txt")
				elif int(ch)==6:
					subprocess.getoutput("ansible all -m ping")
				elif int(ch)==7:
					break
				else: 
					print("Enter the valid choice")
					
			
	subprocess.getoutput("tput setaf 3")								
	print("\t\t\t     ANSIBLE!!")
	subprocess.getoutput("tput setaf 7")
	while True:
		print("\t\t------------------------------------")
		print("""	
		\n
		PRESS 1 : ANSIBLE CONFIGURATION
		PRESS 2 : GO TO MAIN MENU
		""")

		ch = input("Enter your Choice : ") 
		print(ch)

		if int(ch)==1:
			ansible(ch)
		else:
			break

def main7(g):
	def configure(a):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			
			while True:		
				print("""	
				\n
				Press 1 : To check aws-cli version installed
				Press 2 : To Authenticate/configure
				Press 3 : To get help
				Press 4 : Go to main menu
				""")
		                
			

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==1:
					subprocess.getoutput("aws --version")			
				elif int(ch)==2:
					subprocess.getoutput("aws configure")
				elif int(ch)==3:
					subprocess.getoutput("aws help")
				elif int(ch)==4:
					break
				else: 
					print("Enter the valid choice")
					

	def ec2(b):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			
			while True:		
				print("""	
				\n
				Press 0 : To get help in EC2 Instances
				Press 1 : Description of EC2 Instances
				Press 2 : Create a key-pair
				Press 3 : Description of key-pair
				Press 4 : To Launch an Amazon-Linux Instance on AWS Cloud
				Press 5 : Description of security groups
				Press 6 : Create Security Group
				Press 7 : Create Volume
				Press 8 : Attach Volume
				Press 9 : Go to main menu
				""")
		                
			

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==0:
					subprocess.getoutput("aws ec2 help")			
				elif int(ch)==1:
					i=input("Provide instance id : ")
					subprocess.getoutput("aws ec2 describe-instances --instance-ids   {}".format(i))
				elif int(ch)==2:
					a=input("Enter unique key name : ")
					subprocess.getoutput("aws ec2 create-key-pair --key-name  {}".format(a))
				elif int(ch)==3:
					k=input("Enter key name : ")
					subprocess.getoutput("aws ec2 describe-key-pairs --key-names {}".format(k))				
				elif int(ch)==4:
					l=input("Enter key name : ")
					m=input("How many instances you want : ")
					subprocess.getoutput("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name {} --count {}".format(l,m))
				elif int(ch)==5:
					p=input("Enter group id : ")
					subprocess.getoutput("aws ec2 describe-security-groups  --group-ids {}".format(k))
				elif int(ch)==6:
					n=input("Enter description : ")
					o=input("Enter group name : ")
					subprocess.getoutput("aws ec2 create-security-group --description {} --group-name {}".format(n,m))
				elif int(ch)==7:
					n=input("Provide availability zone : ")
					o=input("Enter Size : ")
					subprocess.getoutput("aws ec2 create-volume --availability-zone {} --volume-type gp2 --size {}".format(n,m))
				elif int(ch)==8:
					q=input("Enter instance id : ")
					r=input("Enter volume id : ")
					s=input("Enter device : ")
					subprocess.getoutput("aws ec2 attach-volume --instance-id {} --volume-id {} --device {}".format(q,r,s))
				elif int(ch)==9:
					break
				else: 
					print("Enter the valid choice")
			
	subprocess.getoutput("tput setaf 3")								
	print("\t\t  AWS-CLI AUTOMATION USING PYTHON!!")
	subprocess.getoutput("tput setaf 7")
	while True:
		print("\t\t------------------------------------")
		print("""	
		\n
		PRESS 1 : AWS-CLI AUTHENTICATION
		PRESS 2 : EC2 INSTANCES
		PRESS 3 : GO TO MAIN MENU
		""")

		ch = input("Enter your Choice : ") 
		print(ch)

		if int(ch)==1:
			configure(ch)
		elif int(ch)==2:
			ec2(ch)
		else:
			break

def main8(h):
	def server(a):
		passwd=getpass.getpass("Enter your Password : ")
		actualpass="arth"
		if passwd!=actualpass:
			print("Incorrect Password...")
			exit()
		else:
			
			while True:		
				print("""	
				\n
				Press 0 : To check httpd software installed or not
				Press 1 : To install httpd webserver
				Press 2 : Create a html file (webpages)
				Press 3 : Put your webpages to var/www/html/ directory
				Press 4 : Start the service
				Press 5 : Check the status (active/inactive)
				Press 6 : Stop the service 
				Press 7 : Go to main menu
				""")
		                
			

				ch = input("Enter your Choice : ") 
				print(ch)

				if int(ch)==0:
					subprocess.getoutput("yum list httpd")			
				elif int(ch)==1:
					subprocess.getoutput("yum install httpd")
				elif int(ch)==2:
					a=input("create html file : ")
					subprocess.getoutput("gedit {}".format(a))
				elif int(ch)==3:
					b=input("Enter the html file you have created : ")
					subprocess.getoutput("mv {} /var/www/html".format(b))
				elif int(ch)==4:
					subprocess.getoutput("systemctl start httpd")
				elif int(ch)==5:
					subprocess.getoutput("systemctl status httpd")
				elif int(ch)==6:
					subprocess.getoutput("systemctl stop httpd")
				elif int(ch)==7:
					break
				else: 
					print("Enter the valid choice")
					
			
	subprocess.getoutput("tput setaf 3")								
	print("\t\t CONFIGURE APACHE httpd WEBSERVER!!")
	subprocess.getoutput("tput setaf 7")
	while True:
		print("\t\t------------------------------------")
		print("""	
		\n
		PRESS 1 : CONFIGURE APACHE httpd WEBSERVER
		PRESS 2 : GO TO MAIN MENU
		""")

		ch = input("Enter your Choice : ") 
		print(ch)

		if int(ch)==1:
			server(ch)
		else:
			break


while True:
		subprocess.getoutput("tput setaf 3")		
		print("\n")						
		print("\t ===============WELCOME TO AUTOMATION WORLD!!===================")
		subprocess.getoutput("tput setaf 7")
		print("\t\t  ---------------------------------------")
		print("""	
		\n
		PRESS 1 : BASIC LINUX COMMANDS
		PRESS 2 : PARTITIONS
		PRESS 3 : LVM
		PRESS 4 : HADOOP
		PRESS 5 : DOCKER
		PRESS 6 : ANSIBLE
		PRESS 7 : AWS-CLI
		PRESS 8 : WEBSERVER
		PRESS 9 : EXIT
		""")
        
		ch = input("Enter your Choice : ") 
		print(ch)

		if int(ch)==1:
			main1(ch)
		elif int(ch)==2:
			main2(ch)
		elif int(ch)==3:
			main3(ch)
		elif int(ch)==4:
			main4(ch)
		elif int(ch)==5:
			main5(ch)
		elif int(ch)==6:
			main6(ch)
		elif int(ch)==7:
			main7(ch)
		elif int(ch)==8:
			main8(ch)
		elif int(ch)==9:
			exit()
		else:
			print("ENTER A VALID CHOICE")
