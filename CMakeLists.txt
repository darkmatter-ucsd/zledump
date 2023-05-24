cmake_minimum_required(VERSION 3.10 FATAL_ERROR)

if(UNIX AND NOT APPLE)
  add_definitions(-DLINUX)
endif()

project(ZLEDump)

file(GLOB sources ${PROJECT_SOURCE_DIR}/src/*.c)
file(GLOB headers ${PROJECT_SOURCE_DIR}/include/*.h)

# file(GLOB configurations ${PROJECT_SOURCE_DIR}/config/*.txt)
# file(COPY ${configurations} DESTINATION ${PROJECT_BINARY_DIR})

add_executable(zle_exe src/WaveDump.c ${sources})
target_include_directories(zle_exe PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# add_compile_options(-lm)
target_link_libraries(zle_exe m)
# target_link_libraries(zle_exe chrono)
target_link_libraries(zle_exe CAENDigitizer)
target_link_libraries(zle_exe CAENComm)
# target_link_libraries(zle_exe CAENVMELib)

add_custom_target(ZLEDump DEPENDS zle_exe)
target_compile_features(zle_exe PRIVATE cxx_std_17)