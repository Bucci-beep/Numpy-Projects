{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e1cdd0df-2480-4403-981d-3c677997dab2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Create a 1D array with 20 elements (numbers 0 to 19).\\nTry reshaping it into:\\n(4, 5)\\n(3, 5)'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Create a 1D array with 20 elements (numbers 0 to 19).\n",
    "Try reshaping it into:\n",
    "(4, 5)\n",
    "(3, 5)'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "64b287f5-c55b-4d21-bc49-b16e79ebdc51",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array = np.arange(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "301b1cc6-0e0e-44c4-92dd-05ce9ddb151b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2283509f-f4ac-48e4-958a-05a9f7e63090",
   "metadata": {},
   "outputs": [],
   "source": [
    "reshaped_array = array.reshape(4,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d6ec0796-c6f4-4ce7-b392-5452ee359585",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0  1  2  3  4]\n",
      " [ 5  6  7  8  9]\n",
      " [10 11 12 13 14]\n",
      " [15 16 17 18 19]]\n"
     ]
    }
   ],
   "source": [
    "print(reshaped_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b0ea17cb-eb39-4257-99cf-bd7ee795f346",
   "metadata": {},
   "outputs": [],
   "source": [
    "array = np.arange(20)\n",
    "trimmed_array = array[:15]\n",
    "reshaped_array_pro = trimmed_array.reshape(3,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "7adff780-3ab6-4f72-9792-74859ce01913",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0  1  2  3  4]\n",
      " [ 5  6  7  8  9]\n",
      " [10 11 12 13 14]]\n"
     ]
    }
   ],
   "source": [
    "print(reshaped_array_pro)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91586813-f0aa-4a3e-98f0-00cee629e2ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''when reshaping an array where the total number of elements != the total\n",
    "number of elements speified in the shape, a ValueError occurs.\n",
    "We solve that using either of two ways:\n",
    "trimming an arrya by reducing the number of elemets to match the elemts in the \n"
   ]
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
