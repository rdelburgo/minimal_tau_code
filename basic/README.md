# minimal_tau_code 
minimal code to access tau timing info ( some library may be optional)
this code allow to access the timing information in the miniAOD files and print out some parameters like pt, eta, dz and time.
you can run it on CMSSW 9_3_2 with
cmsenv
>> scram b
>> cmsRun minimal_cfg.py

THIS CODE DO NOT CREATE A ROOT FILE, IT JUST PRINT THE INFORMATION ON THE TERMINAL

something on the units:
dz is in CENTIMETER (10 mm)
time or dtime are in NANOSECONDS
example of the print out:
```
Tau number: 0
Leading Hadron pt, eta, phi, time:  3.37891 0.52736 -2.80927-0.0538823
pt, eta, phi:  29.7411 0.537622 -2.78439
decay mode: 11
starting loop in packed candidate 

there are 2 signal candidates
pt, eta, phi, dz, time: 3.37891 0.52736 -2.80927 -0.00304199 -0.0538823
pt, eta, phi, dz, time: 2.77539 0.505387 -2.72743 -0.00392822 -0.00702813
there are 5 isolation candidates
pt, eta, phi, dz, time: 6.56641 0.613239 -2.81669 -0.00354492 -0.0491969
pt, eta, phi, dz, time: 3.76758 0.661214 -2.82284 -0.00280273 -0.0299867
pt, eta, phi, dz, time: 2.60156 0.405408 -2.84774 -0.000748901 -0.0215529
pt, eta, phi, dz, time: 2.26758 0.711386 -2.32194 0.00611816 -0.00327979
pt, eta, phi, dz, time: 1.08887 0.382336 -2.31696 0.0416406 0.00749667
Tau number: 1
```
the time information is retrieved in the lines:
```
pat::PackedCandidate const* tempIsoCand = dynamic_cast<pat::PackedCandidate const*>(cand.get());
  double time = timetempIsoCand->dtime(0);
```
more info available at [cmssdt lxr](https://cmssdt.cern.ch/lxr/source/DataFormats/PatCandidates/interface/PackedCandidate.h?v=CMSSW_9_3_3)

* time and dtime had always the same value in the miniAOD that I used
* this is the absolute time of arrival corrected by the time of flight ( so the time at which che particle is created)
* you want to compare this time with the time of the vertex, or the leading pt tau signal candidate, is up to you

* **if the time is 0** it means the particle has no time information ( it was neutral, out of acceptance or the timing layer was inefficient)
