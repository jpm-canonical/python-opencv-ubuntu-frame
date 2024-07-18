# Python OpenCV example on Ubuntu Frame

This example snap packages a Python script that uses OpenCV to draw a GUI,
along with dependencies to make it work under Ubuntu Frame.

It is based on the [core22 glx gears](https://github.com/canonical/iot-example-graphical-snap/tree/22/x11-glxgears) example from Ubuntu Frame.  

Build the snap:

```
snapcraft -v debug
```

Install the snap:

```
sudo snap install --dangerous ./python-ui-frame_0.0.1_amd64.snap
```

Connect the wayland plug to allow drawing to the screen:

```
sudo snap connect python-ui-frame:wayland
```

Show the Python OpenCV QT5 GUI:

```
frame-it python-ui-frame
```

![python](media/frame-python-gui.png)

Show GLX Gears:

```
frame-it python-ui-frame.iot-example-graphical-snap
```

![python](media/frame-gears.png)
