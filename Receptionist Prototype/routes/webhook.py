#  this file only work is to 
# receive HTTP requests
# call receptionist.py to process the request
# Return Json response 

from fastapi import APIRouter
from receptionist import Receptionist

router = APIRouter()

#create one receptionist instance
receptionist = Receptionist()

@router.post("/webhook")
def webhook():
    """
    Handle incoming webhook requests.
    """
    result = receptionist.handle_conversation()
    
     #if user said exit
    if result["status"] == "exit":
        receptionist.clear()
    return result