ALTER TABLE attendance ADD COLUMN student_id INT;
ALTER TABLE attendance ADD COLUMN marked_by INT;

ALTER TABLE attendance
ADD FOREIGN KEY (student_id) REFERENCES students(id);

ALTER TABLE attendance
ADD FOREIGN KEY (marked_by) REFERENCES users(id);
  
ALTER TABLE attendance
ADD CONSTRAINT unique_attendance
UNIQUE (student_id, date);