# -*- coding: utf-8 -*-
# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An example of showing geographic data."""

import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

script = '<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no"><link rel="shortcut icon" href="./favicon.png"><title>Streamlit</title><script async src="https://www.googletagmanager.com/gtag/js?id=G-99G772J80M"></script><script>function gtag(){dataLayer.push(arguments)}window.dataLayer=window.dataLayer||[],gtag("js",new Date),gtag("config","G-99G772J80M")</script><script src="./vendor/viz/viz-1.8.0.min.js" type="javascript/worker"></script><script src="./vendor/bokeh/bokeh-2.4.1.min.js"></script><script src="./vendor/bokeh/bokeh-widgets-2.4.1.min.js"></script><script src="./vendor/bokeh/bokeh-tables-2.4.1.min.js"></script><script src="./vendor/bokeh/bokeh-api-2.4.1.min.js"></script><script src="./vendor/bokeh/bokeh-gl-2.4.1.min.js"></script><script src="./vendor/bokeh/bokeh-mathjax-2.4.1.min.js"></script><link href="./static/css/5.71be5c0a.chunk.css" rel="stylesheet"><link href="./static/css/main.b46f6fce.chunk.css" rel="stylesheet"></head><body><noscript>You need to enable JavaScript to run this app.</noscript><div id="root"></div><script>!function(o){function e(e){for(var t,r,c=e[0],n=e[1],f=e[2],d=0,a=[];d<c.length;d++)r=c[d],Object.prototype.hasOwnProperty.call(s,r)&&s[r]&&a.push(s[r][0]),s[r]=0;for(t in n)Object.prototype.hasOwnProperty.call(n,t)&&(o[t]=n[t]);for(b&&b(e);a.length;)a.shift()();return i.push.apply(i,f||[]),u()}function u(){for(var e,t=0;t<i.length;t++){for(var r=i[t],c=!0,n=1;n<r.length;n++){var f=r[n];0!==s[f]&&(c=!1)}c&&(i.splice(t--,1),e=p(p.s=r[0]))}return e}var r={},l={4:0},s={4:0},i=[];function p(e){if(r[e])return r[e].exports;var t=r[e]={i:e,l:!1,exports:{}};return o[e].call(t.exports,t,t.exports,p),t.l=!0,t.exports}p.e=function(i){var e=[];l[i]?e.push(l[i]):0!==l[i]&&{7:1}[i]&&e.push(l[i]=new Promise(function(e,c){for(var t="static/css/"+({}[i]||i)+"."+{0:"31d6cfe0",1:"31d6cfe0",2:"31d6cfe0",6:"31d6cfe0",7:"f5138d60",8:"31d6cfe0",9:"31d6cfe0",10:"31d6cfe0",11:"31d6cfe0",12:"31d6cfe0",13:"31d6cfe0",14:"31d6cfe0",15:"31d6cfe0",16:"31d6cfe0",17:"31d6cfe0",18:"31d6cfe0",19:"31d6cfe0",20:"31d6cfe0",21:"31d6cfe0",22:"31d6cfe0",23:"31d6cfe0",24:"31d6cfe0",25:"31d6cfe0",26:"31d6cfe0",27:"31d6cfe0",28:"31d6cfe0",29:"31d6cfe0",30:"31d6cfe0",31:"31d6cfe0",32:"31d6cfe0",33:"31d6cfe0",34:"31d6cfe0",35:"31d6cfe0",36:"31d6cfe0",37:"31d6cfe0",38:"31d6cfe0",39:"31d6cfe0",40:"31d6cfe0",41:"31d6cfe0",42:"31d6cfe0",43:"31d6cfe0",44:"31d6cfe0"}[i]+".chunk.css",n=p.p+t,r=document.getElementsByTagName("link"),f=0;f<r.length;f++){var d=(o=r[f]).getAttribute("data-href")||o.getAttribute("href");if("stylesheet"===o.rel&&(d===t||d===n))return e()}var a=document.getElementsByTagName("style");for(f=0;f<a.length;f++){var o;if((d=(o=a[f]).getAttribute("data-href"))===t||d===n)return e()}var u=document.createElement("link");u.rel="stylesheet",u.type="text/css",u.onload=e,u.onerror=function(e){var t=e&&e.target&&e.target.src||n,r=new Error("Loading CSS chunk "+i+" failed.\n("+t+")");r.code="CSS_CHUNK_LOAD_FAILED",r.request=t,delete l[i],u.parentNode.removeChild(u),c(r)},u.href=n,document.getElementsByTagName("head")[0].appendChild(u)}).then(function(){l[i]=0}));var r=s[i];if(0!==r)if(r)e.push(r[2]);else{var t=new Promise(function(e,t){r=s[i]=[e,t]});e.push(r[2]=t);var c,n=document.createElement("script");n.charset="utf-8",n.timeout=120,p.nc&&n.setAttribute("nonce",p.nc),n.src=p.p+"static/js/"+({}[i]||i)+"."+{0:"fa6f70b2",1:"e3273bb6",2:"aff84428",6:"07f53c8c",7:"1b81d86c",8:"88dab8a1",9:"490c6744",10:"59a61a26",11:"58050b9e",12:"b25d2810",13:"b92a59d5",14:"05e8b407",15:"c51b7d38",16:"f3a702a6",17:"3a5218e5",18:"0e38b13d",19:"542bc821",20:"c8e5fd91",21:"cdddcbf1",22:"50a4e3a7",23:"6f2b3f13",24:"39a159c5",25:"b80d914e",26:"4221aec2",27:"cc779cad",28:"15b19c4a",29:"9201c720",30:"142c51aa",31:"53201f1e",32:"5f642b82",33:"ccc13171",34:"b0e51a9f",35:"802337d3",36:"272ed0a6",37:"cc6d11ab",38:"16d11e48",39:"43d78ffd",40:"f7de80d3",41:"b73ac215",42:"4d726bb3",43:"d3710f2d",44:"462bb128"}[i]+".chunk.js";var f=new Error;c=function(e){n.onerror=n.onload=null,clearTimeout(d);var t=s[i];if(0!==t){if(t){var r=e&&("load"===e.type?"missing":e.type),c=e&&e.target&&e.target.src;f.message="Loading chunk "+i+" failed.\n("+r+": "+c+")",f.name="ChunkLoadError",f.type=r,f.request=c,t[1](f)}s[i]=void 0}};var d=setTimeout(function(){c({type:"timeout",target:n})},12e4);n.onerror=n.onload=c,document.head.appendChild(n)}return Promise.all(e)},p.m=o,p.c=r,p.d=function(e,t,r){p.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},p.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},p.t=function(t,e){if(1&e&&(t=p(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var r=Object.create(null);if(p.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var c in t)p.d(r,c,function(e){return t[e]}.bind(null,c));return r},p.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return p.d(t,"a",t),t},p.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},p.p="./",p.oe=function(e){throw console.error(e),e};var t=this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[],c=t.push.bind(t);t.push=e,t=t.slice();for(var n=0;n<t.length;n++)e(t[n]);var b=c;u()}([])</script><script src="./static/js/5.7ed33730.chunk.js"></script><script src="./static/js/main.d8e12ea6.chunk.js"></script></body></html>'

st.markdown(script, unsafe_allow_html=True)

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="NYC Ridesharing Demo", page_icon=":taxi:")

# LOAD DATA ONCE
@st.experimental_singleton
def load_data():
    data = pd.read_csv(
        "uber-raw-data-sep14.csv.gz",
        nrows=100000,  # approx. 10% of data
        names=[
            "date/time",
            "lat",
            "lon",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=[
            "date/time"
        ],  # set as datetime instead of converting after the fact
    )

    return data


# FUNCTION FOR AIRPORT MAPS
def map(data, lat, lon, zoom):
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )


# FILTER DATA FOR A SPECIFIC HOUR, CACHE
@st.experimental_memo
def filterdata(df, hour_selected):
    return df[df["date/time"].dt.hour == hour_selected]


# CALCULATE MIDPOINT FOR GIVEN SET OF DATA
@st.experimental_memo
def mpoint(lat, lon):
    return (np.average(lat), np.average(lon))


# FILTER DATA BY HOUR
@st.experimental_memo
def histdata(df, hr):
    filtered = data[
        (df["date/time"].dt.hour >= hr) & (df["date/time"].dt.hour < (hr + 1))
    ]

    hist = np.histogram(filtered["date/time"].dt.minute, bins=60, range=(0, 60))[0]

    return pd.DataFrame({"minute": range(60), "pickups": hist})


# STREAMLIT APP LAYOUT
data = load_data()

# LAYING OUT THE TOP SECTION OF THE APP
row1_1, row1_2 = st.columns((2, 3))

# SEE IF THERE'S A QUERY PARAM IN THE URL (e.g. ?pickup_hour=2)
# THIS ALLOWS YOU TO PASS A STATEFUL URL TO SOMEONE WITH A SPECIFIC HOUR SELECTED,
# E.G. https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/main?pickup_hour=2
if not st.session_state.get("url_synced", False):
    try:
        pickup_hour = int(st.experimental_get_query_params()["pickup_hour"][0])
        st.session_state["pickup_hour"] = pickup_hour
        st.session_state["url_synced"] = True
    except KeyError:
        pass

# IF THE SLIDER CHANGES, UPDATE THE QUERY PARAM
def update_query_params():
    hour_selected = st.session_state["pickup_hour"]
    st.experimental_set_query_params(pickup_hour=hour_selected)


with row1_1:
    st.title("NYC Uber Ridesharing Data")
    hour_selected = st.slider(
        "Select hour of pickup", 0, 23, key="pickup_hour", on_change=update_query_params
    )


with row1_2:
    st.write(
        """
    ##
    Examining how Uber pickups vary over time in New York City's and at its major regional airports.
    By sliding the slider on the left you can view different slices of time and explore different transportation trends.
    """
    )

# LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
row2_1, row2_2, row2_3, row2_4 = st.columns((2, 1, 1, 1))

# SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
la_guardia = [40.7900, -73.8700]
jfk = [40.6650, -73.7821]
newark = [40.7090, -74.1805]
zoom_level = 12
midpoint = mpoint(data["lat"], data["lon"])

with row2_1:
    st.write(
        f"""**All New York City from {hour_selected}:00 and {(hour_selected + 1) % 24}:00**"""
    )
    map(filterdata(data, hour_selected), midpoint[0], midpoint[1], 11)

with row2_2:
    st.write("**La Guardia Airport**")
    map(filterdata(data, hour_selected), la_guardia[0], la_guardia[1], zoom_level)

with row2_3:
    st.write("**JFK Airport**")
    map(filterdata(data, hour_selected), jfk[0], jfk[1], zoom_level)

with row2_4:
    st.write("**Newark Airport**")
    map(filterdata(data, hour_selected), newark[0], newark[1], zoom_level)

# CALCULATING DATA FOR THE HISTOGRAM
chart_data = histdata(data, hour_selected)

# LAYING OUT THE HISTOGRAM SECTION
st.write(
    f"""**Breakdown of rides per minute between {hour_selected}:00 and {(hour_selected + 1) % 24}:00**"""
)

st.altair_chart(
    alt.Chart(chart_data)
    .mark_area(
        interpolate="step-after",
    )
    .encode(
        x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
        y=alt.Y("pickups:Q"),
        tooltip=["minute", "pickups"],
    )
    .configure_mark(opacity=0.2, color="red"),
    use_container_width=True,
)
