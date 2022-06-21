import json
import argparse
from json import JSONEncoder

class ServiceAccount: 
    def __init__(self,number,project):
        self.active = True
        self.description = ''
        self.number = number
        self.type = ''
        self.project = project

    def show(self):
        print(f'ServiceAccount - number: {self.number} project: {self.project} active: {self.active}')

    def disable(self):
        self.active = False

    def enable(self):
        self.active = True

class ServiceAccountList: 
    def __init__(self):
        self.service_accounts = []

    def serviceAccounttoJson(self,js):
        sa = ServiceAccount(js['number'],js['project'])
        sa.active = js['active']
        return sa

    def fromJson(self,json):
        self.service_accounts = [self.serviceAccounttoJson(elem) for elem in json]

    def get(self,project):
        get_free = [sa for sa in self.service_accounts if sa.project == project]
        number = 0
        if len(get_free) > 0: 
            number = max([sa.number for sa in get_free]) + 1
        sa = ServiceAccount(number,project)
        self.service_accounts.append(sa)
        return sa
    
    def delete(self, number, project):
        sa = [sa for sa in self.service_accounts if sa.project == project and sa.number == number]
        if len(sa) > 0:
            self.service_accounts.remove(sa[0])
            return sa[0]

    def disable(self, number, project): 
        for sa in self.service_accounts: 
            if sa.number == number and sa.project == project: 
                sa.disable()
                return sa
    
    def enable(self, number, project): 
        for sa in self.service_accounts: 
            if sa.number == number and sa.project == project: 
                sa.enable()
                return sa

    def list(self):
        [sa.show() for sa in self.service_accounts]

class ServiceAccountEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
        
def read(path): 
    f = open(path)
    d = json.load(f)
    f.close()
    return d

def write(path,obj): 
    with open(path, "w") as outfile:
        outfile.write(obj)

def test_case():
    sa_list = ServiceAccountList()
    sa_list.get('Test')
    sa_list.get('Test')
    sa_list.get('Test2')
    js = json.dumps(sa_list, indent=4, cls=ServiceAccountEncoder)
    print(js)
    write('sa.json',js)

parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("get",nargs='?', help="Get service account, next number avaliable for project")
parser.add_argument("list",nargs='?', help="List all service accounts")
parser.add_argument("-p", "--project", type=str, help="Project number")
parser.add_argument("delete", nargs='?', type=int, help="Delete service account, with number")
parser.add_argument("disable", nargs='?', help="Disable service account")
parser.add_argument("-n", '--number', type=int, help="Number service account")
parser.add_argument("enable", nargs='?', help="Enable service account")
args = parser.parse_args()

config = vars(args)

if config['project'] and config['get'] == 'get': 
    obj = read('sa.json')
    sa = ServiceAccountList()
    sa.fromJson(obj['service_accounts'])
    new = sa.get(config['project'])
    new.show()
    js = json.dumps(sa, indent=4, cls=ServiceAccountEncoder)
    write('sa.json',js)

if config['project'] and config['delete']:
    obj = read('sa.json')
    sa = ServiceAccountList()
    sa.fromJson(obj['service_accounts'])
    delete = sa.delete(config['delete'],config['project'])
    delete.show()
    js = json.dumps(sa, indent=4, cls=ServiceAccountEncoder)
    write('sa.json',js)

if config['get'] == 'list': 
    obj = read('sa.json')
    sa = ServiceAccountList()
    sa.fromJson(obj['service_accounts'])
    sa.list()

if config['get'] == 'disable' and config['project'] and config['number']:
    obj = read('sa.json')
    sa = ServiceAccountList()
    sa.fromJson(obj['service_accounts'])
    disable = sa.disable(config['number'],config['project'])
    disable.show()
    js = json.dumps(sa, indent=4, cls=ServiceAccountEncoder)
    write('sa.json',js)

if config['get'] == 'enable' and config['project'] and config['number']:
    obj = read('sa.json')
    sa = ServiceAccountList()
    sa.fromJson(obj['service_accounts'])
    disable = sa.enable(config['number'],config['project'])
    disable.show()
    js = json.dumps(sa, indent=4, cls=ServiceAccountEncoder)
    write('sa.json',js)


print(config)