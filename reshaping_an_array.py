{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d34525f9-816d-4f97-b2df-0d1b6d836a71",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'creating a 1d array with 36 elements(1-36) and then reshape it into\\nA 2D array with 6 rows and 6 columns.\\nA 3D array with dimensions (3, 3, 4).'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''creating a 1d array with 36 elements(1-36) and then reshape it into\n",
    "A 2D array with 6 rows and 6 columns.\n",
    "A 3D array with dimensions (3, 3, 4).'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e93567bb-f956-407d-ae74-650f8f60585e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "array = np.arange(1,37)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c1af3e5d-9c28-4a9d-8eea-0db90c5437f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24\n",
      " 25 26 27 28 29 30 31 32 33 34 35 36]\n"
     ]
    }
   ],
   "source": [
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6953dac2-dddf-4dab-a307-ef5ce9aa4f5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "reshaped_array = array.reshape(6,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c592a47d-51e6-4979-a164-5d84e80e8815",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24\n",
      " 25 26 27 28 29 30 31 32 33 34 35 36]\n",
      "Reshaped 2D array: [[ 1  2  3  4  5  6]\n",
      " [ 7  8  9 10 11 12]\n",
      " [13 14 15 16 17 18]\n",
      " [19 20 21 22 23 24]\n",
      " [25 26 27 28 29 30]\n",
      " [31 32 33 34 35 36]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Original array:\", array)\n",
    "print(\"Reshaped 2D array:\", reshaped_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "892b48ef-90f6-47b6-a2f9-52654d321fe6",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_reshaped_array = array.reshape(3,3,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "c0f6683c-a4a3-4baa-920c-40f4a77a57f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reshaped 2D array: [[ 1  2  3  4  5  6]\n",
      " [ 7  8  9 10 11 12]\n",
      " [13 14 15 16 17 18]\n",
      " [19 20 21 22 23 24]\n",
      " [25 26 27 28 29 30]\n",
      " [31 32 33 34 35 36]]\n",
      "Reshaped 3D array: [[[ 1  2  3  4]\n",
      "  [ 5  6  7  8]\n",
      "  [ 9 10 11 12]]\n",
      "\n",
      " [[13 14 15 16]\n",
      "  [17 18 19 20]\n",
      "  [21 22 23 24]]\n",
      "\n",
      " [[25 26 27 28]\n",
      "  [29 30 31 32]\n",
      "  [33 34 35 36]]]\n"
     ]
    }
   ],
   "source": [
    "print(\"Reshaped 2D array:\", reshaped_array)\n",
    "print(\"Reshaped 3D array:\", new_reshaped_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1014f0e-c016-4f5e-8f7c-1ad7a050f880",
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
