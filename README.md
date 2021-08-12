# Setup
1. You must first go to https://quantum-computing.ibm.com/ and create an account. 
2. After your account is created, navigate to https://lab.quantum-computing.ibm.com/
3. On this page, click on the 'Upload File' button found here:

   ![image](https://user-images.githubusercontent.com/39656777/129139052-3431f766-9636-451f-a6ef-22f18b4a0d42.png)
4. Upload the [ShorDemo2.ipynb](./ShorDemo2.ipynb) file
5. With this file now open in IBM's online IDE, click Run > Run Selected Cells.
6. The program will now run on IBM's simulator. It may take up to 90 seconds to run for `N = 21`. It will calculate the prime factors of your input N and output the possible e and d values you can use for encryption and decryption.
7. If you change the value of N in the code, you must change it in the code for the next two programs as well.
8. You can now run [encrypt.py](./encrypt.py) with the N value and one of the e values generated in the previous step. This program will output your ciphertext at the end of its execution.
9. You can now run [decrypt.py](./decrypt.py) to decrypt the ciphertext generated in the previous step. Input the same N value as before and one of the d values for the e value you got in step 6.
