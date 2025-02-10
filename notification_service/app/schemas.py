from pydantic import BaseModel
from datetime import datetime

class NotificationCreate(BaseModel):
    name: str
    status: str
    description: str
    id_user: str
