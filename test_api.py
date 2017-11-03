import cmapPy
import pdb

base_url='https://api.clue.io/api'
user_key='24092bd44c6aa36bc21ae81191c81cf3'
r = 'perts'
w = {}
f = {}

pdb.set_trace()
a = cmapPy.clue_api_client.ClueApiClient(base_url=base_url,user_key=user_key)
r = a.run_filter_query(r, f)
natee=0
