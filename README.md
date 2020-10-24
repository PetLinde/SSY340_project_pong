# SSY340_project_pong
In this project there has been 3 different versions of agents trained and 1 base "hard-coded" version and is an extension of the already existing version done 3 years previously, https://github.com/xinghai-sun/deep-rl/blob/master/docs/selfplay_pong.md    
The 3 different are one A3C agent trained only against the base agent. Then there is a self-play agent who has been trained both against the A3Cs best version and against itself after that. Lastly there has also been a continued self-play agent with some power-ups implemented.  
  
The three different versions can be seen in gifs here where they combat eachother, for more videos go into the folders ending with "-Monitoring" in the repository where you can find mp4 files for different checkpoints.  

Games from Table 1:
<p align="center">
  <img src=gifs/A3C0-vs-builtin.gif hspace = "50">
  <img src=gifs/A3C500-vs-builtin.gif hspace = "50">
  <img src=gifs/A3C1000-vs-builtin.gif hspace = "50">
  <pre>
              A3C-version 0 VS Built in         A3C-version 500 VS Built in          A3C-version 1000 VS Built in
  </pre>
</p>
<p align="center">
  <img src=gifs/A3C3000-vs-builtin.gif hspace = "50">
  <img src=gifs/A3C5000-vs-builtin.gif hspace = "50">
  <img src=gifs/A3C9000-vs-builtin.gif hspace = "50">
  <pre>
            A3C-version 3000 VS Built in        A3C-version 5000 VS Built in        A3C-version 10000 VS Built in
  </pre>
</p>
  
  
Games from Table 2:
<p align="center">
  <img src=gifs/Selfplay100-vs-builtin.gif hspace = "50">
  <img src=gifs/Selfplay3000-vs-builtin.gif hspace = "50">
  <pre>
                               Selfplay 100 VS Built in            Selfplay 3000 VS Built in
  </pre>
</p>
<p align="center">
  <img src=gifs/Selfplay100-vs-A3C1000.gif hspace = "50">
  <img src=gifs/Selfplay100-vs-A3C5000.gif hspace = "50">
  <img src=gifs/Selfplay3000-vs-A3C10000.gif hspace = "50">
  <pre>
              Selfplay 100 VS A3C1000             Selfplay 100 VS A3C5000            Selfplay 3000 VS A3C10000
  </pre>
</p>
<p align="center">
  <img src=gifs/Selfplay1100-vs-selfplay100.gif hspace = "50">
  <img src=gifs/Selfplay1100-vs-selfplay1000.gif hspace = "50">
  <img src=gifs/Selfplay3000-vs-selfplay1000.gif hspace = "50">
  <pre>
           Selfplay 1100 VS Selfplay 100       Selfplay 1100 VS Selfplay 1000      Selfplay 3000 VS Selfplay 1000
  </pre>
</p>
  
  
Games from Table 3:
<p align="center">
  <img src=gifs/powerup1000-vs-builtin.gif hspace = "50">
  <img src=gifs/powerup1000-vs-A3C10000.gif hspace = "50">
  <img src=gifs/powerup1000-vs-selfplay3000.gif hspace = "50">
  <pre>
              Powerup 1000 VS Built-in           Powerup 1000 VS A3C10000            Powerup 1000 VS Selfplay 3000
  </pre>
</p>

