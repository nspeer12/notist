import time
import threading
import multiprocessing
import time
from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from typing import Optional
import requests
import json
import os
from settings import *
from assistant import *


app = FastAPI()
templates = Jinja2Templates(directory="templates")

dex = DexterCloud(debug=True)


class QueryLog(BaseModel):
	input: str
	detection: str
	response: Optional[str]



@app.get('/')
def index(request:Request, query: Optional[str] = None):

	try:
		ans = None
		if query:
			print(query)
			ans = dex.process_input(query)
			print(ans)

		return templates.TemplateResponse('index.html', {"request": request, "ans": ans})
	except Exception as ex:
		return ex


@app.get('/api/')
async def fulfillment(query:str):
	print(query)
	
	try:

		if query:
			print(query)
			res = dex.process_input(query)
			print(res)
			return res
		else:
			return '400'
	except Exception as ex:
		return ex

@app.post('/log-query/')
async def log_query(query: QueryLog):
	print(query)
	with open('logs/query-log.csv', 'a') as f:
		f.write(query.input + ',' + query.detection + ',' + query.response + '\n')
		f.close()
	
	return '400'