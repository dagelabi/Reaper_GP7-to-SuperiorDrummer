class Instrument(object):
    def __init__(self, name, id, part_id):
        self._part_id       = part_id
        self._name          = name
        self._id            = id
        self.midi_channel   = None
        self._pitch         = None
        self._pan           = 0
        self._volume        = 80
        self._measures      = []
    
    def __str__(self) -> str:
        return f'<obj.Part.Instrument> {self._name} ({self._part_id}:{self._id})'
    def __repr__(self) -> str:
        return f'<obj.Part.Instrument> {self._name} ({self._part_id}:{self._id})'

    def link_beat(self, beat_obj):
        pass

    def link_measure(self, measure_obj):
        pass
    
    @property
    def part_id(self):
        return self._part_id

    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    @property
    def midiChannel(self):
        return self.midi_channel
    @midiChannel.setter
    def midiChannel(self, midi_channel):
        self.midi_channel = midi_channel
    
    @property
    def pitch(self):
        return self._pitch
    @pitch.setter
    def pitch(self, pitch):
        self._pitch = pitch
    
    @property
    def pan(self):
        return self._pan
    @pan.setter
    def pan(self, pan):
        self._pan = pan
    
    @property
    def volume(self):
        return self._volume
    @volume.setter
    def volume(self, volume):
        self._volume = volume 
    
    @property
    def measures(self):
        return self._measures