from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from geopy.distance import geodesic
from validation import ItemCreate, ItemResponse, AreasCovered
 
# FastAPI app instance
app = FastAPI()
 
# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
 
# Database model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    longitude = Column(Integer)
    latitude = Column(Integer)
 
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
# API endpoint to read an item by ID
@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Error reading: Item not found")
    return db_item

# API endpoint to call all items
@app.get("/all", response_model=list[ItemResponse])
def read_all(db: Session = Depends(get_db)):
    db_items = db.query(Item).all()
    if not db_items:
        raise HTTPException(status_code=404, detail="Error reading: Items not found")
    
    return db_items

# API endpoint to create an item
@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Error inserting: Item not found")
    db.commit()
    db.refresh(db_item)
    return db_item

# API endpoint to update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item_data: dict, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Error updating: Item not found")
    # Update the item with the new data
    if "name" in item_data:
        db_item.name = item_data["name"]
    if "description" in item_data:
        db_item.description = item_data["description"]
    if "longitude" in item_data:
        db_item.longitude = item_data["longitude"]
    if "latitude" in item_data:
        db_item.latitude = item_data["latitude"]

    db.commit()
    db.refresh(db_item)
    return db_item

# API endpoint to delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Error deleting: Item not found")
    db.delete(db_item)
    db.commit()
    return db_item

# API endpoint to compute areas within given coordinates and distance
@app.get("/areas")
def areas_covered(area: AreasCovered, db: Session = Depends(get_db)):
    area_covered = []
    base_location = (area.longitude, area.latitude)
    db_items = db.query(Item).all()
    for address in db_items:
        address_location = (address.longitude, address.latitude)
        if geodesic(base_location, address_location).kilometers <= area.distance:
            area_covered.append(address)
    if len(area_covered) == 0:
        return {"msg": "No areas covered"}
    return area_covered
 
if __name__ == "__main__":
    import uvicorn
 
    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)