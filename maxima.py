{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww7580\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Maximum value in an array Python script\
\
def find_maxima(array):\
	\'93\'94\'94Returns the positions of the maximum\
	values in the array.\
\
	Example:\
	find_maxima([1,2,1]) \'97> [0,1]\
	find_maxima([2,0,0,-2,2]) \'97> [0,4]\
	\'93\'94\'94\
	\
	max_val=max(array)\
	position=list.index(max_val)\
	\
	return position\
\
find_maxima([1,2,1]) \
find_maxima([2,0,0,-2,2])}