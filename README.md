# notification_service

# run the program

- docker run -d --name mongodb -p 27017:27017 mongo\
- pip install -r requirements.txt
-  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# testing

http://localhost:8000/docs

post endpoint

{
  "name": "alejandra",
  "status": "completado",
  "description": "limpiar caneca",
  "id_user": "90w3-e"
}

response

{
  "id_notification": "339a568",
  "message": "alejandra: limpiar caneca (Status: completado)",
  "date": "2025-02-10T08:43:51.008036"
}
