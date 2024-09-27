from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.db.String(120), unique=True, nullable=False)
#     password = db.Column(db.db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return f'<User {self.email}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#         }

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),unique=True,nullable=False)
    password = db.Column(db.db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship("Favorite",back_populates="user",uselist=True)

    def __repr__(self) -> str:
        return f"<User {self.username}>"

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "is_active": self.is_active,
        }

class Favorite(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    user = db.relationship("User",back_populates="favorites",uselist=False)
    favorite_type = db.Column(db.String(20))  # 'planet' or 'people'
    favorite_id = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "favorite_type": self.favorite_type,
            "favorite_id": self.favorite_id
        }
    
class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),  nullable=False)
    height = db.Column(db.String(120),  nullable=False)
    mass = db.Column(db.String(120),  nullable=False)
    hair_color = db.Column(db.String(120),  nullable=False)
    skin_color = db.Column(db.String(120),  nullable=False)
    eye_color = db.Column(db.String(120),  nullable=False)
    birth_year = db.Column(db.String(120),  nullable=False)
    gender = db.Column(db.String(120),  nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

class Planet(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    diameter = db.Column(db.String(120),  nullable=False)
    climate = db.Column(db.String(120),  nullable=False)
    gravity = db.Column(db.String(120),  nullable=False)
    terrain = db.Column(db.String(120),  nullable=False)
    population = db.Column(db.String(120),  nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "population": self.population
        }