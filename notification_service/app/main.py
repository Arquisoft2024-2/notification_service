from fastapi import FastAPI, Depends
from app.database import get_db
from app.models import NotificationModel
from app.schemas import NotificationCreate
from datetime import datetime
import uuid

app = FastAPI()

@app.post("/notifications/")
async def create_notification(notification: NotificationCreate, db=Depends(get_db)):
    id_notification = str(uuid.uuid4())[:7]  # Generate 7-character alphanumeric ID
    message = f"{notification.name}: {notification.description} (Status: {notification.status})"
    date = datetime.now()

    new_notification = NotificationModel(
        id_notification=id_notification,
        message=message,
        id_user=notification.id_user,
        date=date
    )

    # Save to MongoDB
    result = await db.notifications.insert_one(new_notification.dict(by_alias=True))
    
    return {
        "id_notification": id_notification,
        "message": message,
        "date": date
    }
