{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "295dfa45-fac4-4c76-a5d5-1d97fdc3d6f0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' Create an array with numbers from 1 to 10. '"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "''' Create an array with numbers from 1 to 10. '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "34bb08bd-3ba4-4956-acab-69bf06aa0125",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "a = np.arange(1,11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2594e15c-ef1a-4761-a9df-21ce080d047e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  2  3  4  5  6  7  8  9 10]\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1d00fbe1-0a2a-4099-8ae1-fee7379e62ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' now randomly shuffle the numbers\\nwe need to use the random.permutation function'"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "''' now randomly shuffle the numbers\n",
    "we need to use the random.permutation function'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "59c50568-527b-4776-9909-139ecbb70279",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "x must be an integer or at least 1-dimensional",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[31], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m shuffled_array \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39mrandom\u001b[38;5;241m.\u001b[39mpermutation(a)\n",
      "File \u001b[1;32mnumpy\\\\random\\\\mtrand.pyx:4722\u001b[0m, in \u001b[0;36mnumpy.random.mtrand.RandomState.permutation\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: x must be an integer or at least 1-dimensional"
     ]
    }
   ],
   "source": [
    "shuffled_array = np.random.permutation(a)"
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
