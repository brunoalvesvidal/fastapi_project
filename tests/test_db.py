from sqlalchemy import select

from fastapi_main.models import User


def test_create_user(session):
    user = User(
        username="brunoalves",
        email="bruno@ssauro.com",
        password="senhapadrao",
    )
    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == "bruno@ssauro.com")
    )

    assert result.id == 1
