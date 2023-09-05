import psutil
import time
import pyodbc

#In SQL Managment Studio you need create a new database called "System_information"

#We connect the code on the SQL Server Database 
con = pyodbc.connect('Driver={SQL Server};'
                     'Server=DESKTOP-970K9SD\SQLISTEA;'#In this line you need replace this information with your server, you can find it on propierties inside you sql managment studio
                     'Database=System_information;'
                     'Trusted_Connection=yes;')
cursor = con.cursor()

#Create a loop with sql querys for update the information of cpu
while 1==1:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()[2]
    cpu_interrupts = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]
    memory_used = psutil.virtual_memory()[3]
    memory_free = psutil.virtual_memory()[4]
    bytes_sent = psutil.net_io_counters()[0]
    bytes_recibe = psutil.net_io_counters()[1]
    disk_usage = psutil.disk_usage('/')[3]
    
    cursor.execute('insert into Performance values (GETDATE(),'
                   + str(cpu_usage) + ','
                   + str(memory_usage) + ','
                   + str(cpu_interrupts) + ','
                   + str(cpu_calls) + ','
                   + str(memory_used) + ','
                   + str(memory_free) + ','
                   + str(bytes_sent) + ','
                   + str(bytes_recibe) + ','
                   + str(disk_usage) + ')')
    con.commit() 
    