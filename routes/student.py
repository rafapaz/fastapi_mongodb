
import json
from fastapi import APIRouter
from config.database import dbobj
from commom import *

student_router = APIRouter()

@student_router.get('/hello')
async def hello():
    return 'Hello World'

@student_router.get('/students')
async def find_all_students():
    return convertIdMongo(dbobj['student'].find())

@student_router.post('/student_add')
async def create_student(student):
    return convertIdMongo(dbobj['student'].insert_one(json.loads(student)))
