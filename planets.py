from astropy import time, coordinates as coord, units as un
from astropy import constants as con

############### Use only SI units! The astropy units module will let you convert to other unit systems anyway. ####################

exoplanets = {

######### Following planets added for ESO P106, Lorenzo UHJ proposal. #######

"HAT-P-57" : {
    "b":{
        "Rp":[1.41*un.R_jup, 0.36*un.R_jup, 0.36*un.R_jup ],
        "Mp":None,
        #### Add other properties here later.
    },

    "star" : {

    },

    "Refs" : {
        "Stassun+2017" : "ADSlink",
        "Hartman+2015": "ADSlink",
    }

},

"HAT-P-70" : {
    "b":{
        "Rp":[1.87*un.R_jup, 0.15*un.R_jup, 0.1*un.R_jup ],
        "Mp":[6.78*un.M_jup, None, None ], ####### upper limit
        "P" : [2.74432452, 0.00000079,0.00000068],
        "T0" : [2458439.57519,0.00045,0.00037],
        "occ_dur":[]

        #### Add other properties here later.
    },

    "star" : {
        "Rs": [  1.858*un.R_sun, 0.119*un.R_sun, 0.091*un.R_sun ],
        "log_g" : [4.181, 0.055,0.063],  ##### log10(cm/s2)
        "lum" : [1.22, 0.12,0.12], #### log10(Lsun)
        "met" : [-0.0590,0.0750,0.0880], ############ dex
        "coord" : "04:58:12.560 +09:59:52.726",
        "Teff": [8124.333 * un.K, 669.166 * un.K, 1365.583 * un.K]

    },

    "Refs" : {
        "Temple+2017" : "ADSlink",
    }

},

"KELT-19A" : {
    "b":{
        "Rp":[1.91*un.R_jup, 0.11*un.R_jup, 0.11*un.R_jup ],
        "Mp":None,
        #### Add other properties here later.
    },

    "star" : {

    },

    "Refs" : {
        "Siverd+2018" : "ADSlink",
    }

},

"WASP-167" : {
    "b":{
        "Rp":[1.58*un.R_jup, 0.05*un.R_jup, 0.05*un.R_jup ],
        "Mp":None,
        #### Add other properties here later.
    },

    "star" : {

    },

    "Refs" : {
        "Temple+2017" : "ADSlink",
    }

},

"WASP-18" : {
    "b":{
        "Rp":[1.19*un.R_jup, 0.038*un.R_jup, 0.038*un.R_jup ],
        "Mp":[10.2*un.M_jup, 0.7*un.M_jup, 0.7*un.M_jup ],
        "P" : [0.941453, 0.000002,0.000002], #### Shporer
        "T0" : [2458375.169900,0.000025,0.000025],
        "occ_dur":[2.181,0.019,0.019] ### Triaud+2010

        #### Add other properties here later.
    },

    "star" : {
        "Rs": [  1.2397299*un.R_sun, 0.07*un.R_sun, 0.12*un.R_sun ],
        "log_g" : [4.47, 0.13,0.13],  ##### log10(cm/s2)
        "lum" : [0.3828, 0.00224,0.00225], #### log10(Lsun)
        "met" : [0.,0.09,0.09], ############ dex
        "coord" : "01:37:25.0 -45:40:40",
        "Teff": [6462.0073* un.K, 338.2180 * un.K, 192.0640 * un.K]

    },

    "Refs" : {
        "Temple+2017" : "ADSlink",
    }

},

"MASCARA-1" : {
    "b":{
        "Rp":[1.5*un.R_jup, 0.3*un.R_jup, 0.3*un.R_jup ],
        "Mp":[3.7*un.M_jup, 0.9*un.M_jup, 0.9*un.M_jup ],
        "P" : [2.148780, 0.000008,0.000008],
        "T0" : [2457097.278,0.002,0.002],
        "occ_dur":[4.05, 0.03,0.03]


        #### Add other properties here later.
    },

    "star" : {
        "Rs": [  1.9440713*un.R_sun, 0.0823562*un.R_sun, 0.0217450*un.R_sun ],
        "log_g" : [4., None,None],  ##### log10(cm/s2)
        "lum" : [1.1106570, 0.0060764,0.0061627], #### log10(Lsun)
        "met" : [0.,None,None], ############ dex
        "coord" : "21:10:12.37 +10:44:19.9",
        "Teff": [7845.750 * un.K, 44.250 * un.K, 161.083 * un.K]

    },

    "Refs" : {
        "Temple+2017" : "ADSlink",
    }

},

"WASP-121" : {
    "b":{
        "Rp":[1.865*un.R_jup, 0.044*un.R_jup, 0.044*un.R_jup ],
        "Mp":[1.183*un.M_jup, 0.064*un.M_jup, 0.062*un.M_jup ],
        "P" : [1.27492550, 0.00000025,0.00000025],
        "T0" : [2456635.70832,0.00010,0.00010],
        "occ_dur":[2.8872,0.0072,0.0072]  #### hours
        #### Add other properties here later.
    },

    "star" : {
        "Rs": [  1.458*un.R_sun, 0.03*un.R_sun, 0.03*un.R_sun ],
        "log_g" : [4.242, 0.011,0.011],  ##### log10(cm/s2)
        "lum" : [0.58254650, 0.00456161,0.00456161], #### log10(Lsun)
        "met" : [0.13,0.09,0.09], ############ dex
        "coord" : "07:10:24.07 -39:05:50.6",
        "Teff":[6396.0664*un.K, 121.33*un.K, 133.14*un.K]

    },

    "Refs" : {
        "Temple+2017" : "ADSlink",
    }

},

"XO-2N" : {
    "b":{
        "Rp":[1.019*un.R_jup, 0.03*un.R_jup, 0.03*un.R_jup ],  ### Bonomo+
        # "Mp":[0.595*un.M_jup, 0.02*un.M_jup, 0.02*un.M_jup ], #### Bonomo+
        "Mp": [0.595 , 0.02, 0.02],  #### Bonomo+

        "P" : [2.61585922, 0.00000028,0.00000028], ####Bonomo+
        "T0" : [2454508.73829,0.00014,0.00016], ### Crouzet+
        "occ_dur":[2.6839,0.0066,0.0077],  #### Crouzet+
        #### Add other properties here later.
        "ecc":[0.,0.,0.],
        "w":[90.,0.,0.],
        "rp":[0.10304,0.00037,0.00037],
        "a":[7.986,0.074,0.074],
        "inc":[88.01,0.33,0.28],
        "Teq":[1328., 17.,28.]
    },

    "star" : {
        "Rs": [  1.1022209*un.R_sun, 0.0468730*un.R_sun, .0334030*un.R_sun ], ###GaiaDR2
        "log_g" : [4.433, 0.008,0.008],  ##### log10(cm/s2) ###Crouzet
        "lum" : [0.10751163, 0.00530122,0.00536674], #### log10(Lsun)  #### GaiaDR2
        "met" : [0.430,0.05,0.05], ############ dex  ###Bonomo+
        "coord" : "07:48:06.47 +50:13:32.9",
        "Teff":[5167.900*un.K, 80.133*un.K, 106.500*un.K]

    },

    "Refs" : {
        "Temple+2017" : "ADSlink",
    }

},

"WASP-19" : {
    "b":{
        "Rp":[1.392*un.R_jup, 0.04*un.R_jup, 0.04*un.R_jup ],
        "Mp":[1.069*un.M_jup, 0.038*un.M_jup, 0.037*un.M_jup ],
        # "Mp": [1.069 , 0.038 , 0.037 ],

        "P" : [0.788838989, 0.000000040,0.000000040],
        # "e":[0.0020,0.014,0.002],
        # "w":[259.,13.,-170.],
        "T0" : [2455708.534626,0.000019,0.000019],
        "occ_dur":[1.581,0.008,0.008],  #### hours
        #### Add other properties here later.
        "ecc":[0.,0.,0.],
        "w":[90.,0.,0.],
        "rp":[0.1409,0.0013,0.0013],  ### Revised from Spitzer
        "a":[3.46, 0.08 , 0.08  ], ### Old, from K2
        "inc":[ 78.78, 0.58,0.58 ], ### Old from K2
        "b" : [None,None,None] , ###
        "Teq":[2240., 40.,40.]      #### See WASP-19 TESS phase curve paper by Wong et al. 2019; this is the dayside isotherm from the overall emission spectra.
    },

    "star" : {
        "Rs": [  1.0011936*un.R_sun, 0.0347518*un.R_sun, 0.0390503*un.R_sun ],
        "log_g" : [4.45, 0.05,0.05],  ##### log10(cm/s2)
        "lum" : [-0.096028855, 0.004813273,0.004867256], #### log10(Lsun)
        "met" : [0.15,0.07,0.07], ############ dex
        "coord" : "09:53:40.08 -45:39:33.1",
        "Teff":[5458.3335*un.K, 109.6670*un.K, 92.3335*un.K]

    },

    "Refs" : {
        "Temple+2017" : "ADSlink",
    }

},


"HAT-P-26" : {
    "b":{
        "Rp":[0.63*un.R_jup, 0.04*un.R_jup, 0.04*un.R_jup ],
        # "Mp":[0.07*un.M_jup, 0.02*un.M_jup, 0.02*un.M_jup ],
        "Mp": [0.07 , 0.02 , 0.02 ],

        "P" : [4.234516, 0.000015,0.000015],
        "e":[0.124,0.06,0.06],
        # "w":[259.,13.,-170.],
        "T0" : [2455304.65218,0.0002,0.0002],
        "occ_dur":[	2.4552,0.024,0.024],  #### hours
        #### Add other properties here later.
        "ecc":[0.124,0.06,0.06],
        "w":[54.,165.,165.],
        "rp":[0.0737,0.0012,0.0012],  ### Revised from Spitzer
        "a":[13.06, 0.83, 0.83 ], ### Old, from K2
        "inc":[ 88.6, 0.7,0.7 ], ### Old from K2
        "b" : [0.303,0.112,0.112] , ###
        "Teq":[1001., 66.,37.]      #### See WASP-19 TESS phase curve paper by Wong et al. 2019; this is the dayside isotherm from the overall emission spectra.
    },

    "star" : {
        "Rs": [  0.8564404*un.R_sun, 0.029*un.R_sun, 0.022*un.R_sun ],
        "log_g" : [4.56, 0.06,0.06],  ##### log10(cm/s2)
        "lum" : [-0.36789808, 0.00463184,0.00468180], #### log10(Lsun)
        "met" : [-0.04,0.08,0.08], ############ dex
        "coord" : "14:12:37.53 +04:03:36.0",
        "Teff":[5046.6504*un.K, 66.9196*un.K, 85.6504*un.K]

    },

    "Refs" : {
        "Temple+2017" : "ADSlink",
    }

},



"V1298-Tau" : {
    "b":{
        "Rp": [ 0.916*un.R_jup, 0.052*un.R_jup, 0.047*un.R_jup ],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp":[0.40*un.M_jup, 0.*un.M_jup, 0.*un.M_jup ], ### Mjup Mb + Md < 120 Mearth
        "P" : [ 24.141445 ,0.000056 ,0.000056], #### Revised from Spitzer
        "T0" : [2457067.04646,0.002141,0.002141], ### Revised from Spitzer IRAC2 and confimred from Trevor; might be better to use Claire's estimate;
        "occ_dur":[ 6.42, 0.013, 0.013 ],  #### From K2
        #### Add other properties here later.
        "ecc":[0.,0.,0.],
        "w":[90.,0.,0.],
        "rp":[0.0699,0.001,0.001],  ### Revised from Spitzer
        "a":[27.0,1.1,1.1  ], ### Old, from K2
        "inc":[ 89.00, 0.46,0.24 ], ### Old from K2
        "b" : [0.36,0.11,0.19],  ### Revised, from Spitzer
        "Teq":[668.,22,22]
    },

    "c": {
        "Rp": [0.499 * un.R_jup, 0.032 * un.R_jup, 0.029 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        # "Mp": [0.0880761 * un.M_jup, 0. * un.M_jup, 0. * un.M_jup],  ### Mjup Mc + Md < 28 Mearth, so extreme upper limit.
        "Mp": [0.0629 * un.M_jup, 0. * un.M_jup, 0. * un.M_jup],  ### Mjup Mc ~ 20 Mearth , reasonable upper limit
        "P": [8.24958, 0.00072, 0.00072],  #### Revised from Spitzer
        "T0": [2457064.2797, 0.0034	, 0.0034 ],
        ### Revised from Spitzer IRAC2 and confimred from Trevor; might be better to use Claire's estimate;
        "occ_dur": [4.66, 0.12, 0.12],  #### From K2
        #### Add other properties here later.
        "ecc": [0., 0., 0.],
        "w": [90., 0., 0.],
        "rp": [0.0381, 0.0017, 0.0017],
        "a": [13.19, 0.55, 0.55],  ### Old, from K2
        "inc": [88.49,0.92,0.72],  ### Old from K2
        "b": [0.34, 0.19, 0.21] ,
        # "Teq":[968.,31,31], ### ExoArchive
        "Teq":[1000.,0.,0.]  ## Mean
        # "Teq":[1120.,0,0], #### Bean's proposal
    },

    "d": {
        "Rp": [0.572 * un.R_jup, 0.052 * un.R_jup, 0.047 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [0.40 * un.M_jup, 0. * un.M_jup, 0. * un.M_jup],  ### Mjup Mb + Md < 120 Mearth
        "P": [12.4032, 0.0015, 0.0015],  #### Revised from Spitzer
        "T0": [2457072.3913, 0.003, 0.003],
        ### Revised from Spitzer IRAC2 and confimred from Trevor; might be better to use Claire's estimate;
        "occ_dur": [5.59, 0.013, 0.013],  #### From K2
        #### Add other properties here later.
        "ecc": [0., 0., 0.],
        "w": [90., 0., 0.],
        "rp": [0.0436, 0.0024,0.0021],  ### Revised from Spitzer
        "a": [17.31, 0.72, 0.72],  ### Old, from K2
        "inc": [89.04, 0.46, 0.24],  ### Old from K2
        "b": [0.29, 0.27, 0.20],
        # "Teq":[845,27,27],
        "Teq": [890., 0, 0],  #### Bean's proposal

    },

    "e": {
        "Rp": [0.780 * un.R_jup, 0.075* un.R_jup, 0.064 * un.R_jup],  ### From K2
        "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        # "Mp": [0.40 * un.M_jup, 0. * un.M_jup, 0. * un.M_jup],  ### Mjup Mb + Md < 120 Mearth
        "P": [60, 60, 18],  #### Revised from Spitzer
        "T0": [2457096.6229, 0.0023	, 0.0023 ],
        ### Revised from Spitzer IRAC2 and confimred from Trevor; might be better to use Claire's estimate;
        "occ_dur": [7.45, 0.32, 0.25],  #### From K2
        #### Add other properties here later.
        "ecc": [0., 0., 0.],
        "w": [90., 0., 0.],
        "rp": [0.0699, 0.001, 0.001],  ### Revised from Spitzer
        "a": [27.0, 1.1, 1.1],  ### Old, from K2
        "inc": [89.00, 0.46, 0.24],  ### Old from K2
        "b": [0.36, 0.11, 0.19] ,
        "Teq":[492,66,104]
    },

    "star" : {
        "Rs": [  1.2943925*un.R_sun,0.0238242*un.R_sun, 0.0446042*un.R_sun ], ###GaiaDR2
        "Ms" : [  1.10*un.M_sun,0.05*un.M_sun, 0.05*un.M_sun ],
        "log_g" : [4.246, 0.034,0.034],  ##### log10(cm/s2) ###David+2019
        "lum" : [ -0.038449572, 0.003682562 , 0.003714036 ], #### log10(Lsun)  #### GaiaDR2
        "met" : [None,None,None], ############ dex  ###Bonomo+
        "coord" : "04:05:19.59 +20:09:25.6",
        "Teff":[4962.2764*un.K, 87.7739*un.K, 45.0464*un.K],
        "Prot":[2.870, 0.022,0.022], #### days, David+2019
        "vsini":[23., 2.,2.], #### km/s
        "baryRV":[16.15,0.38,0.38] ### km/s  #### this is the vsys

    },

    "Refs" : {
        "David+2019" : "ADSlink",
    }

},

"GJ-436" : {
    "b":{
        "Rp": [ 0.372*un.R_jup, 0.015*un.R_jup, 0.015*un.R_jup ],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp":[0.0728, 0.0024, 0.0024 ], ### Mjup
        "P" : [ 2.64389788 ,0.00000010 ,0.00000010], #### Revised from Spitzer
        "T0" : [2454238.479958,0.000039,0.000039], ### Revisedfrom Spitzer and confimred fromTrevor
        "occ_dur":[ 1.009, 0.034, 0.034 ],  #### From K2
        #### Add other properties here later.
        "ecc":[0.152,0.009,0.009],
        "w":[325.8,5.4,5.7],
        "rp":[0.0822,0.001,0.001],  ### Revised from Spitzer
        "a":[14.54,0.14,0.14  ], ### Old, from K2
        "inc":[ 86.774, 0.03,0.03 ], ### Old from K2
        "b" : [0.73,0.04,0.04],  ### Revised, from Spitzer
        "Teq":[686,10,10]
    },

    "star" : {
        "Rs": [  0.455*un.R_sun,0.018*un.R_sun, 0.018*un.R_sun ], ###GaiaDR2
        "Ms" : [  0.47*un.M_sun,0.07*un.M_sun, 0.07*un.M_sun ],
        "log_g" : [4.792, 0.047,0.044],  ##### log10(cm/s2) ###David+2019
        "lum" : [ -1.523, 0.669 , 0.426 ], #### log10(Lsun)  #### GaiaDR2
        "met" : [None,None,None], ############ dex  ###Bonomo+
        "coord" : "11:42:11.09 +26:42:23.7",
        "Teff":[3660.420*un.K, 136*un.K, 131*un.K],
        "Prot":[44.09, 0.08,0.08], #### days, David+2019
        "vsini":[0.33, 0.09,0.09], #### km/s
        "baryRV":[9.6,0.,0.] ### km/s  #### this is the vsys

    },

    "Refs" : {
        "David+2019" : "ADSlink",
    }

},

"WASP-33" : {
    "b":{
        "Rp": [ 1.603*un.R_jup, 0.014*un.R_jup, 0.014*un.R_jup ],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp":[2.8, 0.53, 0.53 ], ### Mjup

        "Teq":[2782,41,41]
    },

    "star" : {


    },

    "Refs" : {
        "David+2019" : "ADSlink",
    }

},

"WASP-12" : {
    "b":{
        "Rp": [ 1.9*un.R_jup, 0.057*un.R_jup, 0.057*un.R_jup ],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp":[1.47, 0.076, 0.069 ], ### Mjup

        "Teq":[2593.,57.,57.]
    },

    "star" : {


    },

    "Refs" : {
        "David+2019" : "ADSlink",
    }

},

"WASP-55" : {
    "b":{
        "Rp": [ 1.3*un.R_jup, 0.05*un.R_jup, 0.05*un.R_jup ],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp":[0.57, 0.04, 0.04 ], ### Mjup

        "Teq":[1290.,0.,0.]
    },

    "star" : {


    },

    "Refs" : {
        "David+2019" : "ADSlink",
    }

},

"Kepler-42" : {
    "b":{
        "Rp": [ 0.070*un.R_jup, 0.02*un.R_jup, 0.02*un.R_jup ],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp":[0.001255, 0.0, 0.0 ], ### Mjup

        "Teq":[519.,0.,0.]
    },

    "star" : {


    },

    "Refs" : {
        "David+2019" : "ADSlink",
    }

},

"HAT-P-23": {
    "b": {
        "Rp": [1.368 * un.R_jup, 0.09 * un.R_jup, 0.09 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [2.09, 0.11, 0.11],  ### Mjup

        "Teq": [2056., 66, 66]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},


"TrES-3": {
    "b": {
        "Rp": [1.305 * un.R_jup, 0.09 * un.R_jup, 0.09 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [1.91, 0.06, 0.07],  ### Mjup  ### Mjup

        "Teq": [1638., 22, 22]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},

"Kepler-45": {
    "b": {
        "Rp": [0.96 * un.R_jup, 0.11 * un.R_jup, 0.11 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [0.505, 0.09, 0.09],  ### Mjup

        "Teq": [1000., 20, 20]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},



"WASP-32": {
    "b": {
        "Rp": [1.190 * un.R_jup, 0.06 * un.R_jup, 0.06 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [3.60, 0.07, 0.07],  ### Mjup

        "Teq": [1428., 0, 0]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},

"WASP-48": {
    "b": {
        "Rp": [1.5 * un.R_jup, 0.2 * un.R_jup, 0.2 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [0.8, 0.23, 0.23],  ### Mjup

        "Teq": [2035., 52, 52]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},

"GJ-3470": {
    "b": {
        "Rp": [0.408 * un.R_jup, 0.016 * un.R_jup, 0.016 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [0.0437, 0.0047, 0.0047],  ### Mjup

        "Teq": [615., 16, 16]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},

"Kepler-18": {
    "c": {
        "Rp": [0.490 * un.R_jup, 0.016 * un.R_jup, 0.016 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [0.054, 0.006, 0.006],  ### Mjup

        "Teq": [899., 0, 0]
    },

    "d": {
        "Rp": [0.623 * un.R_jup, 0.016 * un.R_jup, 0.016 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [0.052, 0.004, 0.004],  ### Mjup

        "Teq": [720., 0, 0]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},

"HAT-P-7": {
    "b": {
        "Rp": [1.51 * un.R_jup, 0.21 * un.R_jup, 0.21 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [1.84, 0.53, 0.53],  ### Mjup

        "Teq": [2200., 30, 30]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},

"WASP-4": {
    "b": {
        "Rp": [1.321 * un.R_jup, 0.039 * un.R_jup, 0.039 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [1.186, 0.09, 0.09],  ### Mjup

        "Teq": [1664., 54, 54]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},

"WASP-80": {
    "b": {
        "Rp": [0.999 * un.R_jup, 0.03 * un.R_jup, 0.031 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [0.538, 0.035, 0.036],  ### Mjup

        "Teq": [825., 19., 19.]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},


"HAT-P-1": {
    "b": {
        "Rp": [1.319 * un.R_jup, 0.019 * un.R_jup, 0.019 * un.R_jup],  ### From K2
        # "Mp":[None, None, None ], #### 3 sigma upper limit 2.2 M jup
        "Mp": [0.525, 0.019, 0.019],  ### Mjup

        "Teq": [1322., 14., 15.]
    },

    "star": {

    },

    "Refs": {
        "David+2019": "ADSlink",
    }

},

"HIP67522" : {
    "b":{
        "Rp": [ 0.8984*un.R_jup, 0.0419*un.R_jup, 0.0419*un.R_jup ],
        # "Mp":[None, None, None ],
        "Mp":[0.2*un.M_jup, 0.*un.M_jup, 0.*un.M_jup ],   #### RV upper limit
        "P" : [ 6.959503 ,0.000016, 0.000015],
        "T0" : [2458604.02371,0.00036,0.00037],
        "occ_dur":[ 4.822, 0.021, 0.019 ],
        #### Add other properties here later.
        "ecc":[0.,0.,0.],
        "w":[90.,0.,0.],
        "rp":[0.0667,0.0012,0.0011],
        "a":[11.70,0.24,0.27  ],
        "inc":[ 89.34, 0.45,0.54 ],
        "b" : [0.134,0.106,0.092 ],
        "Teq": [1174., 21., 20.]
    },

    "star" : {
        "Rs": [  1.38*un.R_sun,0.06*un.R_sun, 0.06*un.R_sun ],
        "Ms" : [  1.22*un.M_sun,0.05*un.M_sun, 0.05*un.M_sun ],
        "log_g" : [None,None,None],  ##### log10(cm/s2)
        "lum" : [ 0.243, 0.022, 0.023], #### log10(Lsun)  #### GaiaDR2
        "met" : [None,None,None], ############ dex  ###Bonomo+
        "coord" : "13:50:06.28 -40:50:08.9",
        "Teff":[5675.*un.K, 75*un.K, 75*un.K],
        "Prot":[2.870, 0.022,0.022], #### days, David+2019
        "vsini":[54.2, 0.7,0.7], #### km/s
        "baryRV":[7.41,0.25,0.25] ### km/s  #### this is the vsys

    },

    "Refs" : {
        "Rizzuto+2020" : "ADSlink",
    }

},


"DS-Tuc-A" : {
    "b":{
        "Rp": [ 0.509*un.R_jup, 0.02*un.R_jup, 0.02*un.R_jup ],
        # "Mp":[None, None, None ],
        # "Mp":[1.3*un.M_jup, 0.*un.M_jup, 0.*un.M_jup ],   #### RV upper limit
        "Mp":[0.089345*un.M_jup, 0.*un.M_jup, 0.*un.M_jup ],   #### Chen and Kipping prediction, predicted mass of the planet if it is fully mature
        # "Mp":[0.0188735*un.M_jup, 0.*un.M_jup, 0.*un.M_jup ],
        "P" : [ 8.13826, 0.000011, 0.000011	],   ## Newton et al. 2019
        "T0" : [ 2458332.30997, 0.00026,0.00026], ## Newton et al. 2019
        "occ_dur":[ 3.1764, 0.0118, 0.0094 ],
        #### Add other properties here later.
        "ecc":[0.,0.,0.],
        "w":[90.,0.,0.],
        "rp":[0.05419,0.00024,0.00024],
        "a":[20.35, 0.29,0.69  ],
        "inc":[ 89.50, 0.34,0.41 ],
        "b" : [0.18,0.13,0.12 ],
        "Teq": [915, 0., 0.]   ### Bean+ proposal;
    },

    "star" : {
        "Rs": [  0.964*un.R_sun,0.029*un.R_sun, 0.029*un.R_sun ], ### Newton et al. 2019
        "Ms" : [  1.01*un.M_sun,0.06*un.M_sun, 0.06*un.M_sun ], ###  Newton et al. 2019
        "log_g" : [4.60,0.15,0.15],  ##### log10(cm/s2), Benatti et al. 2019
        "lum" : [ -0.1608987, 0.0011, 0.0011], #### log10(Lsun)  #### GaiaDR2
        "met" : [ -0.080,0.06,0.06], ############ dex  ###Benatti et al. 2019
        "coord" : "23:39:39.48 -69:11:44.7",
        "Teff":[5428.*un.K, 80*un.K, 80*un.K],
        "Prot":[2.85, 0.04,0.05], #### days, David+2019
        "vsini":[17.8, 0.2,0.2], #### km/s
        "baryRV":[8.05,0.06,0.06] ### km/s  #### this is the vsys

    },

    "Refs" : {
        "Newton+2019" : "ADSlink",
        "Benatti+2019": "ADSlink",
    }

},


}