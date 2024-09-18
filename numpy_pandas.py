#gorev 1#########################################
#Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

import numpy as np
import seaborn as sns
from unicodedata import category

sns.load_dataset("titanic")
df = sns.load_dataset("titanic")
df.head()

#gorev 2#########################################
#Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

df.sort_values("sex").count()

#gorev 3#########################################
# Her bir sutuna ait unique değerlerin sayısını bulunuz.

df.nunique("columns")
df.head()

#gorev 4#########################################
#pclass değişkeninin unique değerlerinin sayısını bulunuz

df["pclass"].unique()

#gorev 5#########################################
#pclass ve parch değişkenlerini nunique değerlerinin sayısını bulunuz

df[["pclass", "parch"]].nunique()

#gorev 6#########################################
# embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

df["embarked"].dtype
df["embarked"].astype("category")
df["embarked"].dtype

#gorev 7######################################
#embarked değeri C olanların tüm bilgelerini gösteriniz.
df[df["embarked"] == "C"].head()

#gorev 8#########################################
#embarked değeri S olmayanların tüm bilgelerini gösteriniz
df[df["embarked"] != "S"].head()

#gorev 9#########################################
#Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df.loc[(df["age"] < 30) & (df["sex"] == "female")].head()

#gorev 10#########################################
#Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz

df.loc[(df["fare"] < 500) & (df["age"] > 70)].head()

#gorev 11#########################################
#Her bir değişkendeki boş değerlerin toplamını bulunuz

df.isnull().sum()

#gorev 12#########################################
#who değişkenini dataframe’den çıkarınız

sns.load_dataset("titanic")
df = sns.load_dataset("titanic")
df.head()
df.columns.drop("who")

#gorev 13#########################################
#deck değikenindeki boş değerleri deck değişkenin en çok
# tekrar eden değeri (mode) ile doldurunuz.

df["deck"] = df["deck"].fillna(df["deck"].mode()[0])
df["deck"]
df

#gorev 14#########################################
#age değikenindeki boşdeğerleri age değişkenin medyanı ile doldurunuz

df["age"].fillna(df["age"].median())
df["age"]

#gorev 15#########################################
#survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında
# sum, count, mean değerlerini bulunuz

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})

#gorev 16#########################################
#30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın.
# Yazdığınızfonksiyonukullanaraktitanikverisetindeage_flagadındabirdeğişkenoluşturunuzoluşturunuz.
# (apply velambda yapılarınıkullanınız)

def age_30(age):
    if age > 30:
        return 1
    else:
        return 0
    print(age_30)

df["age_flag"]= df["age_30"].apply(lambda x: age_30(x))

df["age_flag"]= df["age_30"].apply(lambda x: 1 if x<30 else 0)

#gorev 17#########################################
#Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız

import seaborn as sns
import pandas as pd
sns.load_dataset("tips")
df = sns.load_dataset("tips")
df.columns

#gorev 18#########################################
#Time değişkeninin kategorilerine (Dinner, Lunch) göre
# total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz

df.groupby(["time"]).agg({"total_bill":["sum", "min", "max", "mean"]})

#gorev 19#########################################
#Günlere ve time göre total_bill değerlerinin
# toplamını, min, max ve ortalamasını bulunuz

df.groupby(["time", "day"]).agg({"total_bill":["sum", "min", "max", "mean"]})

#gorev 20#########################################
#Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin
# day'e göre toplamını, min, max ve ortalamasını bulunuz

df.loc[(df["time"]== "lunch") & (df["sex"] == "female")]

df.groupby(["day"]).agg({"total_bill": ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max"]})

#gorev 21#########################################
#size'i 3'ten küçük, total_bill'i 10'dan büyük olan
# siparişlerin ortalaması nedir? (loc kullanınız)

df.loc[(df["size"]<3) & (df["total_bill"] > 10)].mean().head()

#gorev 22#########################################
#total_bill_tip_sum adında yeni birdeğişken oluşturunuz.
# Her bir müşterinin ödediği total bill ve tip in toplamını versin.

df["total_bill_sum"] = df["total_bill"] + df["tip"]
df

#gorev 23#########################################
#Total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız
# ve ilk 30 kişiyi yeni bir dataframe'e atayınız
df = df.sort_values("total_bill_sum", ascending=False)[:30]
df
