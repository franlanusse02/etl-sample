from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#fNAME,lNAME,Age,gender,country,residence,entryEXAM,prevEducation,studyHOURS,Python,DB

class Students(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    f_name = db.Column(db.String(255))
    l_name = db.Column(db.String(255))
    age = db.Column(db.Integer)

    country_id = db.relationship(db.Integer, db.ForeignKey('country.id')) #reference with foreign id to country class 
    prev_education_id = db.Column(db.Integer, db.ForeignKey('education.id')) #reference with foreign id to education 

    esidence = db.Column(
        db.Enum('Sognsvann', 'Private', 'Bi Residence', name='residence_enum')
    )

    study_hours = db.Column(db.Integer)

    entry_exam = db.Column(db.Integer) #must be number 0-100
    python_score = db.Column(db.Float) #must be number 0-100
    db_score = db.Column(db.Integer) #must be number 0-100


class Country(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    country_name = db.Column(db.String(255))
    students = db.relationship('Students', back_populates='country') #relates to country_id

class Education(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    education_name = db.Column(db.String(255))
    students = db.relationship('Students', back_populates='education') #relates to education_id