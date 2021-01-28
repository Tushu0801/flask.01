from flask import Flask, render_template, request, redirect, url_for

courseList = [ ]

app = Flask(__name__) 

@app.route("/") # route # get
def index():
    return render_template('index.html', courseList = courseList)

@app.route("/add", methods=['GET', 'POST'])
def addCourse():
    
    if request.method == 'POST': # POST
        data = request.form
        courseName = data['courseName']
        teacherName = data['teacherName']
        courseID = data['courseID']
        teacherID = len(courseList)+1
        classID = len(courseList)+1
        
        
        courseList.append({
            'courseName': courseName,
            'teacherName': teacherName,
            'courseID' : courseID,
            'teacherID' : teacherID,
            'classID' : classID
       })

        sum = 0
        if(len(courseList)+1 > 1):
            for i in range(1,len(courseList)+1,1):
                sum=sum+1
            print(sum)

        print(courseList)

        #if(len(courseList)+1 > 1):
        #    if (addCourse(courseList[0]) == addCourse(courseList[1])):
        #        print('Matched')
        #    else:
        #        print('Not Matched')
    
        return redirect(url_for('index'))
    else: # GET
        return render_template('addCourse.html')

@app.route("/delete/<string:courseName>", methods=['GET'])
def deleteCourse(courseName):
    indexToBeDeleted = -1 # 0
    for i in range(len(courseList)):
        if courseList[i]['courseName'] == courseName: # XYZ # Udit
            indexToBeDeleted = i
            break
    if (indexToBeDeleted != -1):
        del courseList[indexToBeDeleted]
        #return render_template('deleteCourse.html')
        return redirect(url_for('index'))
        #return "Course deleted"
    return "Course does not exist"
    

@app.route("/update/<string:courseName>", methods=['GET', 'POST'])
def updateCourse(courseName):
    for i in courseList:
        if i['courseName'] == courseName:
            # return "Student name is : {0}\nStudent college is: {1}".format(i['name'], i['college'])
            if request.method == 'POST':
                data = request.form
                teacherName = data['teacherName']
                i['teacherName'] = teacherName
                #teacherID = data['teacherID']
                #i['teacherID'] = teacherID
                #classID = data['classID'] 
                #i['classID'] = classID
                return redirect(url_for('index'))
            else:
                return render_template('updateCourse.html', course=i)

if __name__ == "__main__": # starting point of the application
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True)
