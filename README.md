## Structure:
```
├── analysis
│   ├── jet_cfg.py
│   ├── output_test
│   │   └── utility
│   │       ├── cast_plot.py
│   │       ├── plot.py
│   │       └── roc.py
│   ├── tau_cfg.py
│   └── test
│       ├── classe.py
│       ├── configuration
│       │   ├── conf_builder.py
│       │   ├── configurations
│       │   │   └── configuration_0.py
│       │   ├── conf_list.txt
│       │   └── print_bash.py
│       ├── run.sh
│       └── test.py
├── basic
│   ├── description.md
│   ├── minimal_cfg.py
│   ├── MinimaltauAnalyzer.cc
│   └── README.md
└── mva
    ├── mva.py
    ├── parameter.py
    └── plotter.py
   ```
# basic
- Minimal code to access timing information inside the miniaod files. print the variable on the screen, does nothing
- Some info in the included .md fils

# analysis
- Code used to run the analysis
- Starting from the miniaod files create new root files and run on different configurations ( eta region, isolation cuts, time resolution)
    ## configuration    
    - basic tool to write the configurations files starting from the conf_list.txt 
    - for now 169 basic configuration are available that differs for DM selection, Eta and p_T range, timing resolution
    ##  output_test/utility
    - tools to plot the results ( ROC curves, correlation plots, efficiency and fakerate plots, ratio plots and so on)

# mva
- skeleton to run an MVA analysis using few parameters ( eta, pt, charged isolation and time gated charged isolation)
