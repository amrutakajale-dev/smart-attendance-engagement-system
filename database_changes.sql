ALTER TABLE attendance ADD COLUMN student_id INT;
ALTER TABLE attendance ADD COLUMN marked_by INT;

ALTER TABLE attendance
ADD FOREIGN KEY (student_id) REFERENCES students(id);

ALTER TABLE attendance
ADD FOREIGN KEY (marked_by) REFERENCES users(id);
  
ALTER TABLE attendance
ADD CONSTRAINT unique_attendance
UNIQUE (student_id, date);

/*inner join to show students name as well */
SELECT students.name, attendance.date, attendance.status
FROM attendance
INNER JOIN students
ON attendance.student_id = students.id
ORDER BY attendance.date DESC;