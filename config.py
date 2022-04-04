import yaml  
from yaml.loader import FullLoader  
  

#open yaml file in read  
with open('/home/kanhaiya/Desktop/yaml_test/new_config.yaml', 'rb') as file:  
    config_new = yaml.load(file, Loader=FullLoader)  


    #open yaml file in read  
with open('/home/kanhaiya/Desktop/yaml_test/config_old.yaml', 'rb') as f:  
    config_old = yaml.load(f, Loader=FullLoader)  
