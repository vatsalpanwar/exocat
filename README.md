exocat

```python

sys.path.append(os.path.abspath(<path to exocat folder>))
import planets

Do importlib.reload(planets) everytime you update the file 

For general planet and stellar host properties:

star = "HIP67522"
pex = "b"
  
Rs = planets.exoplanets[star]["star"]["Rs"][0] ## Stellar radius 
Mp = planets.exoplanets[star][pex]["Mp"][0] ## Planetary Mass
Rp = planets.exoplanets[star][pex]["Rp"][0] ## Planetary Radii
T = planets.exoplanets[star][pex]["Teq"][0] ## Planetary Equilibrium temperature 

For updating the PandExo exodictionary 

import master_exo_dict as med
planet_dict = med.all_planets[planet_name]
exo_dict = jdi.load_exo_dict()
exo_dict.update(planet_dict)  #### This would update most of the planet information in the pandexo exo_dict 

```
