from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DataAccessLayer:
    """ access to DB fabric"""

    def __init__(self, conn_string, base, echo=False):
        self.engine = None # Ссылка на создаваемый объект движка.
        self.Session = None # Ссылка на класс-сессию.
        self.session = None # Ссылка на объект сессии.
        self.conn_string = conn_string # Ссылка на путь до базы данных.
        self.echo = echo # Флаг, отвечающий за включение логгирования.
        self.Base = base # Ссылка на базовый класс, который мы используем при описании моделей.

    def connect(self):
        self.engine = create_engine(self.conn_string, echo=self.echo) # Создаем объект движка.
        self.Base.metadata.create_all(self.engine) # переносим описание моделей на структуру таблиц базы данных.
        self.Session = sessionmaker(bind=self.engine) # Создаем класс-сессию в привязке к движку, который мы создали ранее
