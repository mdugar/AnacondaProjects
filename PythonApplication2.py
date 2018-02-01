
import pandas as pd
import gzip

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

''' Reading the Reviews into DataFrames'''

#df_IV5 = getDF('reviews_Amazon_Instant_Video_5.json.gz')
#df_AA5 = getDF('reviews_Apps_for_Android_5.json.gz')
#
#df_AU5 = getDF('reviews_Automotive_5.json.gz')
#df_BA5 = getDF('reviews_Baby_5.json.gz')
#df_BE5 = getDF('reviews_Beauty_5.json.gz')
#df_BO5 = getDF('reviews_Books_5.json.gz')
#df_CV5 = getDF('reviews_CDs_and_Vinyl_5.json.gz')
#df_CP5 = getDF('reviews_Cell_Phones_and_Accessories_5.json.gz')
#df_CJ5 = getDF('reviews_Clothing_Shoes_and_Jewelry_5.json.gz')
#df_DM5 = getDF('reviews_Digital_Music_5.json.gz')
#df_EL5 = getDF('reviews_Electronics_5.json.gz')
#df_GG5 = getDF('reviews_Grocery_and_Gourmet_Food_5.json.gz')
#df_HP5 = getDF('reviews_Health_and_Personal_Care_5.json.gz')
#df_HK5 = getDF('reviews_Home_and_Kitchen_5.json.gz')
#df_KS5 = getDF('reviews_Kindle_Store_5.json.gz')
#df_MT5 = getDF('reviews_Movies_and_TV_5.json.gz')
#df_MI5 = getDF('reviews_Musical_Instruments_5.json.gz')
#df_OP5 = getDF('reviews_Office_Products_5.json.gz')
#df_LG5 = getDF('reviews_Patio_Lawn_and_Garden_5.json.gz')
#df_PS5 = getDF('reviews_Pet_Supplies_5.json.gz')
#df_SO5 = getDF('reviews_Sports_and_Outdoors_5.json.gz')
#df_TH5 = getDF('reviews_Tools_and_Home_Improvement_5.json.gz')
#df_TG5 = getDF('reviews_Toys_and_Games_5.json.gz')
#df_VG5 = getDF('reviews_Video_Games_5.json.gz')
#

'''Reading the Ratings into DataFrames'''

df_RT_IV5 = pd.read_csv('ratings_Amazon_Instant_Video.csv')
df_RT_AA5 = pd.read_csv('ratings_Apps_for_Android.csv')
#
#df_RT_AU5 = pd.read_csv('ratings_Automotive.csv')
#df_RT_BA5 = pd.read_csv('ratings_Baby.csv')
#df_RT_BE5 = pd.read_csv('ratings_Beauty.csv')
#df_RT_BO5 = pd.read_csv('ratings_Books.csv')
#df_RT_CV5 = pd.read_csv('ratings_CDs_and_Vinyl.csv')
#df_RT_CP5 = pd.read_csv('ratings_Cell_Phones_and_Accessories.csv')
#df_RT_CJ5 = pd.read_csv('ratings_Clothing_Shoes_and_Jewelry.csv')
#df_RT_DM5 = pd.read_csv('ratings_Digital_Music.csv')
#df_RT_EL5 = pd.read_csv('ratings_Electronics.csv')
#df_RT_GG5 = pd.read_csv('ratings_Grocery_and_Gourmet_Food.csv')
#df_RT_HP5 = pd.read_csv('ratings_Health_and_Personal_Care.csv')
#df_RT_HK5 = pd.read_csv('ratings_Home_and_Kitchen.csv')
#df_RT_KS5 = pd.read_csv('ratings_Kindle_Store.csv')
#df_RT_MT5 = pd.read_csv('ratings_Movies_and_TV.csv')
#df_RT_MI5 = pd.read_csv('ratings_Musical_Instruments.csv')
#df_RT_OP5 = pd.read_csv('ratings_Office_Products.csv')
#df_RT_LG5 = pd.read_csv('ratings_Patio_Lawn_and_Garden.csv')
#df_RT_PS5 = pd.read_csv('ratings_Pet_Supplies.csv')
#df_RT_SO5 = pd.read_csv('ratings_Sports_and_Outdoors.csv')
#df_RT_TH5 = pd.read_csv('ratings_Tools_and_Home_Improvement.csv')
#df_RT_TG5 = pd.read_csv('ratings_Toys_and_Games.csv')
#df_RT_VG5 = pd.read_csv('ratings_Video_Games.csv')
#
print(df_RT_IV5.head())
print(df_RT_AA5.head())
#print(df_IV5.head())
#print(df_AA5.head())