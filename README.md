# CrashChannel - A CalgaryHacks 2019 Project

CrashChannel is a tool that aims to help users, city planners, and first responders make smarter decisions about traffic intersections. Using the [City of Calgary's open data] (https://data.calgary.ca/Transportation-Transit/Traffic-Cameras/k7p9-kppz), CrashChannel looks at the image feed of each traffic camera in the City of Calgary, runs it through our machine learning model, and detects whether or not a crash has occurred.

The project uses:
* Vue.js for a front end that shows an interactive map of each traffic camera in the city and the current status of whether or not there is a crash there.
* Python with Tensorflow and Flask for the REST API that takes in image links, runs the image through our model, and responds with whether or not the image contains a car crash.
* Google Cloud Firestore for the database, to keep track of each traffic camera.

## Contributing/Running
* Go into the `frontend` folder and run `npm install` to install the needed npm packages, then run `npm run serve` to start the Vue app.
* Go into the `image_training` folder, and run `python app.py`. Note, there are a bunch of packages in there that you'll need to install with pip, such as `Tensorflow` and `Flask`, but if the command line returns an error saying that something is missing, please install that, too.

Special thanks to my teammates, Anton Santos, Stanton Thai, Jeremy Olea, and Kevin Ta.
