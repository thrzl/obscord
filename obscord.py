import obspython as obs
from pypresence import Presence
import datetime

rpc = Presence("831576935863812146")
rpc.connect()
rpc.update(state="Idling", large_image='obs_studio')

def script_description():
    return "OBS RPC for Discord!"

def obs_event(event):
    if event == obs.OBS_FRONTEND_EVENT_EXIT:
        rpc.clear()
        rpc.close()
        return
    key = None
    message = "Idling"
    scene = obs.obs_frontend_get_current_scene()
    if obs.obs_frontend_streaming_active():
        key = 'play_button'
        message = "Streaming"
    if obs.obs_frontend_recording_active():
        key = 'record'
        message = "Recording"
    if obs.obs_frontend_recording_active() and obs.obs_frontend_streaming_active():
        message = "Streaming and Recording"
    rpc.update(state=message, start=None if message == "Idling" else datetime.datetime.now().timestamp(), small_image=key, large_image='obs_studio')

obs.obs_frontend_add_event_callback(obs_event)