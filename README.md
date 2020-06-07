# Speaker-Recognition

* Base project: [orchidas](https://github.com/orchidas/Speaker-Recognition?fbclid=IwAR3_Cpf-L0WXXs92E1HfkH0xrU7nTyfX7M4qPgj9V0cEgBOzhAzKGpsFaxU)

* Automatic Speaker Recognition algorithms in Python

* This repository contains Python programs that can be used for Automatic Speaker Recognition. ASR is done by extracting MFCCs and LPCs from each speaker and then forming a speaker-specific codebook
of the same by using Vector Quantization (I like to think of it as a fancy name for NN-clustering). 
After that, the system is trained and tested for 8 different speakers. 

* Create virtualenv with:

	virtualenv -p python3 .env
	. .env/bin/activate
	pip install -r requirements.txt

* To test the algorithm, run test.py. Certain parameters are open to be changed, such as the order of LPC coefficients, the number of Mel filterbanks and the number of centroids in each codebook.
Everything is included in the repository, including .wav files for testing and training, hence cloning it and running test.py should work. 

* Add record function: The algorithm will start by recording the sound from your microphone (6 seconds long). After the testing you will need to delete the s1 file in test folder just type test\s1.wav when it asked u to enter filename.

### Group7.The sound files in the train folder belongs to the following members:
* s1-random sound :)
* s2-Huong Giang
* s3-Hai Long
* s4-Long Vu
* s5-Ba Cuong
* s6-Minh Phuc
* s7-2T
* s8-Minh Hoang
