with open('input', 'r') as fh:
    data = fh.readlines()

course_data = {
    "depth": 0,
    "horizontal": 0,
    "aim": 0
}

for this_course in data:
    this_course_split = this_course.split(" ")
    
    match this_course_split[0]:
        case "forward":
            course_data["horizontal"] += int(this_course_split[1])
            course_data["depth"] += (int(this_course_split[1]) * course_data['aim'])
        case "down":
            course_data["aim"] += int(this_course_split[1])
        case "up":
            course_data["aim"] -= int(this_course_split[1])

print(course_data)
print(course_data['horizontal'] * course_data['depth'])