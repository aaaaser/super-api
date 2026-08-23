import sys
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from core.database import Base, get_db
from main import app

# IMPORT SEMUA MODEL DI SINI (supaya tabel otomatis terbuat)
import features.projects.models
import features.attendance.models

sys.path.insert(0, str(Path(__file__).parent))

# Database In-Memory khusus Testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True)
def setup_test_db():
    # Buat tabel sebelum tes berjalan
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    yield

    # Hapus tabel setelah tes selesai
    Base.metadata.drop_all(bind=engine)


# FIXTURE CLIENT YANG DIBUTUHKAN PYTEST
@pytest.fixture
def client():
    """Membuat TestClient FastAPI untuk dipanggil di unit test."""
    with TestClient(app) as c:
        yield c