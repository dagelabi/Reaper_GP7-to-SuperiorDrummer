import reapy
project = reapy.Project()

instrument_groups =     {
                          "35" : 'Snare'
                        }

midi_item = project.import_media("D:/Documents/DAW/Reaper/API/Reapy/04_Call-of-the-Void_Drums_GP6-v2.mid")
midi_track = midi_item.track
#select the new item
project.select_item(midi_item, makeUnique=True)

#explode action ID 40920
project.perform_action(40920)

#get child tracks ----------------------------------------------------------
n_track_left    = project.n_tracks - midi_track.index
last_track_id   = n_track_left+midi_track.index
new_track_id    = midi_track.index

child_tracks    = []
for track_id in range(last_track_id, new_track_id+1, -1):
    track = project.tracks[track_id-1]
    if new_track_id == track.parent_track.index :
        child_tracks.insert(0,track)
#---------------------------------------------------------------------------

#get note CC
for t in child_tracks:
    CC_note = t.items[0].takes[0].notes[0].pitch    