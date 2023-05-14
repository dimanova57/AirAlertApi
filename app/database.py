from sqlalchemy import Column, Boolean, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///app.db?check_same_thread=False")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True)
    email = Column(String)
    password = Column(String)

    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.email = email
        self.password = password


class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    isAlert = Column(Boolean, unique=False, nullable=True)

    def __init__(self, name, isAlert):
        self.name = name
        self.isAlert = isAlert


list_of_region = ["Автономна Республіка Крим", "Вінницька", "Волинська", "Дніпропетровська", "Донецька", "Житомирська",
                  "Закарпатська", "Запорізька", "Івано-Франківська", "Київська", "Кіровоградська", "Луганська",
                  "Львівська", "Миколаївська", "Одеська", "Полтавська", "Рівненська", "Сумська", "Тернопільська",
                  "Харківська", "Херсонська", "Хмельницька", "Черкаська", "Чернівецька", "Чернігівська", "Київ"]


Base.metadata.create_all(engine)

# for name in list_of_region:
#     region = Region(name=name, isAlert=False)
#     session.add(region)
#     session.commit()
