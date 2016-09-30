Stage 1 Ntuplizer
=================

This repository contains programs used to make necessary stage 1 ntuples on CERN's lxplus

Installation
============

This program has been tested with CMSSW_7_4_2. To use this program, obtain this CMSSW release and move into the source directory.

    cmsrel CMSSW_8_0_2
    cd CMSSW_8_0_2
    cd src
    cmsenv
  
Then, clone this git repository and compile CMSSW

    git clone https://github.com/bregnery/UfHMuMuCode.git
    scram b
    cmsenv

Instructions
============

First, source the .bash_profile in bregnery/Settings/lxplus. Then, set up the CRAB environment and obtain a proxy.

    cd CMSSW_8_0_2/src/UfHMuMuCode/UFDiMuonsAnalyzer/test
    cmsenv
    CRAB
    vprox

Now, check that the CRAB environment is working properly.

    crab --version

Next, add file names and DAS directories to Samples_v3.py and create the CRAB submit scripts.

    python make_crab_script.py

Finally, submit the CRAB jobs, check status, and clean the directory.

    ./crabsubmitall
    ./crabstatusall
    ./crabcleansubmit
`
