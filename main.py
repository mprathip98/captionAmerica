import pvcheetah

cheetah = pvcheetah.create(access_key='${/EptENU0fNeCoqIh7OBfHlSQdfnemRqP1cviLlQWGG1MqawrMKNXwQ==}')

def get_next_audio_frame():
    pass

while True:
    partial_transcript, is_endpoint = cheetah.process(get_next_audio_frame())
    if is_endpoint:
        final_transcript = cheetah.flush()
