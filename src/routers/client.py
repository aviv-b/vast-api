from fastapi import APIRouter, Depends,status
from src.database import SessionLocal as Session, get_db
import src.schemas as schemas
import src.models as models
import src.config as config
import httpx

router = APIRouter(
    tags=["Client"]
)


@router.post("/getads")
async def get_ads( request: schemas.Client , db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        response = await client.get(config.API_ADS)
        
    if response.status_code == status.HTTP_200_OK:
        client = db.query(models.Client).\
                filter(models.Client.username == request.username ).\
                first()
        # add
        if client is None:
            new = models.Client(username = request.username , ads = 1 )
            db.add(new)
            db.commit()     
            return {"operation": "added" , "response":response.text}
        # update (+=1 will raise race condition)
        client.ads = client.ads + 1
        db.commit()        
    return {"status": response.status_code , "response":response.text}




@router.post("/impression")
def get_impression(request: schemas.Client, db: Session = Depends(get_db)):
    
        client = db.query(models.Client).\
                filter(models.Client.username == request.username ).\
                first()
        # add
        if client is None:
            new = models.Client(username = request.username , impression = 1 )
            db.add(new)
            db.commit()     
            return {"added"}
        
        #update 
        client.impressions  += 1
        db.commit()  
        return {"updated"}



@router.get("/getstats/{username}")
def get_stats( username:str ,db: Session = Depends(get_db)):
    client = db.query(models.Client).\
        filter(models.Client.username == username).\
        first()
    # calculate fill_rate to avoid divide by zero error
    if client is not None:
        fill_rate = 0 
        if client.ads > 0:
            fill_rate = client.impressions / client.ads
            
        return {"username": client.username, 
                "impression":client.impressions,
                "ads":client.ads, 
                "fill_rate": fill_rate}

@router.get("/all",)
def get_all_data( db: Session = Depends(get_db)):
    return db.query(models.Client).all()



  
    