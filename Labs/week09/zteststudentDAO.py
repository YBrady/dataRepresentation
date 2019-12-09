from zStudentDAO import studentDAO

#create
latestid = studentDAO.create(("Mark", 45))

# find by id
result = studentDAO.findByID(latestid);
print ("1.",result)

# update
studentDAO.update(("Fred", 21, latestid))
results = studentDAO.findByID(latestid);
print("2.", result)

# get all
allStudents = studentDAO.getAll()
for student in allStudents:
    print("3.",student)

# delete
studentDAO.delete(latestid)