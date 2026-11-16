# Software-verification 2023 (at Radboud)
## Elevator model
Created a NuSMV (https://nusmv.fbk.eu/) elevator simulation (elevator.smv)
<br> with Daniël Schenk <br>
Feedback:<br>
- Basic requirements met.
- Additional requirement met (note that 5 and 7 are exactly the same).
- NuSMV model: this is a nice, concise model, good job!
- Additional features: distinguishing between up/down requests and elevator moves in a direction until reaching the requested floor.
- All requirements successfully checked.
- Elevator with 7 floors.
<br><br>
## Simplified SVFuzzer
Created a simplified version of AFL – SVFuzzer (SVFuzzer folder) <br>
Feedback:
- Mutator: we would like to also use the extended ASCII characters (up to char 255)
- Coverage: instead of putting all covered lines in a list, you could also get the previous line from the frame object to get the line pair
- SVFuzzer: you should check if an inputs coverage is not a subset of the total coverage.






