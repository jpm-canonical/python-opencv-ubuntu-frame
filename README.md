# Python OpenCV example on Ubuntu Frame

```
snapcraft -v debug
sudo snap install --dangerous ./python-ui-frame_0.0.1_amd64.snap
sudo snap connect python-ui-frame:wayland
```

This works:
```
frame-it python-ui-frame.iot-example-graphical-snap
```

This fails:
```
frame-it python-ui-frame
```

Error:
```
[2024-07-18 15:53:01.974116] <information> mirserver: Sending display configuration to session :
qt.qpa.xcb: could not connect to display 
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/snap/python-ui-frame/x10/lib/python3.10/site-packages/cv2/qt/plugins" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.

/snap/frame-it/18/frame-it: line 35: 2453408 Aborted                 (core dumped) WAYLAND_DISPLAY="${wayland_display}" SDL_VIDEODRIVER=wayland QT_QPA_PLATFORM=wayland GDK_BACKEND=wayland $@
[2024-07-18 15:53:03.112214] < - debug - > mirserver: Handling Terminated from pid=2453307
[2024-07-18 15:53:03.112398] < -warning- > mirserver: wl_surface@12 destroyed before associated role
```