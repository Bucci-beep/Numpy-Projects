{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "df729eb3-956d-48a4-b7a0-88d4e461faa7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Create a 1D NumPy array of 20 consecutive numbers starting from 5.'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Create a 1D NumPy array of 20 consecutive numbers starting from 5.'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7c87ce9d-4c0c-488b-b8c6-28f80bb4d11c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array = np.arange(5,25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "113c14c4-76cc-44eb-81fb-3b631f7c6837",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3b636d53-96b6-4dca-b805-154efb46ec99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Reshape it into a 2D array with 4 rows and 5 columns.'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Reshape it into a 2D array with 4 rows and 5 columns.'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f8fba603-032a-4754-8264-2ac40d15ce9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "array = np.arange(5,25)\n",
    "reshaped_array = array.reshape(4,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "fe1844f9-1812-4abd-98b3-77d4369da729",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array: [ 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]\n",
      "Reshaped array: [[ 5  6  7  8  9]\n",
      " [10 11 12 13 14]\n",
      " [15 16 17 18 19]\n",
      " [20 21 22 23 24]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Original array:\", array)\n",
    "print(\"Reshaped array:\", reshaped_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d24a2d4-c281-41da-b204-5a7562c7fded",
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
