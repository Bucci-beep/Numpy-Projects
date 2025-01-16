{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4d1dfd28-26e7-4938-9b03-363fe8c875b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' Generate a NumPy array of even numbers between 10 and 50 (inclusive).'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "''' Generate a NumPy array of even numbers between 10 and 50 (inclusive).'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "61dc898c-cc2a-4619-90d3-654dd48a619a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "a = np.arange(10,51,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "19481454-eb52-4a7a-9ffb-20a758c3a2ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50]\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6e288a33-210b-474d-97c5-4e5c415ca84d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' reshaping the array into a 4 by 5 matrix '"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "''' reshaping the array into a 4 by 5 matrix '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7b6aa155-e349-4aba-8e15-35477cc88231",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.arange(10,51,2)[:20] #the [:20] avoids slicing but creates an array with20 elements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "32ca4d73-113b-422c-8de2-9e7608dbf504",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[10 12 14 16 18]\n",
      " [20 22 24 26 28]\n",
      " [30 32 34 36 38]\n",
      " [40 42 44 46 48]]\n"
     ]
    }
   ],
   "source": [
    "r = a.reshape(4,5)\n",
    "print(r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33595272-1d4a-4c5f-8cbb-275caef3b2a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
