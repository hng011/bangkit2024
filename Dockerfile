FROM tensorflow/tensorflow:2.13.0-gpu

RUN python3 -m pip install numpy matplotlib seaborn pandas notebook pyarrow scikit-learn
