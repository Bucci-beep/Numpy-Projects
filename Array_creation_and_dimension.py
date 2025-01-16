{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3870957-ecdb-4925-a4b9-c302b69bf9db",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Create a 1D NumPy array with numbers from 1 to 15.'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9da91883-54b4-4e3d-99ae-6cd40af3fd8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a =np.arange(1,16)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50ff1b5c-9343-4a2f-9569-23d0e15330c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Convert the 1D array into a 2D array with 3 rows and 5 columns.'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "8d85c4e3-77d3-4cfc-aea9-bdb71e908004",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4  5]\n",
      " [ 6  7  8  9 10]\n",
      " [11 12 13 14 15]]\n"
     ]
    }
   ],
   "source": [
    "a = np.arange(1,16).reshape(3,5)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "db7b7974-4d6f-483b-82db-3df4fa3dd100",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' Check the dimensions and and shape of the array'"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "''' Check the dimensions and and shape of the array'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "4ec77d68-db71-4f65-ab16-e383dcf5f80d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d3f61b83-1b6a-418a-a98f-3829129f823b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 5)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a4fd38a-7161-4110-a198-5f3d2b207f7b",
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
