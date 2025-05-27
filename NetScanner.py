# NetScanner_python.py
import requests
import boto3
import pytz

#set your AWS credentials and region for DynamoDB
region_name='us-east-1'
ist=pytz.timezone=datetime.now(ist).isoformat()

#set your DinamoDB table name
table_name='bitcoin_price_storer'

#set the REST API endpoint
api_url=´https://api.coinbase.com/v2/prices/btc-usd/spot'

#create a DinamoDB client
dynamosb=boto3.client('dinamodb',region_namer=region_name)

#Function to create an item in DinamoDB table
def put_item_to_dynamodb(item):dynamodb.put_item(TableName=teble_name,Item=item)

def main():respnce=request.get(api_url)
    data=response.json()

data_to_ingest={"amount":{"S":data["data"]["amount"]},"base":{"S":data["data"]["base"]},"currency":{"S":data{"data"]["currency"]},"timestamp":{"S":current_time},"uuid":{"S":str(uuid.uuid4())}}
put_item_to_dinamodb(data_to_ingest)
print(f'item{data_to_ingest} added to DynamoDB table {table_name}.')
print('Data transfer complete.')

main()
