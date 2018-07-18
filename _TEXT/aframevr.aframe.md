a frame a web framework for building virtual reality experiences site — docs — school — slack — blog examples find more examples on the homepage a week of a frame and webvr directory features eyeglasses virtual reality made simple a frame handles the 3d and webvr boilerplate required to get running across platforms including mobile desktop vive and rift just by dropping in a scene heart declarative html html is easy to read and copy and paste since a frame can be used from html a frame is accessible to everyone web developers vr enthusiasts educators artists makers kids electric plug entity component architecture a frame is a powerful framework on top of three js providing a declarative composable reusable entity component structure for three js while a frame can be used from html developers have unlimited access to javascript dom apis three js webvr and webgl zap performance a frame is a thin framework on top of three js although a frame uses the dom a frame does not touch the browser layout engine performance is a top priority being battle tested on highly interactive webvr experiences globe with meridians cross platform build vr applications for vive rift daydream gearvr and cardboard dont have a headset or controllers no problem a frame still works on standard desktop and smartphones mag visual inspector a frame provides a built in visual 3d inspector with a workflow similar to a browsers developer tools and interface similar to unity open up any a frame scene and hit ctrl alt i runner features hit the ground running with a frames built in components such as geometries materials lights animations models raycasters shadows positional audio tracked controllers get even further with community components such as particle systems physics multiuser oceans mountains speech recognition or teleportation usage example build vr scenes in the browser with just a few lines of html to start playing and publishing now remix the starter example on glitch html html head script src https aframe io releases 0 8 2 aframe min js script head body a scene a box position 1 0 5 3 rotation 0 45 0 color 4cc3d9 a box a sphere position 0 1 25 5 radius 1 25 color ef2d5e a sphere a cylinder position 1 0 75 3 radius 0 5 height 1 5 color ffc65d a cylinder a plane position 0 0 4 rotation 90 0 0 width 4 height 4 color 7bc8a4 a plane a sky color ececec a sky a scene body html with a frames entity component architecture we can drop in community components from the ecosystem e g ocean physics and plug them into our objects straight from html html a entity id sphere geometry primitive sphere material color efefef shader flat position 0 0 15 5 light type point intensity 5 animation property position easing easeinoutquad dir alternate dur 1000 to 0 0 10 5 loop true a entity a entity id ocean ocean density 20 width 50 depth 50 speed 4 material color 9ce3f9 opacity 0 75 metalness 0 roughness 1 rotation 90 0 0 a entity a entity id sky geometry primitive sphere radius 5000 material shader gradient topcolor 235 235 245 bottomcolor 185 185 210 scale 1 1 1 a entity a entity id light light type ambient color 888 a entity a scene builds to use the latest stable build of a frame include aframe min js js head script src https aframe io releases 0 8 2 aframe min js script head to check out the stable and master builds see the dist folder npm sh npm install save aframe or yarn add aframe js require aframe e g with browserify or webpack local development sh git clone https github com aframevr aframe git clone the repository cd aframe npm install install dependencies npm start start the local development server and open in your browser http localhost 9000 generating builds sh npm run dist questions for questions and support ask on stackoverflow stay in touch to hang out with the community join the a frame slack follow a week of a frame on the a frame blog follow aframevr on twitter contributing get involved check out the contributing guide for how to get started license this program is free software and is distributed under an mit license