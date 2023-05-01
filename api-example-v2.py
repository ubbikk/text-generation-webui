import requests

# For local streaming, the websockets are hosted without ssl - http://
HOST = '0.0.0.0:5000'
URI = f'http://{HOST}/api/v1/generate'

# For reverse-proxied streaming, the remote will likely host with ssl - https://
# URI = 'https://your-uri-here.trycloudflare.com/api/v1/generate'

def run(prompt):
    request = {
        'prompt': prompt,
        'max_new_tokens': 2000,
        'do_sample': True,
        'temperature': 0.7,
        'top_p': 0.1,
        'typical_p': 1,
        'repetition_penalty': 1.18,
        'top_k': 40,
        'min_length': 40,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'skip_special_tokens': True,
        'stopping_strings': []
    }

    response = requests.post(URI, json=request)

    if response.status_code == 200:
        result = response.json()['results'][0]['text']
        print(prompt + result)

if __name__ == '__main__':
    prompt = """You are a helpful assistant called Joi trained by OpenAssistant on large corpus of data, you will now help user to answer the question as concise as possible
User: Write 100 short, diverse, emotional comments about the following text. Don't use hashtags. The text:
"While Putin's spokesman urges not to trust reports of
new wave of mobilization, Russians are lured to the draft board by all possible
ways: social advertising with "nostalgic motives", and when
it became useless to press patriotism - with money, all kinds of bonuses,
new job prospects. That is, mobilization in Russia is no longer in waves,
and the constant is partial: there are no waves, it is a continuous process. among the people
a joke is already circulating: “you should not believe the rumors until they are refuted by Peskov.”
The Russians no longer know how to lure them to war. In the defense department
Russia said they launched a campaign across the country to raise popularity
military service among the population, the authorities are trying by any means to raise
"prestige" of this idea. The Ministry of Digital Transformation promises to book from
conscription to the army for IT specialists who returned to the Russian Federation. Stop. Why book?
if the mobilization is completed.
In the regions, there are vacancies in the military registration and enlistment offices for the distribution of subpoenas, and
companies are looking for specialists for mobilization accounting of employees. AT
military registration and enlistment offices have vacancies for heads and assistants of the department
planning and accounting of mobilized resources, doctors, assistants
Commissioner for "Manning the mobilization human and transport
resources." The question is why, if the authorities from all sides are shouting about the absence
mobilization plans. Officially announce a new wave of mobilization
unlikely to be, and why, if you can massively send summonses without any
ads. Well how are you guys, ready to die for the power that sends on
slaughter and at the same time still brazenly lying? Such is the artificial selection: the first
the law-abiding will die.
So, in Donetsk Makiivka, men who got a job in a mine immediately
mobilize. The management of the mine transmits to the military registration and enlistment offices data on new
employees who were previously lured to work by high salaries.
When applying for a job, it is enough to provide complete information about yourself and
copies of documents, and at the exit a military commissar will already be waiting for you. ingenious
move, because it's easier to come to everything ready than to catch them somewhere.
"The motherland will look for you everywhere, son." So going to a new
work, do not forget to bring dry food and a black bag with you, and be ready
"acquire unforgettable experiences" in "large-scale
breathtaking manoeuvres."

Joi:"""
    run(prompt)
