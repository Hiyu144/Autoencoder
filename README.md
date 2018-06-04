# Autoencoder

SVHN and USPS datasets are in *.mat format, therefore, it is nescessary to pre-process these 2 datasets, convert them to *.pkl format and [0, 1] range
The code for this part is in svhn_handler.py and usps_handler.py files.

Both SdA.py and dA.py are currently for SVHN. In order to run other datasets, some parameters must be modified.

After execution, the filters can be for SdA and dA can be found in theirs respective folder.

This project is based on the tutorial on Deeplearning.net, however, some chances were made and the handler files are my owns. 

Due to size restriction, SVHN dataset cannot be uploaded to GitHub. The set can be found in the following link:  http://ufldl.stanford.edu/housenumbers/
