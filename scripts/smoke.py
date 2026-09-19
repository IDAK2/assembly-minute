import json,secrets,time
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
R=Path(__file__).parents[1];E=(R.parents[3]/'accounts.env').read_text();v=lambda n:next(x.split('=',1)[1].strip().strip('"').strip("'") for x in E.splitlines() if x.startswith(n+'='));secretary=create_account(account_private_key=v('ACCOUNT_7_GENLAYER_PRIVATE_KEY'));reviewer=create_account(account_private_key='0x'+secrets.token_hex(32));cs=create_client(chain=studionet,account=secretary);cr=create_client(chain=studionet,account=reviewer);addr='0x9A6D39019438c22E32B721eDf90b9C7E08CdA115';rid='LIVE-'+str(int(time.time()));commit='4e4cae3';minute=f'https://raw.githubusercontent.com/IDAK2/assembly-minute/{commit}/evidence/minute.txt';objection=f'https://cdn.jsdelivr.net/gh/IDAK2/assembly-minute@{commit}/evidence/objection.txt';tx=[]
def send(client,fn,args):
 h=client.write_contract(address=addr,function_name=fn,args=args);r=client.wait_for_transaction_receipt(transaction_hash=h,status='FINALIZED',retries=180,interval=5000);assert r.get('status_name')=='FINALIZED';tx.append(h)
send(cs,'open_motion',[rid,reviewer.address,'Adopt the watershed maintenance budget.']);send(cs,'adopt',[rid,'Passed 8-2',['North Ward reserved on implementation timing'],'Treasurer']);send(cs,'publish',[rid,minute]);send(cs,'object_minute',[rid,objection]);send(cr,'reconcile',[rid,'https://github.com/IDAK2/assembly-minute/raw/'+commit+'/evidence/minute.txt']);print(json.dumps({'id':rid,'state':'RECONCILED','transactions':tx}),flush=True)
