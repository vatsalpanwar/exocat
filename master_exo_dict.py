import numpy as np

######## Planet dictionaries for use by Pandexo. Just import all from this file when using pandexo. ########

all_planets = {

"Kepler_10c" : {

    "star" : {
        "jmag" : 9.889,
        "hmag" : 9.563,
    },

    "planet" : {
        "type" : "user",
        ### "exopath": ### can be populated later
        "w_unit" : "um",
        ### "f_unit": "fp/f*" or "rp^2/r*^2" , populate it later
        "depth":0.019777**2., ### Morton et al. 2016
        # "e_depth": None,
        "i":89.59,   ## Dumusque+2014
        "ars":47.9, ### Dumusque+2014
        "period":45.29, ### in days
        "transit_duration": 6.8714/24., ### in days  Morton et al. 2016
        "w": 90.,
        "ecc":0.,
    }

    },

"K2_24c" : {

    "star" : {
        "jmag" : 9.635,
        "hmag" : 9.294,
    },

    "planet" : {
        "type" : "user",
        ### "exopath": ### can be populated later
        "w_unit" : "um",
        ### "f_unit": "fp/f*" or "rp^2/r*^2" , populate it later
        "depth":0.061091**2., ### Mayo+2018
        # "e_depth": None,
        "i":89.56,   ## Mayo+2018
        "ars":49.78, ### Mayo+2018
        "period":42.3391, ### in days
        "transit_duration": 7.058/24., ### in days  Sinukoff et al. 2016
        "w": 90.,
        "ecc":0.,
    }

    },

"TOI_125b" : {

    "star" : {
        "jmag" : 9.466,
        "hmag" : 9.112,
    },

    "planet" : {
        "type" : "user",
        ### "exopath": ### can be populated later
        "w_unit" : "um",
        ### "f_unit": "fp/f*" or "rp^2/r*^2" , populate it later
        "depth":0.02950**2., ### Mayo+2018
        # "e_depth": None,
        "i":88.92,   ## Mayo+2018
        "ars":13.16, ### Mayo+2018
        "period":4.65382, ### in days
        "transit_duration": 2.962/24., ### in days  Sinukoff et al. 2016
        "w": 90.,
        "ecc":0.,
    }

    },

"TOI_125c" : {

    "star" : {
        "jmag" : 9.466,
        "hmag" : 9.112,
    },

    "planet" : {
        "type" : "user",
        ### "exopath": ### can be populated later
        "w_unit" : "um",
        ### "f_unit": "fp/f*" or "rp^2/r*^2" , populate it later
        "depth":0.02985**2., ### Mayo+2018
        # "e_depth": None,
        "i":88.54,   ## Mayo+2018
        "ars":20.66, ### Mayo+2018
        "period":9.15059, ### in days
        "transit_duration": 2.954/24., ### in days  Sinukoff et al. 2016
        "w": 90.,
        "ecc":0.,
    }

    },

"Kepler_25b" : {

    "star" : {
        "jmag" : 9.764,
        "hmag" : 9.532,
    },

    "planet" : {
        "type" : "user",
        ### "exopath": ### can be populated later
        "w_unit" : "um",
        ### "f_unit": "fp/f*" or "rp^2/r*^2" , populate it later
        "depth":0.019160**2., ### Mayo+2018
        # "e_depth": None,
        "i":92.827,   ## Mayo+2018
        "ars":13.5, ### Mayo+2018
        "period":6.238297, ### in days
        "transit_duration": 3.54393/24., ### in days  Sinukoff et al. 2016
        "w": 90.,
        "ecc":0.,
    }

    },

"Kepler_25c" : {

    "star" : {
        "jmag" : 9.764,
        "hmag" : 9.532,
    },

    "planet" : {
        "type" : "user",
        ### "exopath": ### can be populated later
        "w_unit" : "um",
        ### "f_unit": "fp/f*" or "rp^2/r*^2" , populate it later
        "depth":0.03637**2., ### Mayo+2018
        # "e_depth": None,
        "i":92.764,   ## Mayo+2018
        "ars":18.44, ### Mayo+2018
        "period":12.727, ### in days
        "transit_duration": 2.59373/24., ### in days  Sinukoff et al. 2016
        "w": 90.,
        "ecc":0.,
    }

    },

"Kepler_89e" : {

    "star" : {
        "jmag" : 11.218,
        "hmag" : 10.957,
    },

    "planet" : {
        "type" : "user",
        ### "exopath": ### can be populated later
        "w_unit" : "um",
        ### "f_unit": "fp/f*" or "rp^2/r*^2" , populate it later
        "depth":0.0396**2., ### Mayo+2018
        # "e_depth": None,
        "i":89.76,   ## Mayo+2018
        "ars":43.1, ### Mayo+2018
        "period":54.3, ### in days
        "transit_duration": 8.4652/24., ### in days  Sinukoff et al. 2016
        "w": 90.,
        "ecc":0.,
    }

    },

"HIP67522b" : {

    "star" : {
        "jmag" : 8.587,
        "hmag" : 8.287,
    },

    "planet" : {
        "type" : "user",
        ### "exopath": ### can be populated later
        "w_unit" : "um",
        ### "f_unit": "fp/f*" or "rp^2/r*^2" , populate it later
        "depth":0.0396**2.,
        # "e_depth": None,
        "i":89.34,
        "ars":11.70,
        "period":6.959503,
        "transit_duration": 4.822/24.,
        "w": 90.,
        "ecc":0.,
    }

    }



}

# BD_20594b
#
# K2_24c
#
# K2_290c
#
# K2_263b
#
# Kepler_22b
