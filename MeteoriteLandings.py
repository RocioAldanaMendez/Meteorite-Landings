import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")

from pandas_profiling import ProfileReport

profile  =  ProfileReport ( df ,  title = "Meteorites", dark_mode=True )

profile.to_file("Meteorites.html")