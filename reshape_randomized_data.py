{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9fc90eaf-ad1a-4cb1-9645-3b4c76745a63",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'generating a 1d array of 12 consecutive numbers from 1 and then suffling it randomly'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''generating a 1d array of 12 consecutive numbers from 1 and then shuffling it randomly'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f77ab627-5661-4b16-b960-5194eabf26ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array = np.arange(1,13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fe183a8e-edda-4226-90a4-5f2a0f30d2bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  2  3  4  5  6  7  8  9 10 11 12]\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a8d62a17-f910-4675-8182-6ae24e257333",
   "metadata": {},
   "outputs": [],
   "source": [
    "reshuffled_array = np.random.permutation(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3cc75f2b-4161-44f0-8a17-a513e1a14b18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2  4  6 12  7 10  5  3  9  8 11  1]\n"
     ]
    }
   ],
   "source": [
    "print(reshuffled_array)"
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
