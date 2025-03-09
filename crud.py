from sqlalchemy.orm import Session
from models import Audition, Role

def create_role_and_audition(db: Session):
    new_role = Role(character_name="Shujaa Liyongo")
    db.add(new_role)
    db.commit()

    new_audition = Audition(actor="Cliff Ombeta", location="Nakuru", phone=254745908587, role=new_role)
    db.add(new_audition)
    db.commit()

    another_audition = Audition(actor="MIchael Limaji", location="Meru", phone=254717654835, hired= True, role=new_role)
    db.add(another_audition)
    db.commit()
  
   
def query_role(db: Session):
    role = db.query(Role).filter_by(character_name="Shujaa Liyongo").first()
    print(role.actors())
    print(role.locations())

def update_audition(db: Session):
    audition = db.query(Audition).filter_by(actor="Cliff Ombeta").first()
    audition.call_back()
    db.commit()

# def delete_audition(db: Session):
#     audition = db.query(Audition).filter_by(actor="John Doe").first()
#     db.delete(audition)
#     db.commit()
