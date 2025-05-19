from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

parent_dir = path.dirname(
    path.dirname(path.abspath(__file__))
    )

sys.path.append(parent_dir)

from cnstctr.app import app

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    password: Mapped[str]