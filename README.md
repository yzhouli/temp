# Experimental Settings

**Platform Settings:** The experimental platform uses an M1 chip with 16GB memory, Python 3.10 and Tensorflow 2.10. The pre-trained BERT model is a transformers library version 4.37.2, with the model name ”bert-base-uncased”. 

**Algorithm Settings:** The MFCC extraction algorithm uses librosa library. Subsequently, Adam is chosen as the model optimizer, and the learning rate is set to 0.001. Meanwhile, the training time of the model is set to 100 epochs, and the optimal model parameters are preserved using an early stopping mechanism. The hyper-parameters of the model are set as follows: threshold f ansThre=partThre=1000, decay factor α=0.62/0.68, signal length (number of sampling points) T=5000/7500.
