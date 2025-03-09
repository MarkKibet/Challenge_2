from database import engine, Base, get_db
from crud import create_role_and_audition, query_role, update_audition

Base.metadata.create_all(bind=engine)
def main():
    db = next(get_db())
    create_role_and_audition(db)
    query_role(db)
    update_audition(db)
    # delete_audition(db)

if __name__ == "__main__":
    main()
