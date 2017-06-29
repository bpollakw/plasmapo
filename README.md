# plasmapo
Pseudocode plasmid map generator using SBOL visual standards

## Intro

This app was generated using the awesome AngularPlasmid (http://angularplasmid.vixis.com) library, and a lot of reused code from Mihails Delmans in LoopDB (https://github.com/HaseloffLab/LoopDB). 

The purpose of its development was for simplifying the making of vector graphics plasmid maps for my PhD thesis, and maintaining feature size and illustration consistency in circular plasmids.

First, its extremely alpha stage and has several constraints. However, it will be useful for consistent for plasmid maps up to 10 transcriptional units or so with relative simplicity by writing pseudocode, inspired by Pigeon (http://pigeoncad.org).

### Constraints
The plasmid size is set for avoiding trouble with adaptive graphics. AngularPlasmid does not incorporate SBOL visual standards, thus they had to be "drawn" in a very primitive way.
The maximum ammount of plasmid features that can be drawn is about 30 (10 transcriptional units), but this may be enough for most current uses in plasmid construction.
Colour schemes are set but can be changes in the javascript.
The code is horribly put together, since I'm in the process of thesis write up, I cannot spare the time to make this better. Nevertheless, with a bit of JS and HTML you can probably fix the mess (and hopefully pull request!).

### Requirements
Most of them are python libraries, which probably can be found through pip. 

- Flask
- other Flask dependencies that you'll probably find out when trying to run the server.


Clone the repo and then just do:

```
python server.py

```

And if you meet the requirements you should be alright. Go to localhost:8080 in your browser and start playing.


MIT license for attribution.
Bernardo Pollak
