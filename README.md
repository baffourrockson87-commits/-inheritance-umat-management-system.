# -inheritance-umat-management-system.
# Campus Management System Using Inheritance in Python

## Overview

This project demonstrates the concept of **inheritance** in Object-Oriented Programming (OOP) using Python. It models a simple university campus management system where different types of people—Students and Lecturers—share common characteristics while also having their own unique attributes and behaviors.

## Objectives

The project aims to:

* Demonstrate the use of inheritance.
* Show how child classes inherit attributes and methods from a parent class.
* Use the `super()` function to initialize inherited attributes.
* Demonstrate method overriding.
* Apply basic OOP principles in Python.

## Class Structure

### 1. Person (Parent Class)

The `Person` class serves as the base class for all people on campus.

**Attributes**

* `name` – Stores the person's name.
* `age` – Stores the person's age.

**Method**

* `display_info()` – Displays the person's name and age.

### 2. Student (Child Class)

The `Student` class inherits from the `Person` class.

**Additional Attribute**

* `student_id` – Stores the student's identification number.

**Methods**

* `enroll_course(course)` – Displays the course the student has enrolled in.
* `display_info()` – Overrides the parent method to display the student's ID in addition to the inherited information.

### 3. Lecturer (Child Class)

The `Lecturer` class also inherits from the `Person` class.

**Additional Attribute**

* `employee_id` – Stores the lecturer's employee identification number.

**Method**

 – Displays the course the lecturer is teaching.

## OOP Concepts Demonstrated

* **Inheritance:** `Student` and `Lecturer` inherit from the `Person` class.
* **Method Overriding:** The `Student` class overrides the `display_info()` method.
* **Use of `super()`:** Used to initialize inherited attributes and call the parent class method.
* **Code Reusability:** Common attributes and methods are defined once in the parent class and reused by child classes.

## Sample Output

``t Information 
Name: Rockson Baffour
Age: 21
Student ID: FOE.41.006.m
Rockson Baffour has enrolled in Object-Oriented Programming.

----- Lecturer Information -----
Name: Dr. Cobbinah
Age: 30
Dr. Cobbinah is teaching Object-Oriented Programming.
