# SSY340_project_pong
In this project there has been 3 different versions of agents trained and 1 base "hard-coded" version and is an extension of the already existing version done 3 years previously, https://github.com/xinghai-sun/deep-rl/blob/master/docs/selfplay_pong.md    
The 3 different are one A3C agent trained only against the base agent. Then there is a self-play agent who has been trained both against the A3Cs best version and against itself after that. Lastly there has also been a continued self-play agent with some power-ups implemented.  
  
The three different versions can be seen in gifs here where they combat eachother, for more videos go into the folders ending with "-Monitoring" in the repository where you can find mp4 files for different checkpoints.  

Games from Table 1:
<p align="left">
  <img src=gifs/A3C0-vs-builtin.gif hspace = "50">
  <img src=gifs/A3C500-vs-builtin.gif hspace = "50">
  <img src=gifs/A3C1000-vs-builtin.gif hspace = "50">
  <pre>
   A3C-version 0 VS Built in       A3C-version 500 VS Built in        A3C-version 1000 VS Built in
  </pre>
</p>
