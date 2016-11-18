#!/usr/bin/env python
####################################
#author        terry.li
#date          18/11/2016
#version       1.0.0
#description   counting Dorryweb issues
#              and reporting to slack
####################################

import urllib2
import json

def getData(type):
        index = 1
        baseurl = "https://api.github.com/repos/MatchboxDorry/dorry-web/issues?state={}&per_page=100&page={}"
        #print baseurl.format(type,index)
        response = urllib2.urlopen(baseurl.format(type,index))
        data = json.load(response)
        length = len(data)
        #print length
        while length == 100 :
                index = index + 1
                data = data.append(json.load(urllib2.urlopen(baseurl.format(type,index))))
                length = len(data)
        return data    

def getPullRequestNum(data):
        index = 0
        for item in data:
                try:
                        item['pull_request']
                        index = index + 1
                except Exception as e:
                        pass
        return index
                        
def getIssuesNum(data):
        return len(data) - getPullRequestNum(data)

def getFilterIssuesNum(data,labels):
        index = 0
        data_labels = []
        for item in data:
                data_labels.append(item['labels'])
        for data_label in data_labels:
                print "label:>>>>" + data_label
                
        if set(lebels).issubset(set(data['labels'])):
                index = index + 1
        
        
def main():
        open_all = getData('open')
        close_all = getData('closed')
        
        open_issue = getIssuesNum(openData)
        close_issue = getIssuesNum(closedData)

        open_fixed_issue = get
        

if __name__ == "__main__":
	main()

