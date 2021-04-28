import os
import requests
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'en-us'),
    lm=os.path.join(model_path, 'en-us.lm.bin'),
    dic=os.path.join(model_path, 'cmudict-en-us.dict')
)

for phrase in speech:
    print(str(phrase))
    if str(phrase) == "man":
        # importing the requests library
        print("OLI MIES")
        # api-endpoint
        URL = "http://localhost:8080"
        
        # location given here
        id = "Raspi 4 - makkara"
        
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'address':id}
        
        # sending get request and saving the response as response object
        r = requests.get(url = URL, params = PARAMS)
        
 