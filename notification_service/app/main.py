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


@app.delete("/notifications/first/")
async def delete_first_notification(db=Depends(get_db)):
    first_notification = await db.notifications.find_one({}, sort=[("date", 1)])
    
    if not first_notification:
        raise HTTPException(status_code=404, detail="No notifications found")

    await db.notifications.delete_one({"_id": first_notification["_id"]})
    return {"message": "First notification deleted successfully"}

@app.get("/notifications/first10/")
async def get_first_10_notifications(db=Depends(get_db)):
    notifications_cursor = db.notifications.find().sort("date", -1).limit(10)
    notifications_list = await notifications_cursor.to_list(length=10)  # Ensures we get only 10 items

    return [
        {
            "id_notification": notification["id_notification"],
            "message": notification["message"],
            "id_user": notification["id_user"],
            "date": notification["date"]
        }
        for notification in notifications_list
    ]