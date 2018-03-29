#ifndef PULSE_H
#define PULSE_H

#include<pulse/pulseaudio.h>

class Pulse{
public :
    Pulse();
    ~Pulse();
    static void my_subscription_callback(pa_context *c, pa_subscription_event_type_t t, uint32_t idx, void *userdata);
    static  void context_state_callback(pa_context* c, void* userdata);
    void monitor();

};

#endif

