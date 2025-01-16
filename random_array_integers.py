{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c5401aa3-606b-40ec-95ad-0cd50d237ea8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Generate a 1D array with 12 random integers'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''Generate a 1D array with 12 random integers.\n",
    "we use the random.randint to generate random numbers in a SPECIFIED RANGE'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "36399e18-a26f-48db-aeb2-24bb6d19dfc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array = np.random.randint(1,101, size =12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "fceb71b7-4abd-4af8-9793-7845af0f76a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[33 26 14 66 34 50  2 98 24 35 39 11]\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1456f933-009c-497c-ab49-a30ec6be4679",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'now reshape the array into a 3 by 4 matrix'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''now reshape the array into a 3 by 4 matrix'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "07352927-6b92-463e-823a-932916f89915",
   "metadata": {},
   "outputs": [],
   "source": [
    "array = np.random.randint(1,101, size =12)\n",
    "new_array = np.random.randint(1,101, size =12).reshape(3,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "d1438244-c723-4acb-926d-ecf5e36260a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "New Array: [[55  1 21 81]\n",
      " [55 60 73 25]\n",
      " [29 42 73 48]]\n"
     ]
    }
   ],
   "source": [
    "print(\"New Array:\", new_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1920421-5644-4ea5-87ed-62bafb9f8d2f",
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
