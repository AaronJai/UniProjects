import java.util.ArrayList;

// Created class to represent a pair of student and course
class StudentCourse {
    private String student;
    private String course;

    public StudentCourse(String student, String course) {
        this.student = student;
        this.course = course;
    }

    public String getStudent() {
        return student;
    }

    public String getCourse() {
        return course;
    }
}

public class ClassDatabase {
    // ArrayList to store pairs of student and course
    private ArrayList<StudentCourse> studentCourses;

    public ClassDatabase() {
        // Initialize the ArrayList
        studentCourses = new ArrayList<>();
    }

    // Method to add a student to a course
    public void addCourseStudent(String student, String course) {
        // Create a new StudentCourse object and add it to the ArrayList
        StudentCourse sc = new StudentCourse(student, course);
        studentCourses.add(sc);
    }

    // Method to count the number of students in a course
    public int countStudents(String course) {
        int count = 0;
        // Iterate through the ArrayList and count occurrences of the specified course
        for (StudentCourse i : studentCourses) {
            if (i.getCourse().equals(course)) {
                count++;
            }
        }
        return count;
    }

    public int countStudents() {
        int count = 0;

        for (StudentCourse i : studentCourses) {
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        // Testing the ClassDatabase class
        ClassDatabase db = new ClassDatabase();
        db.addCourseStudent("Alan Turing", "CITS2005");
        db.addCourseStudent("Alan Turing", "CITS2200");
        db.addCourseStudent("Max", "CITS9999");
        db.addCourseStudent("Gozz", "CITS9999");
        db.addCourseStudent("Jane Doe", "CITS2005");

        // Print the number of students in each course
        System.out.println(db.countStudents("CITS2005")); // Should print 2
        System.out.println(db.countStudents("CITS2200")); // Should print 1
        System.out.println(db.countStudents("CITS9999")); // Should print 2
        System.out.println(db.countStudents());
    }
}