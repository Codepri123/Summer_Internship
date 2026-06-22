data= {"name":["aman","arjun","priyanka"],
       "marks":[90,40,45]
       }

sorted_marks = dict(sorted(data.items(), key=lambda x: x[1]))

print(sorted_marks)