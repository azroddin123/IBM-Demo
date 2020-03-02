

import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('2mf1h2QTahDrShaRENsZ5o6k5vl2YJrC_O51cHQMwniC')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)
speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/5c4589f7-b60c-41c3-8515-305e7b93583e')
import sys


# filename = "/home/azhar/Downloads/audio-file2.flac"

json_data = []
text_data = []
filename = sys.argv[-1]
# number = sys.argv[3]
# # print(len(sys.argv))
# # print(sys.argv[3])
# print(number)
print(filename)

def speech_to(filename) :
    with open(join(dirname(__file__),filename),
                'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/flac',
            word_alternatives_threshold=0.9,
        
        ).get_result()


        text_data.append(speech_recognition_results)
        json_data.append(json.dumps(speech_recognition_results, indent=2))
       
        # if rtype == 'text' :
        #     print(speech_recognition_results)
        # else :
        #     print(json.dumps(speech_recognition_results, indent=2))


speech_to(filename);

n = int(input("Enter Result : 1 : JSON  2.Text  \n "))

if n==2 :
    print(text_data)
elif  n==1 :
    print(json_data)