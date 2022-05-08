from typing import Optional
from pydantic import BaseModel
                     
class Client(BaseModel):
    username:str
    sdk_version:Optional[str]
    session_id:Optional[str]
    platform:Optional[str]
    country_code:Optional[int] 
    class Config():
        orm_mode = True 
        
        