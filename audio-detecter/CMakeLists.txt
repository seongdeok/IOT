cmake_minimum_required(VERSION 2.8.7)
project(audio-detecter)

include(FindPkgConfig)

pkg_check_modules(GLIB2 REQUIRED glib-2.0)
include_directories(${GLIB2_INCLUDE_DIRS})
link_directories(${GLIB2_LIBRARY_DIRS})

pkg_check_modules(PULSE REQUIRED libpulse)
include_directories(${PULSE_INCLUDE_DIRS})
link_directories(${PULSE_LIBRARY_DIRS})

pkg_check_modules(ALSA REQUIRED alsa)
include_directories(${ALSA_INCLUDE_DIRS})
link_directories(${ALSA_LIBRARY_DIRS})


file(GLOB_RECURSE SOURCES src/*)

set(BIN_NAME audio-detecter)
set(SRC_LIST ${SOURCES})

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${COMMON_FLAGS}")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${COMMON_FLAGS} -std=c++11")

add_executable(${BIN_NAME} ${SRC_LIST})

set_target_properties(${BIN_NAME} PROPERTIES LINKER_LANGUAGE CXX)
target_link_libraries(${BIN_NAME} ${GLIB2_LDFLAGS} ${PULSE_LDFLAGS} ${ALSA_LDFLAGS})

