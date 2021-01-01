import threading 
from threading import*
import time

dic={} #'dic' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,ttl_value)" ttl is optional 
#you can continue by passing two arguments without ttl

def create(key,value,ttl=0):
    if key in dic:
        print("Error : This key already exists") # Error message 1
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and JSON object value less than 16KB 
                if ttl==0:
                    l=[value,ttl]
                else:
                    l=[value,time.time()+ttl]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dic[key]=l
            else:
                print("Error : Memory limit exceeded!! ")# Error message 2
        else:
            print("Error: Invalid key-name! Key-name must contain only alphabets and no special characters or numbers")# Error message 3 

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in dic:
        print("Error : given key does not exist in database. Please enter a valid key") # Error message 4
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JSON Object i.e.,"key_name:value"
                return stri
            else:
                print("Error : Time-To-Live of ",key," has expired") # Error message 5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in dic:
        print("Error: given key does not exist in database. Please enter a valid key") # Error message 4
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del dic[key]
                print("Key is successfully deleted")
            else:
                print("Error: Time-To-Live of ",key," has expired") # Error message 5
        else:
            del dic[key]
            print("Key is successfully deleted")