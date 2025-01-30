from tinydb import TinyDB, Query

# Create or connect to the database
db = TinyDB('students.json')

class Students:
    def __init__(self, id, name, age, gender, contact, grade_level, math, science, english, attendance, activities, street, city, state, zip_code):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.grade_level = grade_level
        self.math = math
        self.science = science
        self.english = english
        self.attendance = attendance
        self.activities = activities
        self.street =  street,
        self.city = city,
        self.state = state,
        self.zip_code = zip_code


    def table(self):
        student_data = {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'contact': self.contact,
            'grade_level': self.grade_level,
            'subjects': {
                'math': self.math,
                'science': self.science,
                'english': self.english
            },
            'attendance': self.attendance,
            'activities': self.activities,
            'address': {
                'street': self.street,
                'city': self.city,
                'state': self.state,
                'zip_code': self.zip_code
        }
        }
        db.insert(student_data) 


s1 = Students(100, 'Alfa_1', 18, 'male', '111-222-333-444', 'grade 10', 80, 75, 85, 90.2, ['basketball', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s2 = Students(101, 'Alfa_2', 18, 'female', '485-365-624-585', 'grade 9', 81, 95, 87, 89, ['dancing', 'singing'], "11 main street", 'Tashkent', "Uzbekistan", 10024)
s3 = Students(102, 'Alfa_3', 18, 'male', '458-222-321-784', 'grade 11', 69, 70, 21, 75.0, ['coding', 'content creating'], "12 street", 'Tashkent', "Uzbekistan", 10024)
s4 = Students(103, 'Alfa_4', 18, 'male', '458-965-333-752', 'grade 10', 70, 86, 89, 75.9, ['basketball', 'reading book'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s5 = Students(104, 'Alfa_5', 18, 'female', '124-778-742-472', 'grade 9', 93, 92, 63, 73.3, ['basketball', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s6 = Students(105, 'Alfa_6', 18, 'male', '586-545-345-742', 'grade 9', 70, 78, 92, 88.0, ['basketball', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s7 = Students(106, 'Alfa_7', 18, 'female', '425-255-635-424', 'grade 10', 69, 76, 74, 56.8, ['basketball', 'reading book'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s8 = Students(107, 'Alfa_8', 18, 'female', '119-002-333-124', 'grade 10', 88, 62, 62, 88.5, ['dancing', 'playing chess'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s9 = Students(108, 'Alfa_9', 18, 'female', '369-365-355-741', 'grade 9', 80, 75, 85, 90.2, ['singing', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s10 = Students(109, 'Alfa_10', 18, 'male', '355-682-248-444', 'grade 8', 70, 74, 92, 53.7, ['reading book', 'dancing'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s11 = Students(110, 'Alfa_11', 18, 'female', '118-145-348-124', 'grade 8', 75, 80, 87, 89.1, ['basketball', 'playing chess'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s12 = Students(111, 'Alfa_12', 18, 'male', '389-312-364-648', 'grade 8', 65, 95, 60, 58.5, ['coding', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s13 = Students(112, 'Alfa_13', 18, 'male', '325-369-854-789', 'grade 9', 80, 75, 85, 90.2, ['basketball', 'singing'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s14 = Students(113, 'Alfa_14', 18, 'male', '785-785-869-321', 'grade 9', 91, 61, 87, 80.4, ['reading book', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s15 = Students(114, 'Alfa_15', 18, 'female', '111-245-248-784', 'grade 10', 60, 74, 64, 73.1, ['singing', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s16 = Students(115, 'Alfa_16', 18, 'female', '758-245-333-414', 'grade 10', 64, 99, 61, 57.2, ['dancing', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s17 = Students(116, 'Alfa_17', 18, 'male', '782-756-965-657', 'grade 10', 98, 86, 62, 73.6, ['playing chess', 'coding'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s18 = Students(117, 'Alfa_18', 18, 'male', '115-560-555-238', 'grade 11', 80, 75, 85, 90.2, ['basketball', 'reading book'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s19 = Students(118, 'Alfa_19', 18, 'female', '509-348-750-400', 'grade 11', 80, 75, 85, 90.2, ['basketball', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s20 = Students(119, 'Alfa_20', 18, 'male', '186-743-218-191', 'grade 11', 80, 75, 85, 90.2, ['coding', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s21 = Students(120, 'Alfa_21', 18, 'female', '718-514-150-699', 'grade 8', 80, 75, 85, 90.2, ['basketball', 'playing chess'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s22 = Students(121, 'Alfa_22', 18, 'male', '965-630-104-216', 'grade 11', 80, 75, 85, 90.2, ['basketball', 'reading book'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s23 = Students(122, 'Alfa_23', 18, 'female', '860-246-923-600', 'grade 10', 80, 75, 85, 90.2, ['basketball', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s24 = Students(123, 'Alfa_24', 18, 'male', '860-246-923-600', 'grade 10', 80, 75, 85, 90.2, ['coding', 'reading book'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s25 = Students(124, 'Alfa_25', 18, 'male', '517-806-740-678', 'grade 10', 80, 75, 85, 90.2, ['basketball', 'playing chess'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s26 = Students(125, 'Alfa_26', 18, 'male', '175-598-925-668', 'grade 9', 80, 75, 85, 90.2, ['dancing', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s27 = Students(126, 'Alfa_27', 18, 'female', '753-317-342-648', 'grade 8', 80, 75, 85, 90.2, ['playing chess', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s28 = Students(127, 'Alfa_28', 18, 'male', '444-876-760-742', 'grade 8', 80, 75, 85, 90.2, ['basketball', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s29 = Students(128, 'Alfa_29', 18, 'female', '850-516-422-461', 'grade 10', 80, 75, 85, 90.2, ['basketball', 'reading book'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s30 = Students(129, 'Alfa_30', 18, 'male', '360-813-833-659', 'grade 9', 80, 75, 85, 90.2, ['basketball', 'dancing'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s31 = Students(130, 'Alfa_31', 18, 'female', '585-337-645-232', 'grade 9', 80, 75, 85, 90.2, ['coding', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s32 = Students(131, 'Alfa_32', 18, 'female', '974-361-887-588', 'grade 11', 80, 75, 85, 90.2, ['basketball', 'playing chess'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s33 = Students(132, 'Alfa_33', 18, 'female', '811-946-819-570', 'grade 10', 80, 75, 85, 90.2, ['playing chess', 'reading book'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s34 = Students(133, 'Alfa_34', 18, 'female', '506-874-951-563', 'grade 10', 80, 75, 85, 90.2, ['basketball', 'singing'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s35 = Students(134, 'Alfa_35', 18, 'male', '135-262-925-758', 'grade 11', 80, 75, 85, 90.2, ['reading book', 'playing chess'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s36 = Students(135, 'Alfa_36', 18, 'male', '825-736-565-503', 'grade 10', 98, 97, 63, 85.1, ['basketball', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s37 = Students(136, 'Alfa_37', 18, 'male', '136-782-335-478', 'grade 9', 80, 75, 85, 90.2, ['coding', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s38 = Students(137, 'Alfa_38', 18, 'female', '321-460-225-942', 'grade 8', 70, 92, 85, 62.8, ['reading book', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s39 = Students(138, 'Alfa_39', 18, 'female', '111-282-325-444', 'grade 8', 73, 63, 80, 54.3, ['basketball', 'dancing'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s40 = Students(139, 'Alfa_40', 18, 'male', '178-872-333-441', 'grade 11', 61, 79, 99, 60.9, ['singing', 'playing chess'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s41 = Students(140, 'Alfa_41', 18, 'female', '178-352-333-784', 'grade 11', 82, 74, 94, 65.5, ['reading book', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s42 = Students(141, 'Alfa_42', 18, 'male', '111-222-333-694', 'grade 10', 80, 75, 85, 90.2, ['playing chess', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s43 = Students(142, 'Alfa_43', 18, 'female', '251-222-953-425', 'grade 8', 74, 65, 92, 59.3, ['dancing', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s44 = Students(143, 'Alfa_44', 18, 'female', '781-782-333-444', 'grade 10', 87, 67, 97, 91.4, ['coding', 'reading book'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s45 = Students(144, 'Alfa_45', 18, 'female', '111-852-333-489', 'grade 9', 63, 93, 93, 61.6, ['basketball', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s46 = Students(145, 'Alfa_46', 18, 'female', '111-222-333-359', 'grade 11', 80, 75, 85, 90.2, ['basketball', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s47 = Students(146, 'Alfa_47', 18, 'female', '361-224-378-784', 'grade 11', 69, 91, 71, 60.3, ['reading book', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s48 = Students(147, 'Alfa_48', 18, 'male', '541-482-783-488', 'grade 10', 98, 68, 66, 98.4, ['basketball', 'playing chess'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s49 = Students(148, 'Alfa_49', 18, 'male', '745-275-325-145', 'grade 10', 98, 100, 91, 68.0, ['dancing', 'football'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)
s50 = Students(149, 'Alfa_50', 18, 'female', '325-658-387-447', 'grade 10', 97, 84, 93, 69.3, ['singing', 'reading book'], "Mirzo Ulug'bek", 'Tashkent', "Uzbekistan", 10024)

students = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40, s41, s42, s43, s44, s45, s46, s47, s48, s49, s50]

for student in students:
    student.table()


