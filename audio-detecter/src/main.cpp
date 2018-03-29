#include <iostream>
#include <poll.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
//#include <pulse/i18n.h>
#include <pulse/pulseaudio.h>
#include <pulse/rtclock.h>
#include <fstream>
#include "Alsa.h"
#include <glib.h>

using namespace std;
#define FD "/proc/asound/card1/pcm0p/sub0/status"
#define POLLING_INTERVAL 3

static int action = 0;
static bool isPlaying = false;

bool getPlayState(){
    ifstream f(FD);
    if( f.is_open()){
        string line;
        getline(f, line);
        size_t ret = line.find("closed");
        if(ret == string::npos)
            return true;
        else
            return false;
    } else
        cout << "failed to open file " << FD << endl;
}
void setWifiState(bool on) {
    cout << "setWifiState " << on << endl;
    if(on){
        system("mosquitto_pub -d  -t cmnd/sonoff/POWER -m 1");
    } else
        system("mosquitto_pub -d  -t cmnd/sonoff/POWER -m 0");
        
}
int monitoring(gpointer user_data) {
    if( isPlaying != getPlayState()){
        isPlaying = !isPlaying;
        cout << "Audio state = " << isPlaying << endl;
        setWifiState(isPlaying);
    }
    return 1;
}

int main(){
    cout<< "hello" << endl;
    GMainContext* context = g_main_context_new();
    GMainLoop* loop = g_main_loop_new(context, false);
    g_main_context_unref(context);
    GSource* source = g_timeout_source_new_seconds(POLLING_INTERVAL);
    g_source_set_callback(source, monitoring, nullptr, nullptr);
    g_source_attach(source, context);
    g_source_unref(source);
    g_main_loop_run(loop);
    g_main_loop_unref(loop);
    g_main_loop_unref(loop);
    cout << "Program terminated..." <<endl;

}

