from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr, ValidationError
from pydantic_core import ErrorDetails
from typing import List, Dict
from pathlib import Path

class Config(BaseSettings):
    '''
    all env vars read are prefixed with mail
    ''' 

    model_config = SettingsConfigDict(
        env_prefix='mail_',
        env_nested_delimiter=',',
        env_file='.env', # deprecated
        env_ignore_empty=True,
        env_file_encoding='utf-8',
        extra='ignore'
    )

    host: str = Field(frozen=True)
    user: SecretStr = Field(frozen=True)
    password: SecretStr = Field(frozen=True)
    sender: str = Field(default="admin@mail.com", frozen=True)
    port: int = Field(default=465, frozen=True)
    receivers: List[str] = Field(frozen=True)
    max_thread_count: int = Field(default=5, validation_alias='max_thread_count')

BASE_DIR = Path(__file__).parent
CUSTOM_MESSAGES = {
    'missing':'Field required, make sure the field is set in env and prefixed with `mail_`'
}

def convert_errors(e: ValidationError, custom_messages: Dict[str, str]) -> List[ErrorDetails]:
    new_errors: List[ErrorDetails] = []
    for error in e.errors():
        custom_message = custom_messages.get(error['type'])
        if custom_message:
            ctx = error.get('ctx')
            error['msg'] = ( custom_message.format(**ctx) if ctx else custom_message )
        new_errors.append(error)
    return new_errors

try:
    config = Config()
except ValidationError as e:
    print(convert_errors(e, CUSTOM_MESSAGES))
