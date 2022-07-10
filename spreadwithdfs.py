import pandas as pd
import gspread
import gc
from gspread_pandas import Spread
import random, time
import openpyxl
import gspread_dataframe as gd

# Connecting with `gspread` here

day = pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_DAILY.csv")
s = Spread("data")
s.open_sheet("Sheet1")
s.df_to_sheet(day, start = "A1", index = False, )


week = pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_WEEKLY.csv")
wss = Spread("data2")
wss.open_sheet("Sheet1")
wss.df_to_sheet(week, start = "A1", index = False, )


art= pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_ART.csv")
wss = Spread("BLT_ART")
wss.open_sheet("Sheet1")
wss.df_to_sheet(art, start = "A1", index = False, )


attention=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_ATTENTION.csv")
wss = Spread("BLT_ATTENTION")
wss.open_sheet("Sheet1")
wss.df_to_sheet(attention, start = "A1", index = False, )


attentionbtc=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_ATTENTION_BITCOIN.csv")
wss = Spread("BLT_BTC")
wss.open_sheet("Sheet1")
wss.df_to_sheet(attentionbtc, start = "A1", index = False, )


attentioncrypto=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_ATTENTION_CRYPTO.csv")
wss = Spread("BLT_CRYPTO")
wss.open_sheet("Sheet1")
wss.df_to_sheet(attentioncrypto, start = "A1", index = False, )


attentionmetaverse=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_ATTENTION_METAVERSE.csv")
wss = Spread("BLT_METAVERSE")
wss.open_sheet("Sheet1")
wss.df_to_sheet(attentionmetaverse, start = "A1", index = False, )


avatar=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_AVATAR.csv")
wss = Spread("BLT_AVATAR")
wss.open_sheet("Sheet1")
wss.df_to_sheet(avatar, start = "A1", index = False, )


azuki=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_AZUKI.csv")
wss = Spread("BLT_AZUKI")
wss.open_sheet("Sheet1")
wss.df_to_sheet(azuki, start = "A1", index = False, )


blt5=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_BLT5.csv")
wss = Spread("BLT5")
wss.open_sheet("Sheet1")
wss.df_to_sheet(blt5, start = "A1", index = False, )


blt10=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_BLT10.csv")
wss = Spread("BLT10")
wss.open_sheet("Sheet1")
wss.df_to_sheet(blt10, start = "A1", index = False, )


boredape=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_BOREDAPE.csv")
wss = Spread("BLT_BOREDAPE")
wss.open_sheet("Sheet1")
wss.df_to_sheet(boredape, start = "A1", index = False, )


boredapekennelclub=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_BOREDAPEKENNELCLUB.csv")
wss = Spread("BLT_BAKC")
wss.open_sheet("Sheet1")
wss.df_to_sheet(boredapekennelclub, start = "A1", index = False, )


clonex=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_CLONEX.csv")
wss = Spread("BLT_CLONEX")
wss.open_sheet("Sheet1")
wss.df_to_sheet(clonex, start = "A1", index = False, )


coolcats=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_COOLCATS.csv")
wss = Spread("BLT_COOLCATS")
wss.open_sheet("Sheet1")
wss.df_to_sheet(coolcats, start = "A1", index = False, )


cryptokitties=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_CRYPTOKITTIES.csv")
wss = Spread("BLT_CRYPTOKITTIES")
wss.open_sheet("Sheet1")
wss.df_to_sheet(cryptokitties, start = "A1", index = False, )


cryptopunk=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_CRYPTOPUNK.csv")
wss = Spread("BLT_CRYPTOPUNK")
wss.open_sheet("Sheet1")
wss.df_to_sheet(cryptopunk, start = "A1", index = False, )


decentraland=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_DECENTRALAND.csv")
wss = Spread("BLT_DECENTRALAND")
wss.open_sheet("Sheet1")
wss.df_to_sheet(decentraland, start = "A1", index = False, )


games=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_GAMES.csv")
wss = Spread("BLT_GAMES")
wss.open_sheet("Sheet1")
wss.df_to_sheet(games, start = "A1", index = False, )


logindexv=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_LOGINDEX-VOLUME.csv")
wss = Spread("BLT_LONGINDEXV")
wss.open_sheet("Sheet1")
wss.df_to_sheet(logindexv, start = "A1", index = False, )


masterpiece=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_MASTERPIECE.csv")
wss = Spread("BLT_MASTERPIECE")
wss.open_sheet("Sheet1")
wss.df_to_sheet(masterpiece, start = "A1", index = False, )


momentum=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_MOMENTUM.csv")
wss = Spread("BLT_MOMENTUM")
wss.open_sheet("Sheet1")
wss.df_to_sheet(momentum, start = "A1", index = False, )


mutantape=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_MUTANTAPE.csv")
wss = Spread("BLT_MUTANTAPE")
wss.open_sheet("Sheet1")
wss.df_to_sheet(mutantape, start = "A1", index = False, )


nftcoins=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_NFT_COINS.csv")
wss = Spread("BLT_NFTCOINS")
wss.open_sheet("Sheet1")
wss.df_to_sheet(nftcoins, start = "A1", index = False, )


metastocks=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_NFT_METAVERSE_STOCKS.csv")
wss = Spread("BLT_NFT_METASTOCKS")
wss.open_sheet("Sheet1")
wss.df_to_sheet(metastocks, start = "A1", index = False, )


nftcapm=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_NFTCAPM.csv")
wss = Spread("BLT_NFTCAPM")
wss.open_sheet("Sheet1")
wss.df_to_sheet(nftcapm, start = "A1", index = False, )


nftcoincapm=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_NFTCOIN-CAPM.csv")
wss = Spread("BLT_NFTCOINCAPM")
wss.open_sheet("Sheet1")
wss.df_to_sheet(nftcoincapm, start = "A1", index = False, )


pastlosers=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_PASTLOSERS.csv")
wss = Spread("BLT_PASTLOSERS")
wss.open_sheet("Sheet1")
wss.df_to_sheet(pastlosers, start = "A1", index = False, )


pastwinners=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_PASTWINNERS.csv")
wss = Spread("BLT_PASTWINNERS")
wss.open_sheet("Sheet1")
wss.df_to_sheet(pastwinners, start = "A1", index = False, )


penny=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_PENNY.csv")
wss = Spread("BLT_PENNY")
wss.open_sheet("Sheet1")
wss.df_to_sheet(penny, start = "A1", index = False, )


plus=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_PLUS.csv")
wss = Spread("BLT_PLUS")
wss.open_sheet("Sheet1")
wss.df_to_sheet(plus, start = "A1", index = False, )


pudgypenguin=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_PUDGYPENGUIN.csv")
wss = Spread("BLT_PUDGYPENGUIN")
wss.open_sheet("Sheet1")
wss.df_to_sheet(pudgypenguin, start = "A1", index = False, )


rarible=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_RARIBLE.csv")
wss = Spread("BLT_RARIBLE")
wss.open_sheet("Sheet1")
wss.df_to_sheet(rarible, start = "A1", index = False, )


sharperatio=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_SHARPERATIO.csv")
wss = Spread("BLT_SHARPERATIO")
wss.open_sheet("Sheet1")
wss.df_to_sheet(sharperatio, start = "A1", index = False, )


superduck=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_SUPERDUCK.csv")
wss = Spread("BLT_SUPERDUCK")
wss.open_sheet("Sheet1")
wss.df_to_sheet(superduck, start = "A1", index = False, )


virtualland=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_VIRTUALLAND.csv")
wss = Spread("BLT_VIRTUALLAND")
wss.open_sheet("Sheet1")
wss.df_to_sheet(virtualland, start = "A1", index = False, )


volatility=pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_VOLATILITY.csv")
wss = Spread("BLT_VOLATILITY")
wss.open_sheet("Sheet1")
wss.df_to_sheet(volatility, start = "A1", index = False, )


volumedetrend =pd.read_csv(r"C:\Users\User\Desktop\EXCEL-FILES\BLT_VOLUMEDETREND.csv")
wss = Spread("BLT_VOLUMEDETREND")
wss.open_sheet("Sheet1")
wss.df_to_sheet(volumedetrend, start = "A1", index = False, )










