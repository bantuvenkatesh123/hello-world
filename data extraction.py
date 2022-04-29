import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup
import textwrap
df=pd.read_csv('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/titanic_train.csv')
df.sample(5)
