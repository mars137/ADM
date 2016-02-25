__author__ = 'Group 6'


from bottle import template, route, run, request, get, post, redirect
from bottle import static_file
import webbrowser
import DBconnection
import mapreduce
import heapq
from operator import itemgetter

# Defining global variables

data = None
templist = []
output = []
tskillList = []
toolskills = []
yearofexp = ""
edulevel =""


# Handling CSS

@route('/static/:filename#.*#', name='css')
def server_static(filename):
    return static_file(filename, root='./static')


@get('/')
def parse():
    return template("finalindex.html", msg = None)


@post('/')
def extractFormData():
    # message = None
    # global db

# Storing Seek Jobs form data into resume collection

    if request.POST.get("postresume") == "Submit Profile":
        print("Handled Resume Post")
        collectionName = "resume"
        resumeCollection = DBconnection.getcollection(collectionName)

        dataDict = {}
        dataDict['FirstName'] = request.forms.get("fname").lower()
        dataDict['LastName'] = request.forms.get("lname").lower()
        dataDict['EducationLevel'] = request.forms.get("edulevel").lower()
        dataDict['Company'] = request.forms.get("company").lower()
        dataDict['JobTitle'] = request.forms.get("jobtitle").lower()
        dataDict['TechSkills'] = request.forms.get("tskillsp").strip()
        dataDict['TechSkills'] = splitformdata(dataDict['TechSkills'])
        dataDict['ToolSkills'] = request.forms.get("tskillst").strip()
        dataDict['ToolSkills'] = splitformdata(dataDict['ToolSkills'])
        dataDict['WorkExperience'] = request.forms.get("workex").strip()
        dataDict['WorkExperience'] = splitformdata(dataDict['WorkExperience'])
        dataDict['yearsOfExperience'] = request.forms.get("yearsofexp").strip()
        dataDict['Email'] = request.forms.get("email").lower()

        if not resumeCollection.find_one({"Email": dataDict['Email']}):
            resumeCollection.insert(dataDict)
            message = "Candidate Resume successfully added :)"
        else:
            message = "Entry already exists in database!"
        return template("result.html", data=[], msg=message)

# Storing Hire form data into jobdesc collection

    elif request.POST.get("getcandidate") == "Job Description":
        print("Handled Job Description Post")
        newcollectionName = "jobdesc"
        jobdescCollection = DBconnection.getcollection(newcollectionName)

        jobdescDict = {}
        jobdescDict['ReqEducationLevel'] = request.forms.get("reqedulevel").lower()
        jobdescDict['ReqTechSkills'] = request.forms.get("reqtskillsp").strip()
        jobdescDict['ReqTechSkills'] = splitformdata(jobdescDict['ReqTechSkills'])
        jobdescDict['ReqToolSkills'] = request.forms.get("reqtskillst").strip()
        jobdescDict['ReqToolSkills'] = splitformdata(jobdescDict['ReqToolSkills'])
        jobdescDict['ReqYearsOfExperience'] = request.forms.get("reqyearsofexp").strip()

        if not jobdescCollection.find_one({"ReqEducationLevel": jobdescDict['ReqEducationLevel'], "ReqTechSkills": jobdescDict['ReqTechSkills'],"ReqYearsOfExperience": jobdescDict['ReqYearsOfExperience']}):
            jobdescCollection.insert_one(jobdescDict)
        comparedata(jobdescDict['ReqTechSkills'], jobdescDict['ReqToolSkills'], jobdescDict['ReqYearsOfExperience'], jobdescDict['ReqEducationLevel'])

# Formatting and splitting the data

def splitformdata(value):
     value1 = value.lower()
     finalvalue = value1.split(",")
     return finalvalue

# Matching the job description data to resumes (includes the mapreduce function as well)

def comparedata(a,b,c,d):

    global templist, output
    collectionName = "resume"
    resumeCollection = DBconnection.getcollection(collectionName)

    tskillList = a
    toolskills = b
    yearofexp = c
    edulevel = d
    sort = []

    tempoutput = mapreduce.mapReduce(tskillList,toolskills,yearofexp,edulevel)

# Checking if the output of mapreduce is empty
    templist = tempoutput
    if tempoutput != []:
        for doc in tempoutput:
            if doc['value']:
                sort.append((doc["_id"], int(doc["value"])))

# Finding the top candidates in resume collection based on email and appending them to a dictionary

    final = sorted(sort, key=itemgetter(1))

    for item in final:
        output.append(resumeCollection.find_one({"Email": item[0]}))

    redirect("/result")

# Display the output on result.html paga

@route("/result")
def display():
    global templist, output
    tag = ""
    if templist == []:
        tag = "Bad Luck! No suitable candidates found."

    else:
        for dataDoc in output:
            tag = "Here are the best matches : "
    return template("result.html", data=output, msg=tag)



if __name__=='__main__':
    webbrowser.open("http://localhost:8080/")
    run(host='localhost', port=8080, debug=True)


