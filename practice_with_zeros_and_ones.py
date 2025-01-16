{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5c055258-c9df-4060-8b1a-9b112784f7f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'A 1D array of size 5 filled with zeros.\\nA 2D array with 2 rows and 3 columns filled with ones.\\nA 3D array of shape (2, 3, 4) filled with zeros.\\nPrint all arrays along with their shapes.'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''A 1D array of size 5 filled with zeros.\n",
    "A 2D array with 2 rows and 3 columns filled with ones.\n",
    "A 3D array of shape (2, 3, 4) filled with zeros.\n",
    "Print all arrays along with their shapes.'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2c70651f-6ef6-4cc8-bd61-2856c53e8bbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "one_array = np.zeros((5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c3ae63ff-a6e5-4016-b367-02271af98480",
   "metadata": {},
   "outputs": [],
   "source": [
    "two_array = np.ones((2,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0495104c-72ba-4a00-8c59-6877170f85bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "three_array = np.zeros((2,3,4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3afc8848-6665-418d-a495-c42ac9def9a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1D array: [0. 0. 0. 0. 0.]\n",
      "(5,)\n"
     ]
    }
   ],
   "source": [
    "print(\"1D array:\", one_array)\n",
    "print(\"1D shape:\",one_array.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a4c5e1a-7ea1-4acb-bfff-f65e174b09a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"2D array:\", two_array)\n",
    "print(\"2D shape:\",one_array.shape)"
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
