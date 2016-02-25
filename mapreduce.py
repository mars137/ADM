__author__ = 'Group 6'


from bson.code import Code
import DBconnection


def mapReduce(tskillList,toolskills,yearofexp,edulevel):

    collectionName = "resume"
    resumeCollection = DBconnection.getcollection(collectionName)
    newcollectionName = "mroutput"
    mroutputCollection = DBconnection.getcollection(newcollectionName)

    mapper = Code("function () {"
               "for (index in this.WorkExperience) {"
               "emit(this.Email,this.WorkExperience[index]);"
        "}"
    "}")



    reducer = Code("function(email, workex) {"

            "var regex1 = new RegExp('collaborated', 'i');"
            "var regex2 = new RegExp('managed', 'i');"
            "var regex3 = new RegExp('developed', 'i');"
            "var regex4 = new RegExp('designed', 'i');"
            "var regex5 = new RegExp('initiated', 'i');"
            "total = 0;"
            "lscore = 0;"
            "twscore = 0;"
            "ascore = 0;"

            "if(regex1.test(workex))"
                "lscore += 1;"
                "twscore += 1;"
            "if(regex2.test(workex))"
                "lscore += 1;"
                "twscore += 1;"
            "if(regex3.test(workex))"
                "ascore += 1;"
            "if(regex4.test(workex))"
                "ascore += 1;"
            "if(regex5.test(workex))"
                "lscore += 1;"
                "ascore += 1;"
            "total = lscore + twscore + ascore-1;"
            "return total"
    "}")

    resumeCollection.map_reduce(mapper, reducer, "mroutput", query={"TechSkills": {"$all": tskillList}, "ToolSkills": {"$all": toolskills}, "EducationLevel": edulevel, "yearsOfExperience": yearofexp})

# Getting the values of the mapreduce result

    outputlist = []
    for doc in mroutputCollection.find():
         outputlist.append(doc)

    return (outputlist)
ut