import yaml
with open(r'C:/Users/Kunal/Downloads/DataSet/Milestone1/Milestone1A.yaml') as file:
    user_list = yaml.load(file, Loader=yaml.FullLoader)
    print(user_list)