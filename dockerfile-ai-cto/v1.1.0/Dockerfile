FROM datamachines/cudnn_tensorflow_opencv:11.6.2_2.9.1_3.4.16-20220815

RUN python3 -m pip install --upgrade pip

RUN apt-get install -y \
	build-essential \
	cmake \
	git \
	unzip \
	pkg-config \
	libopenblas-dev \
	liblapack-dev \
	libhdf5-dev \
	python3-h5py \
	graphviz \
	&& apt-get clean \
	&& rm -fr /var/lib/apt/lists/*

RUN python3 -m pip install numpy matplotlib scipy==1.10.1 seaborn pandas notebook pyarrow scikit-learn pydot-ng theano pooch
