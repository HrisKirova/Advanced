from unittest import TestCase, main

from project.senior_student import SeniorStudent


class TestSeniorStudent(TestCase):
    def setUp(self):
        self.senior_student = SeniorStudent('12345', "John Doe", 5.5)
    def test_init(self):
        self.assertEqual("12345", self.senior_student.student_id)
        self.assertEqual("John Doe", self.senior_student.name)
        self.assertEqual(5.5, self.senior_student.student_gpa)
        self.assertEqual(self.senior_student.colleges, set())

    def test_id_length_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

    def test_name_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.senior_student.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    def test_student_gpa_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_gpa = 0.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_gpa = -0.1
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    def test_apply_to_college(self):
        self.senior_student.student_gpa = 4.0
        self.senior_student.gpa_required = 5.0
        self.senior_student.apply_to_college(5.0, "Test College")
        self.assertEqual("Application failed!", self.senior_student.apply_to_college(5.0, "Test College"))

        self.senior_student.name = "Ivan"
        self.senior_student.student_gpa = 5.0
        self.senior_student.gpa_required = 4.0
        self.senior_student.colleges = set()
        self.senior_student.apply_to_college(4.0, "Hogwarts")
        self.assertEqual({"HOGWARTS"}, self.senior_student.colleges)
        self.assertEqual("Ivan successfully applied to Hogwarts.", self.senior_student.apply_to_college(4.0, "Hogwarts"))

    def test_update_gpa_invalid(self):
        self.senior_student.student_gpa = 3.0
        result = self.senior_student.update_gpa(1.0)
        self.assertEqual("The GPA has not been changed!", result)
        self.assertEqual(3.0, self.senior_student.student_gpa)  # unchanged

    def test_update_gpa_valid(self):
        result = self.senior_student.update_gpa(4.2)
        self.assertEqual("Student GPA was successfully updated.", result)
        self.assertEqual(4.2, self.senior_student.student_gpa)

    def test_students_equal_by_gpa(self):
        other_student = SeniorStudent('12345', "Ivan", 5.5)
        self.senior_student.student_gpa = 5.5

        self.assertTrue(self.senior_student == other_student)

    def test_students_not_equal_by_gpa(self):
        other_student = SeniorStudent('12345', "Ivan", 5.5)
        self.senior_student.student_gpa = 3.5

        self.assertFalse(self.senior_student == other_student)

if __name__ == "__main__":
    main()
from project.senior_student import SeniorStudent

