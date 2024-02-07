from pydantic import BaseModel, field_validator
from typing import Optional

class Message(BaseModel):
    body:str
    subject:str = '[ENIGMA]: No Subject'
    receivers:list = []
    
    @classmethod
    @field_validator('subject')
    def format_subject(cls, v: str):
        return v.title()