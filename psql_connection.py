# PostgreSQL Connection and Data Insertion using SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database connection parameters
DB_HOST = "localhost"      # Change this to your PostgreSQL server address
DB_PORT = "5432"           # Default PostgreSQL port
DB_NAME = "tutorial_db"    # Change this to your database name
DB_USER = "postgres"       # Change this to your PostgreSQL username
DB_PASSWORD = "your_password"  # Change this to your PostgreSQL password

# Create the database URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False)

# Create declarative base
Base = declarative_base()


class Student(Base):
    """
    Student model class representing the students table.
    """
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
    grade = Column(String(1))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}', age={self.age}, grade='{self.grade}')>"


def create_tables():
    """
    Creates all tables defined in the models.
    """
    try:
        Base.metadata.create_all(engine)
        print("✓ Tables created successfully!")
    except Exception as e:
        print(f"✗ Error creating tables: {e}")


def insert_data():
    """
    Inserts sample data into the students table using SQLAlchemy ORM.
    """
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Sample data to insert
        students_list = [
            Student(name="Alice Johnson", email="alice@example.com", age=20, grade="A"),
            Student(name="Bob Smith", email="bob@example.com", age=21, grade="B"),
            Student(name="Charlie Brown", email="charlie@example.com", age=19, grade="A"),
            Student(name="Diana Prince", email="diana@example.com", age=22, grade="B"),
            Student(name="Eve Wilson", email="eve@example.com", age=20, grade="C")
        ]
        
        # Add all students to the session
        session.add_all(students_list)
        
        # Commit the transaction
        session.commit()
        print(f"✓ Successfully inserted {len(students_list)} records into the database!")
    
    except Exception as e:
        session.rollback()
        print(f"✗ Error inserting data: {e}")
    
    finally:
        session.close()


def fetch_data():
    """
    Retrieves and displays all records from the students table.
    """
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Query all students
        students = session.query(Student).all()
        
        print("\n" + "=" * 90)
        print("Students Table Data:")
        print("=" * 90)
        print(f"{'ID':<5} {'Name':<20} {'Email':<30} {'Age':<5} {'Grade':<5}")
        print("-" * 90)
        
        for student in students:
            print(f"{student.id:<5} {student.name:<20} {student.email:<30} {student.age:<5} {student.grade:<5}")
        
        print("=" * 90)
        print(f"Total students: {len(students)}")
    
    except Exception as e:
        print(f"✗ Error fetching data: {e}")
    
    finally:
        session.close()


def query_by_grade(grade):
    """
    Query students by grade.
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        students = session.query(Student).filter_by(grade=grade).all()
        
        print(f"\n✓ Students with grade '{grade}':")
        for student in students:
            print(f"  - {student.name} ({student.email})")
    
    except Exception as e:
        print(f"✗ Error querying data: {e}")
    
    finally:
        session.close()


def delete_student(email):
    """
    Deletes a student by email.
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        student = session.query(Student).filter_by(email=email).first()
        
        if student:
            session.delete(student)
            session.commit()
            print(f"✓ Student with email '{email}' deleted successfully!")
        else:
            print(f"✗ No student found with email '{email}'")
    
    except Exception as e:
        session.rollback()
        print(f"✗ Error deleting student: {e}")
    
    finally:
        session.close()


def update_student_grade(email, new_grade):
    """
    Updates a student's grade by email.
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        student = session.query(Student).filter_by(email=email).first()
        
        if student:
            old_grade = student.grade
            student.grade = new_grade
            session.commit()
            print(f"✓ Updated {student.name}'s grade from '{old_grade}' to '{new_grade}'")
        else:
            print(f"✗ No student found with email '{email}'")
    
    except Exception as e:
        session.rollback()
        print(f"✗ Error updating student: {e}")
    
    finally:
        session.close()


def main():
    """
    Main function to execute database operations using SQLAlchemy.
    """
    print("Starting PostgreSQL Connection with SQLAlchemy ORM...\n")
    
    try:
        # Test connection
        with engine.connect() as connection:
            print("✓ Successfully connected to PostgreSQL database!")
    except Exception as e:
        print(f"✗ Error connecting to PostgreSQL: {e}")
        print("Please check your connection parameters and ensure PostgreSQL is running.")
        return
    
    # Create tables
    create_tables()
    
    # Insert data
    insert_data()
    
    # Fetch and display data
    fetch_data()
    
    # Additional query examples
    print("\nAdditional Query Examples:")
    query_by_grade("A")
    query_by_grade("B")
    
    # Update example
    print()
    update_student_grade("bob@example.com", "A")
    
    # Display updated data
    print("\nUpdated Students Table:")
    fetch_data()


if __name__ == "__main__":
    main()


"""
SETUP INSTRUCTIONS:
===================

1. Install required packages:
   pip install sqlalchemy psycopg2-binary

2. Update the database connection parameters:
   - DB_HOST: Your PostgreSQL server address (usually 'localhost')
   - DB_PORT: PostgreSQL port (default is 5432)
   - DB_NAME: Your database name
   - DB_USER: Your PostgreSQL username (default is 'postgres')
   - DB_PASSWORD: Your PostgreSQL password

3. Run the script:
   python psql_connection.py

ADVANTAGES OF SQLALCHEMY:
=========================
- Object-Relational Mapping (ORM) - work with Python objects instead of SQL queries
- Automatic table creation and schema management
- Easy query filtering and relationships
- Protection against SQL injection
- Database-agnostic code (can switch databases easily)
- Connection pooling and performance optimization
- Relationship support for complex data structures
"""
