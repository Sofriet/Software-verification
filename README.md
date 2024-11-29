# Software-verification 2023 (at Radboud)
## Elevator model
Created a NuSMV (https://nusmv.fbk.eu/) elevator simulation (elevator.smv)
<br> with Daniël Schenk <br>
Feedback:<br>
- 2pts for the basic requirements.
- 1pt for the additional requirement, note that 5 and 7 are exactly the same, so I have only given points for one of the two.
- 2.5pts for the NuSMV model. This is a nice, conscise model, good job!
- 2pts for additional features: distinguishing between up/down requests and elevator moves in a direction until reaching the requested floor.
- 2pts for all requirements being successfully checked.
- 0.5pts for an elevator with 7 floors.
<br><br>Total 10/12 points
<br><br>
## Simplified SVFuzzer
Created a simplified version of AFL – SVFuzzer (SVFuzzer folder) <br>
Feedback:
- Mutator: we would like to also use the extended ASCII characters (up to char 255)
- Coverage: instead of putting all covered lines in a list, you could also get the previous line from the frame object to get the line pair
- SVFuzzer: you should check if an inputs coverage is not a subset of the total coverage.






