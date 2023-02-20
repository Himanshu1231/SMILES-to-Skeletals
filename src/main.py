# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:42:41 2022

@author: ABC
"""

import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

st.title('SMILES to Skeletals')
st.write('This is an application that draws the [skeletal structure](https://en.wikipedia.org/wiki/Skeletal_formula#:~:text=The%20skeletal%20structure%20of%20an,or%20hydrogen%20are%20called%20heteroatoms.) of the molecule from it\'s [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system) structure. It has been built by [@Himanshu Jain]( https://www.linkedin.com/in/himanshu-jain-in/)')

inp = st.text_input('Input SMILES structure',value = 'C1C(=O)CCC(=N)C1')

try:
    inp = Chem.MolFromSmiles(inp)
    if inp is None:
        raise TypeError('Invalid SMILES Structure')
    
    inp = [inp]
    x = Draw.MolsToGridImage(inp, molsPerRow=1,subImgSize = (300,300))
    st.image(x)
except TypeError:
    st.write('Invalid SMILES Structure. Please input a correct SMILES structure or use on of the followings for a demo')
    st.write(' - COc1cc(C=O)ccc1O')
    st.write(' - CC(=O)NCCc1c[nH]c2ccc(OC)cc12')
    st.write(' - [Cu+2].[O-]S(=O)(=O)[O-]') 
    st.write(' - C1CCCCC1C1CCCCC1') 
    st.write(' - C1=CC=CC=C1') 
    
#st.write('This application has been built by [@Himanshu Jain](https://www.linkedin.com/in/himanshujain1999/)')

with st.sidebar:
    st.title('SMILES to Skeletals')
    st.subheader(':copyright: 2022 Himanshu Jain')
    st.write('Email : [himjain567@gmail.com](himajain567@gmail.com)')
    st.write('LinkedIn : https://www.linkedin.com/in/himanshu-jain-in/')
    st.write('Github: https://github.com/himanshu-jain-in/')
    st.write('This application has been built in [Python](https://www.python.org/) using [streamlit](https://streamlit.io/) and [rdkit](RDKithttps://www.rdkit.org)')
    
