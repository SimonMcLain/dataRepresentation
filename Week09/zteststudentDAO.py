from zstudentDAO import studentDAO

#create command
latestid = studentDAO.create(('mark', 45))

#FIND BY ID
result = studentDAO.findByID(latestid);
print(result)

#Update
studentDAO.update(('Fred', 43, latestid))
result = studentDAO.findByID(latestid);
print(result)

#Get All
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)

#DELETE

studentDAO.delete(latestid)