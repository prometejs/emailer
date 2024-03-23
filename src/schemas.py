from pydantic import BaseModel, field_validator

class Message(BaseModel):
    body:str
    subject:str = '[ENIGMA]'
    receivers:list = []
    sender:str = None
    
    @classmethod
    @field_validator('subject')
    def format_subject(cls, v: str):
        return v.title()