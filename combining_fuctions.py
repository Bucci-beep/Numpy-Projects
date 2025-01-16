{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f6c25fd5-4416-4a67-bf59-d1bcc7bf3776",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' creating a 3 by 3 array filled with numbers from 1 t0 9 using arange and reshape '"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''creating a 3 by 3 array filled with numbers from 1 to 9 using arange and reshape'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e97093b8-d327-4d95-a815-c248b6db71d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array = np.arange(1,10).reshape(3,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cca2fc4e-9051-42d1-a511-254c6ce80a70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "61e008d3-97c1-4941-8870-bd9425a5bd8b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'shuffle the array rows using the np.random.permutation'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''shuffle the array rows using the np.random.permutation'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "bc0d6b41-893e-4dee-91af-c1c55afab936",
   "metadata": {},
   "outputs": [],
   "source": [
    "array = np.random.permutation(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f9f50c80-fc41-44df-8b49-a094cae47e1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<built-in method permutation of numpy.random.mtrand.RandomState object at 0x00000254B8183C40>\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93e1d2bc-7753-4af3-a622-2d35cd8e9ea4",
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
