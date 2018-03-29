#ifndef AUDIO_DETECTER_ALSA_H
#define AUDIO_DETECTER_ALSA_H

#include <alsa/asoundlib.h>

class Alsa {
public:
    Alsa();
    virtual ~Alsa();

    int open_ctl(const char *name, snd_ctl_t **ctlp);
    int monitor(const char *name);
    int print_event(int card, snd_ctl_t *ctl);


};

#endif

