#!/bin/bash

mv OpenNetworkAnalyzer.desktop OpenNetworkAnalyzer.desktop-bak
sed -e "s,Icon=.*,Icon=$PWD/icon/icon.png,g" OpenNetworkAnalyzer.desktop-bak > OpenNetworkAnalyzer.desktop-bak2
sed -e "s,Exec=.*,Exec=$PWD/main.py,g" OpenNetworkAnalyzer.desktop-bak2 > OpenNetworkAnalyzer.desktop-bak
sed -e "s,Path=.*,Path=$PWD,g" OpenNetworkAnalyzer.desktop-bak > OpenNetworkAnalyzer.desktop

rm OpenNetworkAnalyzer.desktop-bak
rm OpenNetworkAnalyzer.desktop-bak2

chmod +x main.py
chmod +x OpenNetworkAnalyzer.desktop

