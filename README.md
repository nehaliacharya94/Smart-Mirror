# Smart Mirror
_(Spring: January 2016 - May 2016)_

The idea of developing a **Smart Mirror** was to have the future in our homes. I wanted to make an everyday household item smarter along with Raspberry Pi and thus, I chose mirror for their wide use case and the future implications that it holds. Also, my aim was that instead of looking up the basic information which we usually have access to on our cell phones after waking up, we see all of it in our household mirror which will be more convenient, creative and fancy.

I used the following tools and devices for this project:
* Raspberry Pi 
* two-way mirror
* camera module
* Motion Sensor
* LCD Display
* Amazon AWS IoT
>
Raspberry Pi is connected to the LCD display. A two-way mirror is placed in front of the display and the part protruding outwards of the display is covered with a black paper. This is done to reflect the person standing in front of the mirror and a display is used to show the notifications. The set up is shown below.
>
<img width="406" alt="capture" src="https://user-images.githubusercontent.com/29523536/28006823-f1f96dd0-651e-11e7-9866-b9d3087cfba2.PNG">

The motion sensor senses motion and sends this data to the raspberry pi for processing. The raspberry pi will then send a signal to switch on the display. The sensor information will be published to the Amazon Web Services (AWS) IoT where AWS will process the data and store it in Dynamo DB. Through the raspberry pi, the user can switch on or switch off the camera. Also, once an image is captured using the camera module, the images are uploaded to the Dropbox and deleted from the local file system.
>
<img width="404" alt="capture1" src="https://user-images.githubusercontent.com/29523536/28006901-4913dbbe-651f-11e7-9db9-7d43c747c4be.PNG">

I developed a web page using Bootstrap and CSS. The web page comprised of APIs elements like weather, date and time in the Midori browser that was downloaded first and then made the default browser. 

The motion sensor I used was very slow. So I created a new circuit with registers so that the output of the motion sensor is immediately sent to the raspberry pi and the it will immediately switch on the monitor. The monitor will be hosting the midori app. 

Raspberry pi has a component called HDMI in. When the value is __“1″__, it senses on the display else the value is __“0″__ and the display remains switched off. When the system loads up it is usually __“0″__ but when I want the display to turn on the HDMI in value is made __“1″__. So when a motion is detected, the value is made __“1″__ and after 5 seconds it should again go back to __“0″__ i.e. the monitor switches off. 

The value of __“1″__ will be updated to the AWS Iot server and the values are stored as metrics in Dynamo DB. The published entries are shown below.
>
<img width="405" alt="capture3" src="https://user-images.githubusercontent.com/29523536/28007017-c96e015e-651f-11e7-9756-9613450ec6c6.PNG">


