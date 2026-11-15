import random
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Subject

DB_URL = "postgresql+psycopg2://postgres:test1@localhost:5433/postgres"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@pytest.fixture
def db():
    session = SessionLocal()
    created_ids = []
    try:
        yield session, created_ids
    finally:
        cleanup = SessionLocal()
        try:
            for sid in created_ids:
                obj = cleanup.get(Subject, sid)
                if obj is not None:
                    cleanup.delete(obj)
            cleanup.commit()
        except Exception:
            cleanup.rollback()
            raise
        finally:
            cleanup.close()
        session.close()


@pytest.fixture
def subject_data():
    rand_id = random.randint(1_000_000, 2_000_000_000)
    title = f"Test Subject {rand_id}"
    return rand_id, title


def test_add_subject(db, subject_data):
    session, created_ids = db
    sid, title = subject_data

    session.add(Subject(subject_id=sid, subject_title=title))
    session.commit()
    created_ids.append(sid)

    stored = session.get(Subject, sid)
    assert stored is not None
    assert stored.subject_title == title


def test_update_subject(db, subject_data):
    session, created_ids = db
    sid, title = subject_data
    new_title = f"Updated {sid}"

    session.add(Subject(subject_id=sid, subject_title=title))
    session.commit()
    created_ids.append(sid)

    stored = session.get(Subject, sid)
    stored.subject_title = new_title
    session.commit()

    fresh = session.get(Subject, sid)
    session.expire_all()
    assert fresh.subject_title == new_title


def test_delete_subject(db, subject_data):
    session, created_ids = db
    sid, title = subject_data

    session.add(Subject(subject_id=sid, subject_title=title))
    session.commit()
    created_ids.append(sid)

    stored = session.get(Subject, sid)
    session.delete(stored)
    session.commit()

    assert session.get(Subject, sid) is None
