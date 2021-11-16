Open Source Python Packages in Hydrology
========================================
My attempt to list interesting open source python projects that can be used in the field of Hydrology. Suggestions as issues or pull requests are welcome!

UPDATE: The Pypa package authority has now added ["Hydrology" as a classifier](https://github.com/pypa/warehouse/issues/5728) so we can start [collecting python packages](https://pypi.org/search/?q=&o=&c=Topic+%3A%3A+Scientific%2FEngineering+%3A%3A+Hydrology) used by the hydrological community! If you are maintaining a python package, please add `Topic :: Scientific/Engineering :: Hydrology` to your setup.py so people can find your package.

R.A. Collenteur, University of Graz.

Hydrological Models
------------------
| Project Name | Description |
| ------- | ------ |
| [CMF](https://github.com/philippkraft/cmf) | Catchment Modelling Framework, a hydrologic modelling toolbox. |
| [TopoFlow](https://github.com/peckhams/topoflow) | Spatial hydrologic model (D8-based, fully BMI-compliant). |
| [VIC](https://github.com/UW-Hydro/VIC) | The Variable Infiltration Capacity (VIC) Macroscale Hydrologic Model. |
| [Xanthos](https://github.com/JGCRI/xanthos)| Xanthos is an open-source hydrologic model, written in Python, designed to quantify and analyze global water availability.|
| [WRF-Hydro](https://github.com/NCAR/wrf_hydro_py)| wrfhydrpy is a Python API for the WRF-Hydro modelling system. |
| [EXP-HYDRO](https://github.com/sopanpatil/exp-hydro) | EXP-HYDRO is a catchment scale hydrological model that operates at a daily time-step.  It takes as inputs the daily values of precipitation, air temperature, and potential evapotranspiration, and simulates daily streamflow at the catchment outlet. |
| [RRMPG](https://github.com/kratzert/RRMPG) | Rainfall-Runoff modelling playground. |
| [LHMP](https://github.com/hydrogo/LHMP) | Lumped Hydrological Models Playground. |
| [SMARTPy](https://github.com/ThibHlln/smartpy) | Python implementation of the rainfall-runoff model SMART |
| [PyStream](https://github.com/martibosch/pystream) | Python implementation of the STREAM hydrological rainfall-runoff model. |
| [HydrPy](https://github.com/hydpy-dev/hydpy) | A framework for the development and application of hydrological models based on Python. |
| [Catchmod](https://pypi.org/project/pycatchmod/) | CATCHMOD is widely used rainfall runoff model in the United Kingdom. It was introduced by Wilby (1994).|
| [wflow](https://github.com/openstreams/wflow) | wflow consists of a set of Python programs that can be run on the command line and perform hydrological simulations. The models are based on the PCRaster Python framework |
|[PyTOPKAPI](https://github.com/sahg/PyTOPKAPI)|PyTOPKAPI is a BSD licensed Python library implementing the TOPKAPI Hydrological model (Liu and Todini, 2002).|
|[mhmpy](https://github.com/MuellerSeb/mhmpy)|A Python-API for the mesoscale Hydrological Model.|
|[SuperflexPy](https://github.com/dalmo1991/superflexPy)|SuperflexPy: A new open source framework for building conceptual hydrological models |
|[NeuralHydrology](https://github.com/neuralhydrology/neuralhydrology)|Python library to train neural networks with a strong focus on hydrological applications.|
|[DRYP](https://github.com/AndresQuichimbo/DRYP)|Dryland Water Partition model.|
|[LuKars](https://github.com/dbittner87/LuKARS)|The LuKARS model is a lumped karst hydrological model to perform studies in karstic environments.|

Meteorological tools
--------------------
| Project Name | Description |
| ------- | ------ |
| [MetPy](https://github.com/Unidata/MetPy) | MetPy is a collection of tools in Python for reading, visualizing and performing calculations with weather data. |
| [PyEto](https://github.com/woodcrafty/PyETo) | PyETo is a Python library for calculating reference crop evapotranspiration (ETo), sometimes referred to as potential evapotranspiration (PET). The library provides numerous functions for estimating missing meteorological data. |
| [Improver](https://github.com/metoppv/improver) | IMPROVER is a library of algorithms for meteorological post-processing and verification. |
| [MetSim](https://github.com/UW-Hydro/MetSim) | MetSim is a meteorological simulator and forcing disaggregator for hydrologic modeling and climate applications. |
| [MELODIST](https://github.com/kristianfoerster/melodist)| MELODIST is an open-source toolbox written in Python for disaggregating daily meteorological time series to hourly time steps. |
| [PyCat](https://github.com/wegener-center/pyCAT) | Climate Analysis Tool written in python |
| [PySteps](https://github.com/pySTEPS/pysteps) | pySTEPS is a community-driven initiative for developing and maintaining an easy to use, modular, free and open source Python framework for short-term ensemble prediction systems. | 
| [Evaporation](https://github.com/openmeteo/evaporation) | Calculation of evaporation and transpiration. |
| [rainymotion](https://github.com/hydrogo/rainymotion) | Python library for radar-based precipitation nowcasting based on optical flow techniques.|
| [pyet](https://github.com/phydrus/pyet) | A python-package for calculating reference and potential evaporation. |

Unsaturated Zone
----------------
| Project Name | Description |
| ------- | ------ |
|[Pytesmo](https://github.com/TUW-GEO/pytesmo)|python Toolbox for the Evaluation of Soil Moisture Observations.|
|[Phydrus](https://github.com/phydrus/phydrus)|Python implementation of the HYDRUS-1D unsaturated zone model|

Groundwater 
-----------
| Project Name | Description |
| ------- | ------ |
| [Flopy](https://github.com/modflowpy/flopy) | The Python interface to MODFLOW. |
| [imod-python](https://imod.xyz/) | Make massive MODFLOW models. |
| [Idfpy](https://github.com/tomvansteijn/idfpy) | A simple module for reading and writing iMOD IDF files. IDF is a simple binary format used by the iMOD groundwater modelling software. |
| [WellApplication](https://github.com/utah-geological-survey/WellApplication) | Set of tools for groundwater level and water chemistry analysis. |
| [TIMML](https://github.com/mbakker7/timml) |  A Multi-Layer, Analytic Element Model. |
| [TTim](https://github.com/mbakker7/ttim) | A Multi-Layer, Transient, Analytic Element Model.  |
| [PyHELP](https://github.com/cgq-qgc/pyhelp) | A Python library for the assessment of spatially distributed groundwater recharge and hydrological components with HELP. |
| [PyRecharge](https://github.com/abdikaiym/pyrecharge)| Spatially distributed groundwater recharge and depletion modeling framework in Python|
| [Anaflow](https://github.com/GeoStat-Framework/AnaFlow)| A python-package containing analytical solutions for the groundwater flow equation|
|[WellTestPy](https://github.com/GeoStat-Framework/welltestpy)| A python-package for handling well based field campaigns.|
|[HydroGeoSines](https://github.com/HydroGeoSines/HydroGeoSines) |Signal In the Noise Exploration Software for Hydrogeological Datasets.|

Time Series (Analysis)
----------------------
| Project Name | Description |
| ------- | ------ |
| [Hydropy](https://github.com/stijnvanhoey/hydropy) | Analysis of hydrological oriented time series. |
| [Pastas](https://github.com/pastas/pastas) | Analysis of hydrological time series using time series models. |
| [Hydrostats](https://github.com/BYU-Hydroinformatics/Hydrostats) | Tools for use in comparison studies, specifically for use in the field of hydrology. |
|[htimeseries](https://github.com/openmeteo/htimeseries)| This module provides the HTimeseries class, which is a layer on top of pandas, offering a little more functionality.|

GIS Related
-----------
| Project Name | Description |
| ------- | ------ |
| [PcRaster](http://pcraster.geo.uu.nl/) | Is a collection of software targeted at the development and deployment of spatio-temporal environmental models. |
| [PyGeoprocessing](https://pypi.org/project/pygeoprocessing/) | a Python/Cython based library that provides a set of commonly used raster, vector, and hydrological operations for GIS processing. |
|[Pysheds](https://github.com/mdbartos/pysheds)|Simple and fast watershed delineation in python.|
| [Lidar](https://github.com/giswqs/lidar) | Terrain and hydrological analysis based on LiDAR-derived digital elevation models (DEM).|


Optimization, Uncertainty, Statistics
------------
| Project Name | Description |
| ------- | ------ |
| [LMFIT](https://github.com/lmfit/lmfit-py) | Non-Linear Least Squares Minimization, with flexible Parameter settings, based on scipy.optimize.leastsq, and with many additional classes and methods for curve fitting. |
| [SPOTpy](https://github.com/thouska/spotpy) | A Statistical Parameter Optimization Tool for Python. |
| [PyGLUE](http://code.activestate.com/pypm/pyglue/) | Generalised Likelihood Uncertainty Estimation (GLUE) Framework. |
| [Pyemu](https://github.com/jtwhite79/pyemu) | python modules for model-independent uncertainty analyses, data-worth analyses, and interfacing with PEST(++). |
| [HPGL](http://hpgl.github.io/hpgl/) |  High Performance Geostatistics Library. |
| [HydroErr](https://github.com/BYU-Hydroinformatics/HydroErr)| Goodness of Fit metrics for use in comparison studies, specifically in the field of hydrology. |
| [Climate-indices](https://github.com/monocongo/climate_indices) | Climate indices for drought monitoring, community reference implementations in Python. |
|[HydroLM](https://github.com/mullenkamp/HydroLM)|The HydroLM package contains a class and functions for automating linear regressions OLS for hydrologists.|
|[PySDI](https://bitbucket.org/pysdi/pysdi/src/master/)|pysdi is a set of open source scripts that compute non-parametric standardized drought indices (SDI) using raster data sets as input data.|
|[xskillscore](https://github.com/xarray-contrib/xskillscore)| Metrics for verifying forecasts.|

Data Collection
---------------
| Project Name | Description |
| ------- | ------ |
| [HKVFEWSPY](https://github.com/HKV-products-services/hkvfewspy) | Connection to the Delft FEWS servers |
| [Openradar](https://github.com/nens/openradar) | Library for processing a set of dutch, german and belgian precipitation radars into calibrated composites. |
| [Ecohydrolib](https://github.com/selimnairb/EcohydroLib)| Libraries and command-line scripts for performing ecohydrology data preparation workflows. |
| [Ulmo](https://github.com/ulmo-dev/ulmo/) | clean, simple and fast access to public hydrology and climatology data.|
| [PyHIS](https://pypi.org/project/pyhis/)| PyHIS is a python library for querying CUAHSI*-HIS** web services|
| [Wetterdienst](https://github.com/earthobservations/wetterdienst)|Python Toolset For Accessing Weather Data From German Weather Service|
| [Dataretrieval](https://github.com/USGS-python/dataretrieval) | dataretrieval is a Python package for obtaining USGS or EPA water quality data, streamflow data, and metadata directly from web services.|

Miscellaneous
-------------
| Project Name | Description |
| ------- | ------ |
| [ESMPY](https://www.earthsystemcog.org/projects/esmpy/) | Earth System Modeling Framework (ESMF) Python interface |
| [PyHSPF](https://github.com/djlampert/PyHSPF) | Python extensions to the Hydrological Simulation Program in Fortran (HSPF).|
| [PYWR](https://github.com/pywr/pywr) | spatial allocation tool |
| [SPHY](https://github.com/WilcoTerink/SPHY) |  Spatial Processes in HYdrology (SPHY) model |
| [xsboringen](https://github.com/tomvansteijn/xsboringen) | (In Dutch) A python library for processing and plotting borehole and CPT data, developed for open data formats in the Netherlands. |
| [PyMT](https://github.com/csdms/pymt/) | PyMT is an Open Source Python package that provides the necessary tools used for the coupling of models that expose the Basic Model Interface (BMI).|
| [Landlab](https://github.com/landlab/landlab) | The Landlab project creates an environment in which scientists can build a numerical landscape model without having to code all of the individual components. |
| [EFlowCalc](https://github.com/ThibHlln/eflowcalc)| Calculator of Streamflow Characteristics. |
| [IRIS](https://github.com/SciTools/iris) | A powerful, format-agnostic, and community-driven Python library for analysing and visualising Earth science data. |
| [Hydrointerp](https://github.com/mullenkamp/hydrointerp) | A Python package for interpolating hydrologic data. |
| [EFlowCalc](https://github.com/ThibHlln/eflowcalc) | EFlowCalc is an open-source calculator of ecological streamflow characteristics in Python. |
| [Hydrofunctions](https://github.com/mroberge/hydrofunctions) | A suite of convenience functions for working with hydrology data in an interactive Python session.|
| [Shyft](https://gitlab.com/shyft-os) | Shyft is the open-source toolbox for the energy-market domain, funded and supported by Statkraft. |
|[Hydroshare](https://github.com/hydroshare/hydroshare) | HydroShare is a collaborative website for better access to data and models in the hydrologic sciences.|
|[Hydrobox](https://github.com/VForWaTer/hydrobox)|hydrological preprocessing and analysis toolbox build upon pandas and numpy|
|[Wetland](https://github.com/giswqs/wetland)|wetland is a toolset for mapping surface water and wetland hydrological dynamics using fine-resolution aerial imagery within Google Earth Engine (GEE).|
|[iRONS](https://github.com/AndresPenuela/iRONS)|iRONS (interactive Reservoir Operation Notebooks and Software) is a python package that enables the simulation, forecasting and optimisation of reservoir systems.|
|[Mesas](https://github.com/charman2/mesas)|Multiresolution Estimation of StorAge Selection functions.|

