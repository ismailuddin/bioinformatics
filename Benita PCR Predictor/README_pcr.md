Benita PCR predictor
==============

A script to predict the probability of PCR success based on parameters determined by Benita et. al (2003), written in Ruby.

**Prerequisites** <br>
<ul type="circle">
<li>FASTA formatted file with three entries. First being the template DNA, remaining being the forward and reverse primers in any order.</li>
<li>BioRuby module to parse FASTA file, and calculate GC content.</li>
<li> Ruby v1.9.3</li>
</ul>

**Usage**<br>
Run the script from your desired terminal. On Windows, navigate to directory containing the script, and type ```<<RUBY PATH>> Benita_PCR_Predictor.rb <<A>>```. Replace ```<<PATH>>``` with the path for your Ruby installation (typically ```C:\Ruby193\bin\ruby.exe```), and ```<<A>>``` with the path for your .FASTA file (must be within the same directory, e.g. ```DENV1.fasta```)

**Operation**<br>
This script is based upon the mathematical model derived by Benita et. al (2003). The template DNA sequence is analysed using a sliding GC window of window length 21, and stepping value of 1. The resulting graph is integrated above the threshold value of 65%, to yield the area under the graph. Using this data, and other parameters set out in the referenced paper, the probability of PCR success is calculated. The variables within the equation are also independently calculated and printed out in the terminal for independent verification.
