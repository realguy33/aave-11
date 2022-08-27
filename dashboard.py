#importing and loading stuff
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from subgrounds.subgrounds import Subgrounds
sg = Subgrounds()
import pandas as pd
from datetime import datetime
from subgrounds.subgraph import SyntheticField


st.set_page_config(page_icon="👻", page_title="aave test 2")
st.image('aave.jpg')
st.title(" AAVE dashboard")

st.subheader("AAVE introduction")
st.write("AAVE is decentralized lending and borrowing protocol. It essentially allows users to lend or borrow digital assets and earn/pay interst on them. Many lenders users use AAVE as an alternative to a simple savings account which is why users might be interested in knowing which chain gives them the overall best yield. The lending rate in AAVE is  variable which is why one may want to look at the historical rates available at different chains to determine which might be the best chain to use for lending purposes")
st.write("AAVEv3 was recently launched in march 2022. Since then it has been deployed on various L2s and chains such as Optimism,Polygon,Fantom,Avalanche and Arbitrum")

st.subheader("METHODOLOGY")
st.write("In this dashboard, we will be looking at the varying lending rates on the various chains on which AAVEv3 is available. We will be lookimg at a variety of tokens that are available on all the chains. We will also look at the perfomance of a portfolio containing - LINK,ETH AND DAI. Extra reward tokens have been excluded from this analysis for the sake of simplicity")
st.write(" Harmony has been  excluded from this analysis becuase of the horizon bridge exploit which was leading to inaccurate data.")
st.subheader("Sources-")
st.write("This dashboard was made with the help of Messari's subgraph and subgrounds library. Proper sources as well as a link to the github repository has been provided at the end of this dashboard")
st.subheader("Lending rate analysis of a coin")
st.write("DAI has been select as the default for this analysis but you can select another coin of your choice from the selction")
st.write("Note - you can run your query by clicking on the Update data button but the query can take upto 5-10 minutes to finish so please be patient")





# 0 means optimism, 1 means polygon,2 means harmony, 3 is fantom, 4 is avalanche and 5 is arbitrum
#in hindsight,i should've used a dictionary but i am not typing all that stuff now
DAI = ('0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1','0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063','one1a7th6tunrsvh3k6lvarkvmapat9s6qee9kna05','0x8D11eC38a3EB5E956B052f67Da8Bdc9bef8Abf3E','0xd586E7F844cEa2F87f50152665BCbc2C279D8d70','0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1')
USDT = ('0x94b008aA00579c1307B0EF2c499aD98a8ce58e58','0xc2132D05D31c914a87C6611C10748AEb04B58e8F','one18s4ch6vu2pvnpq0252njfu9c9p044w50gw3l6y','0x049d68029688eAbF473097a2fC38ef61633A3C7A','0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7','0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9')
USDC = ('0x7F5c764cBc14f9669B88837ca1490cCa17c31607','0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174','one1np293efrmv74xyjcz0kk3sn53x0fm745f2hsuc','0x04068DA6C83AFCFA0e13ba15A6696662335D5B75','0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E','0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8')
CHAINLINK = ('0x350a791Bfc2C21F9Ed5d10980Dad2e2638ffa7f6','0x53E0bca35eC356BD5ddDFebbD1Fc0fD03FaBad39','one1yxzn9gf28zdy4yhup30my2gp68qerx929rv2ns','0xb3654dc3D10Ea7645f8319668E8F54d2574FBdC8','0x5947BB275c521040051D82396192181b413227A3','0xf97f4df75117a78c1A5a0DBb814Af92458539FB4')
BTC = ('0x68f180fcCe6836688e9084f035309E29Bf0A2095','0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6','one1xz2uw4tmev5kenrwxc77qxmkpwsrrukel9ucc5','0x321162Cd933E2Be498Cd2267a90534A804051b11','0x50b7545627a5162F82A992c33b87aDc75187B218','0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f')
ETH = ('0x4200000000000000000000000000000000000006','0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619','one1dxparek77d5scntpdvf4j7sfucvnagqnhhfaun','0x74b23882a30290451A17c44f4F05243b6b58C76d','0x49D5c2BdFfac6CE2BFdB6640F4F80f226bc10bAB','0x82aF49447D8a07e3bd95BD0d56f35241523fBab1')
AAVE = ('0x76FB31fb4af56892A25e32cFC43De717950c9278','0xD6DF932A45C0f255f85145f286eA0b292B21C90B','one1euer4tv72g4e8ugux5k255v66rs5adq0amhn2c','0x6a07A792ab2965C72a5B8088d3a069A7aC3a993B','0x63a72806098Bd3D9520cC43356dD78afe5D386D9','0xba5DdD1f9d7F570dc94a51479a000E3BCE967196')





chainlist = ["optimism","polygon","fantom","avalanche","arbitrum"]
coinlist = ["DAI","USDT","USDC","CHAINLINK","BTC","ETH","AAVE"]
chains = st.multiselect("Select the chains", chainlist,default = chainlist)
coin = st.selectbox("select a coin",coinlist)

if(coin == "DAI"):
    chosen = DAI
    
elif(coin == "USDT"):
    chosen = USDT  
      
elif(coin == "USDC"):
    chosen = USDC
elif(coin=="CHAINLINK"):
    chosen = CHAINLINK
elif(coin=="BTC"):
    chosen = BTC
elif(coin=="ETH"):
    chosen = ETH
elif(coin=="AAVE"):
    chosen = AAVE    






#defining a function that will take the values and create a dataframe that can be worked with
def optfunc(value):
    aop =  sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v3-optimism')

    aop.MarketDailySnapshot.datetime = SyntheticField(
    lambda timestamp: str(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    aop.MarketDailySnapshot.timestamp
    )

    marketD = aop.Query.marketDailySnapshots(
    where =[aop.MarketDailySnapshot.market == value.lower()],
    first = 365,
    orderBy = aop.MarketDailySnapshot.timestamp,
    orderDirection = 'desc'
    )

    a = sg.query_df([marketD.rates,marketD.datetime])
    b = a[a["marketDailySnapshots_rates_side"]=='LENDER']
    c = b[["marketDailySnapshots_rates_rate","marketDailySnapshots_datetime"]]

    c.rename(columns = {'marketDailySnapshots_rates_rate':'Optimism_rate'}, inplace = True)
    return(c)


def polfunc(value):
    apol = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v3-polygon')

    apol.MarketDailySnapshot.datetime = SyntheticField(
    lambda timestamp: str(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    apol.MarketDailySnapshot.timestamp
    )

    marketD = apol.Query.marketDailySnapshots(
    where =[apol.MarketDailySnapshot.market == value.lower()],
    first = 365,
    orderBy = apol.MarketDailySnapshot.timestamp,
    orderDirection = 'desc'
    )

    a = sg.query_df([marketD.rates,marketD.datetime])
    b = a[a["marketDailySnapshots_rates_side"]=='LENDER']
    c = b[["marketDailySnapshots_rates_rate","marketDailySnapshots_datetime"]]

    c.rename(columns = {'marketDailySnapshots_rates_rate':'polygon_rate'}, inplace = True)
    return(c)


def harfunc(value):
    ahar = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v3-harmony')

    ahar.MarketDailySnapshot.datetime = SyntheticField(
    lambda timestamp: str(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    ahar.MarketDailySnapshot.timestamp
    )

    marketD = ahar.Query.marketDailySnapshots(
    where =[ahar.MarketDailySnapshot.market == value.lower()],
    first = 365,
    orderBy = ahar.MarketDailySnapshot.timestamp,
    orderDirection = 'desc'
    )

    a = sg.query_df([marketD.rates,marketD.datetime])
    b = a[a["marketDailySnapshots_rates_side"]=='LENDER']
    c = b[["marketDailySnapshots_rates_rate","marketDailySnapshots_datetime"]]

    c.rename(columns = {'marketDailySnapshots_rates_rate':'Harmony_rate'}, inplace = True)
    return(c)


def fanfunc(value):
    afan = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v3-fantom')

    afan.MarketDailySnapshot.datetime = SyntheticField(
    lambda timestamp: str(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    afan.MarketDailySnapshot.timestamp
    )

    marketD = afan.Query.marketDailySnapshots(
    where =[afan.MarketDailySnapshot.market == value.lower()],
    first = 365,
    orderBy = afan.MarketDailySnapshot.timestamp,
    orderDirection = 'desc'
    )

    a = sg.query_df([marketD.rates,marketD.datetime])
    b = a[a["marketDailySnapshots_rates_side"]=='LENDER']
    c = b[["marketDailySnapshots_rates_rate","marketDailySnapshots_datetime"]]

    c.rename(columns = {'marketDailySnapshots_rates_rate':'Fantom_rate'}, inplace = True)
    return(c)


def avafunc(value):
    aava = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v3-avalanche')

    aava.MarketDailySnapshot.datetime = SyntheticField(
    lambda timestamp: str(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    aava.MarketDailySnapshot.timestamp
    )

    marketD = aava.Query.marketDailySnapshots(
    where =[aava.MarketDailySnapshot.market == value.lower()],
    first = 365,
    orderBy = aava.MarketDailySnapshot.timestamp,
    orderDirection = 'desc'
    )

    a = sg.query_df([marketD.rates,marketD.datetime])
    b = a[a["marketDailySnapshots_rates_side"]=='LENDER']
    c = b[["marketDailySnapshots_rates_rate","marketDailySnapshots_datetime"]]
    c.rename(columns = {'marketDailySnapshots_rates_rate':'Avalanche_rate'}, inplace = True)
    return(c)


def arbfunc(value):
    aarb = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v3-arbitrum')

    aarb.MarketDailySnapshot.datetime = SyntheticField(
    lambda timestamp: str(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')),
    SyntheticField.STRING,
    aarb.MarketDailySnapshot.timestamp
    )

    marketD = aarb.Query.marketDailySnapshots(
    where =[aarb.MarketDailySnapshot.market == value.lower()],
    first = 365,
    orderBy = aarb.MarketDailySnapshot.timestamp,
    orderDirection = 'desc'
    )

    a = sg.query_df([marketD.rates,marketD.datetime])
    b = a[a["marketDailySnapshots_rates_side"]=='LENDER']
    c = b[["marketDailySnapshots_rates_rate","marketDailySnapshots_datetime"]]

    c.rename(columns = {'marketDailySnapshots_rates_rate':'Arbitrum_rate'}, inplace = True)
    return(c)



update = st.button('Update data')

if(update == False):
    chart = pd.read_csv("data.csv")
elif(update == True):
    plotop = pd.DataFrame()
    plotpol = pd.DataFrame()
    plothar = pd.DataFrame()
    plotfan = pd.DataFrame()
    plotava = pd.DataFrame()
    plotarb = pd.DataFrame()


    for i in range(len(chains)):
        if(chains[i]=="optimism"):
            plotop = optfunc(chosen[0])
        elif(chains[i]=="polygon"):
            plotpol = polfunc(chosen[1])
    #    elif(chains[i]=="harmony"):
    #        plothar == harfunc(chosen[2])
        elif(chains[i]=="fantom"):
            plotfan = fanfunc(chosen[3])
        elif(chains[i]=="avalanche"):
            plotava = avafunc(chosen[4])
        elif(chains[i]=="arbitrum"):
            plotarb= arbfunc(chosen[5]) 

    ch1 = pd.merge(plotop,plotpol,on='marketDailySnapshots_datetime')
    ch2= pd.merge(ch1,plotfan,on='marketDailySnapshots_datetime')
    ch3= pd.merge(ch2,plotava,on='marketDailySnapshots_datetime')
    chart= pd.merge(ch3,plotarb,on='marketDailySnapshots_datetime')        


plot = px.line(chart,x='marketDailySnapshots_datetime',y=['Arbitrum_rate','Avalanche_rate','Fantom_rate','polygon_rate','Optimism_rate'])
plot.update_layout(
    xaxis_title="date",
    yaxis_title="lending rate",
)
st.plotly_chart(plot)

st.write("it appears that lending rates were very high on various chains at the start of the protocol, this was probably because the protocol was still new and there were less lenders.")
st.write("Fantom had a temporary strong spike in the beggining but the rate seems to have falllen off. The same is true for Avalanche. It appears that ETH L2 are giving better rates now.")
st.write("Optimism seems to be giving the best lending rate since the start of August, although arbitrum is catching up. Optimism is still very ahead of arbitrum because it also offers additional OP tokens to its lenders")

lnk = pd.read_csv('link.csv')
et = pd.read_csv('eth.csv')
di = pd.read_csv('data.csv')

st.subheader("Measuring yield of a portfolio")
st.write("I have chosen a portfolio containing - LINK,ETH and DAI. It is assumed that i have equal amounts(in USD) of the three token. Hence, the lending rate is calculated adding the three lending rates and dividing the addition by three.")
portop1 = lnk['Optimism_rate'].add(et['Optimism_rate'],fill_value=0)
portop2 = (di['Optimism_rate'].add(portop1,fill_value=0))/3

portpol1 = lnk['polygon_rate'].add(et['polygon_rate'],fill_value=0)
portpol2 = (di['polygon_rate'].add(portpol1,fill_value=0))/3

portfan1 = lnk['Fantom_rate'].add(et['Fantom_rate'],fill_value=0)
portfan2 = (di['Fantom_rate'].add(portfan1,fill_value=0))/3

portava1 = lnk['Avalanche_rate'].add(et['Avalanche_rate'],fill_value=0)
portava2 = (di['Avalanche_rate'].add(portava1,fill_value=0))/3

portarb1 = lnk['Arbitrum_rate'].add(et['Arbitrum_rate'],fill_value=0)
portarb2 = (di['Arbitrum_rate'].add(portarb1,fill_value=0))/3

portop3 =  pd.concat([portop2,lnk['marketDailySnapshots_datetime']],axis = 1,)


portpol3 =  pd.concat([portpol2,lnk['marketDailySnapshots_datetime']],axis = 1,)


portfan3 =  pd.concat([portfan2,lnk['marketDailySnapshots_datetime']],axis = 1,)


portava3 =  pd.concat([portava2,lnk['marketDailySnapshots_datetime']],axis = 1,)


portarb3 =  pd.concat([portarb2,lnk['marketDailySnapshots_datetime']],axis = 1,)
st.subheader("Optimism")

st.plotly_chart(px.line(portop3,y='Optimism_rate',x='marketDailySnapshots_datetime'))
st.subheader("Polygon")

st.plotly_chart(px.line(portpol3,y='polygon_rate',x='marketDailySnapshots_datetime'))
st.subheader("Fantom-")

st.plotly_chart(px.line(portfan3,y='Fantom_rate',x='marketDailySnapshots_datetime'))
st.subheader("Avalanche-")

st.plotly_chart(px.line(portava3,y='Avalanche_rate',x='marketDailySnapshots_datetime'))

st.subheader("Arbitrum-")

st.plotly_chart(px.line(portarb3,y='Arbitrum_rate',x='marketDailySnapshots_datetime'))































