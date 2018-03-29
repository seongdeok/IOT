#include "Pulse.h"
#include <iostream>

using namespace std;

Pulse::Pulse(){

}

Pulse::~Pulse(){

}

void Pulse::my_subscription_callback(pa_context *c, pa_subscription_event_type_t t,
                                      uint32_t idx, void *userdata) {
    cout << "call back !!! " << t << endl;
    if ((t & PA_SUBSCRIPTION_EVENT_TYPE_MASK) == PA_SUBSCRIPTION_EVENT_CHANGE) {
        cout << "event change " << endl;
//        if( getPlayState())
//            cout << "Music is playing" << endl;
//        else
//            cout << "No Sound " << endl;
    } 
}

void Pulse::context_state_callback(pa_context* c, void* userdata){
    cout << "state call back" << pa_context_get_state(c) << endl;
    if( pa_context_get_state(c) == PA_CONTEXT_READY){
        
        pa_context_set_subscribe_callback(c, my_subscription_callback, nullptr);
        //pa_context_subscribe(c, PA_SUBSCRIPTION_MASK_SINK_INPUT, NULL,NULL);
        pa_context_subscribe(c, PA_SUBSCRIPTION_MASK_SINK, NULL,NULL);
        cout << "register call back" << endl;
    }
}

void Pulse::monitor(){
    int ret = 0;
    pa_mainloop* m = nullptr;

    pa_proplist* proplist = pa_proplist_new();
    if(!(m = pa_mainloop_new()))
        cout << "mainloop failed" << endl;
    pa_mainloop_api* mainloop_api = pa_mainloop_get_api(m);
    pa_context* context = nullptr;
    if(!(context = pa_context_new_with_proplist(mainloop_api, NULL, proplist)))
        cout << "context new failed" << endl;
    
    
    pa_context_set_state_callback(context, context_state_callback, NULL);

    if( pa_context_connect(context, nullptr, PA_CONTEXT_NOFLAGS , NULL) < 0)
        cout << "connect failed" << endl;

    
    cout << "start main loop " << endl;
    if(pa_mainloop_run(m, &ret) < 0)
        cout << "mainloop run failed" << endl;
    cout<< "hello" << endl;
}

